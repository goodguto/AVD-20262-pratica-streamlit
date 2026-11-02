# [IA] Codex – Bibliotecas.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

from dados import (
    CSV_TRATADO, RAIZ, QUANTITATIVAS, COR_NEUTRA, COR_DESTAQUE,
    filtrar_intervalo, correlacionar,
)
from src.data_loader import load_data

st.set_page_config(page_title='FIFA | Laboratório de dados', page_icon='⚽', layout='wide')
sns.set_theme(style='whitegrid', rc={'axes.labelcolor': COR_DESTAQUE})


# [IA] Codex – Cache dos dados.
@st.cache_data(show_spinner=False, max_entries=2)
def dados_em_cache(assinatura):
    return load_data()


# [IA] Codex – Mapa de calor.
def mostrar_correlacao(df, variaveis):
    st.subheader('Correlação de Spearman')
    st.caption('Escala fixa de −1 a 1 · ausências tratadas por pares · mínimo de 3 pares válidos.')
    if df.empty:
        st.info('Nenhuma observação no intervalo. Amplie o filtro para calcular a correlação.')
        return
    matriz, excluidas = correlacionar(df, variaveis)
    if excluidas:
        st.info('Sem correlação para variáveis constantes ou com menos de 3 valores: ' + ', '.join(excluidas))
    if len(matriz) < 2:
        st.info('Selecione pelo menos duas variáveis com variação e dados suficientes.')
        return
    pares = matriz.copy()
    for coluna in pares:
        pares.loc[coluna, coluna] = float('nan')
    if not pares.notna().any().any():
        st.info('Não há pares suficientes para calcular correlações entre as variáveis.')
        return
    fig, ax = plt.subplots(figsize=(max(7, len(matriz) * .8), max(5, len(matriz) * .7)))
    sns.heatmap(matriz, mask=matriz.isna(), annot=True, fmt='.2f', cmap='coolwarm',
                vmin=-1, vmax=1, square=True, ax=ax, cbar_kws={'label': 'Spearman (ρ)'})
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.grid(False)
    fig.tight_layout()
    st.pyplot(fig, width='stretch', alt='Matriz de correlação de Spearman das variáveis selecionadas no intervalo atual.')
    plt.close(fig)
    with st.expander('Ver coeficientes em tabela'):
        st.dataframe(matriz, width='stretch', alt='Coeficientes de Spearman das variáveis selecionadas.')


# [IA] Codex – Histogramas.
def mostrar_histogramas(df, variaveis):
    st.subheader('Distribuição das observações')
    if not variaveis:
        st.info('Escolha ao menos uma variável na barra lateral para exibir histogramas.')
        return
    if df.empty:
        st.info('Nenhuma observação no intervalo. Amplie o filtro para exibir histogramas.')
        return
    colunas = st.columns(2)
    for indice, variavel in enumerate(variaveis):
        with colunas[indice % 2]:
            valores = df[variavel].dropna()
            st.markdown(f'**{variavel}**')
            st.caption(f'{len(valores):,} valores válidos · {df[variavel].isna().sum():,} ausentes'.replace(',', '.'))
            if valores.empty:
                st.info('Sem valores disponíveis para esta variável.')
                continue
            fig, ax = plt.subplots(figsize=(7, 4))
            sns.histplot(x=valores, bins='auto', kde=valores.nunique() > 1,
                         color=COR_NEUTRA, edgecolor=COR_DESTAQUE, ax=ax)
            ax.set_xlabel(variavel)
            ax.set_ylabel('Observações')
            fig.tight_layout()
            st.pyplot(fig, width='stretch', alt=f'Distribuição de {variavel} nas observações do intervalo atual.')
            plt.close(fig)
            if valores.nunique() == 1:
                st.caption('Variável constante neste recorte; curva de densidade desativada.')


# [IA] Codex – Dashboard 2 pendente.
def mostrar_dashboard2():
    st.header('Indicadores de Desempenho no Futebol')
    st.info('Aguardando suas decisões para implementar os indicadores e as três visualizações.')
    caminho = RAIZ / 'entregas/justificativa-metricas.md'
    if caminho.exists():
        st.caption('Arquivo de decisões encontrado. A implementação depende da revisão das escolhas registradas.')
        with st.expander('Consultar decisões registradas pelo aluno'):
            st.text(caminho.read_text(encoding='utf-8'))
    else:
        st.caption('Arquivo ainda ausente: entregas/justificativa-metricas.md.')
    st.markdown('''
Preencha o arquivo com:

- Público-alvo e decisão que o dashboard deve apoiar.
- De 3 a 5 métricas: nome, variáveis, fórmula, unidade, agrupamento e regras para ausentes ou denominador zero.
- Para cada métrica: o que mede, por que foi escolhida e o que comunica ao público.
- Exatamente 3 visualizações complementares: tipo, eixos, agregações e relação com as métricas.
- Filtros: campos, valores iniciais e quais indicadores e gráficos cada um controla.
- Unidade de análise: observação jogador-partida ou agregação explicitamente definida por você.
''')
    st.caption('As justificativas e interpretações serão escritas pelo aluno. Consulte entregas/PENDENCIAS.md.')


# [IA] Codex – Dashboard 2 pendente.
st.title('FIFA · Laboratório de dados')
st.caption('Análise e Visualização de Dados | EDA → aplicação Streamlit')
st.write('Explore distribuições e correlações das observações de desempenho.')
df = None
try:
    manifesto = RAIZ / 'data/proveniencia.json'
    assinatura = (CSV_TRATADO.stat().st_mtime_ns, manifesto.stat().st_mtime_ns)
    df = dados_em_cache(assinatura)
except (FileNotFoundError, ValueError, OSError, pd.errors.ParserError) as erro:
    st.error(f'Não foi possível carregar o dataset: {erro}')

# [IA] Codex – Filtros.
selecionadas = []
filtrado = None
with st.sidebar:
    st.header('Laboratório')
    st.caption('Filtros do Dashboard 1')
    if df is not None:
        selecionadas = st.multiselect('Variáveis quantitativas', QUANTITATIVAS,
                                     default=QUANTITATIVAS, key='variaveis')
        variavel_filtro = st.selectbox('Variável do intervalo', QUANTITATIVAS,
                                      index=QUANTITATIVAS.index('minutes_played'), key='variavel_filtro')
        valores = df[variavel_filtro].dropna()
        if valores.empty:
            st.warning('A variável do filtro não contém valores válidos.')
            filtrado = df.iloc[0:0].copy()
        elif valores.nunique() == 1:
            unico = float(valores.iloc[0])
            st.caption(f'Intervalo constante: {unico:g}. Slider desnecessário.')
            filtrado = filtrar_intervalo(df, variavel_filtro, (unico, unico))
        else:
            inteiro = pd.api.types.is_integer_dtype(valores)
            converter = int if inteiro else float
            minimo, maximo = converter(valores.min()), converter(valores.max())
            intervalo = st.slider('Intervalo de valores', min_value=minimo, max_value=maximo,
                                  value=(minimo, maximo), step=1 if inteiro else 0.01,
                                  key=f'intervalo_{variavel_filtro}')
            filtrado = filtrar_intervalo(df, variavel_filtro, intervalo)
        st.caption('Limites inclusivos. O intervalo afeta todos os gráficos do laboratório.')
    st.divider()
    st.caption('Base: FIFA 2026 Player Performance · versão 2 do Kaggle.')

# [IA] Codex – Abas.
laboratorio, indicadores = st.tabs([
    'Laboratório de Distribuição e Correlação', 'Indicadores de Desempenho no Futebol',
])
with laboratorio:
    st.header('Laboratório de Distribuição e Correlação')
    if df is not None:
        a, b = st.columns(2)
        a.metric('Observações na base', f'{len(df):,}'.replace(',', '.'), border=True)
        b.metric('Observações no intervalo', f'{len(filtrado):,}'.replace(',', '.'), border=True)
        st.caption('Cada linha é uma observação de desempenho; a contagem não representa jogadores únicos.')
        if not selecionadas:
            st.info('Nenhuma variável selecionada. Escolha variáveis na barra lateral.')
        else:
            mostrar_correlacao(filtrado, selecionadas)
            st.divider()
            mostrar_histogramas(filtrado, selecionadas)
        with st.expander('Dados e preparação'):
            st.write('Imputação pela mediana da base completa em market_value_eur_m, pass_accuracy_pct e distance_covered_km. Outliers mantidos, conforme a EDA.')
            st.write('match_id, player_name e indicadores booleanos não entram na correlação.')
            st.caption('A EDA registra limitações de confiabilidade e possíveis dados simulados. Os valores originais foram preservados.')
            st.dataframe(filtrado.head(100), width='stretch', hide_index=True,
                         alt='Prévia das primeiras 100 observações do intervalo atual.')
            st.caption('Prévia limitada às primeiras 100 observações do recorte.')
with indicadores:
    mostrar_dashboard2()
