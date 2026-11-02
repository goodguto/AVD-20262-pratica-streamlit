# [IA] Codex – Esqueleto do app.
import pandas as pd
import streamlit as st
from dados import CSV_TRATADO, RAIZ, QUANTITATIVAS, filtrar_intervalo
from src.data_loader import load_data

st.set_page_config(page_title='FIFA | Laboratório de dados', page_icon='⚽', layout='wide')


# [IA] Codex – Cache dos dados.
@st.cache_data(show_spinner=False, max_entries=2)
def dados_em_cache(assinatura):
    return load_data()


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

# [IA] Codex – Gráficos pendentes.
st.header('Laboratório de Distribuição e Correlação')
if df is not None:
    a, b = st.columns(2)
    a.metric('Observações na base', f'{len(df):,}'.replace(',', '.'))
    b.metric('Observações no intervalo', f'{len(filtrado):,}'.replace(',', '.'))
    st.caption('As contagens representam observações, não jogadores únicos.')
    st.subheader('Correlação')
    st.info('Espaço reservado para o mapa de calor da Aula 22.')
    st.subheader('Distribuição')
    st.info('Espaço reservado para os histogramas da Aula 22.')
