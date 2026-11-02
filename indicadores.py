# [IA] Codex – Indicadores escolhidos pelo aluno.
import pandas as pd


# [IA] Codex – Filtros do Dashboard 2.
def filtrar_desempenho(df, nacionalidade=None, posicao=None, idades=None):
    filtrado = df.copy()
    if nacionalidade is not None:
        filtrado = filtrado.loc[filtrado['nationality'] == nacionalidade]
    if posicao is not None:
        filtrado = filtrado.loc[filtrado['position'] == posicao]
    if idades is not None:
        minimo, maximo = idades
        if minimo > maximo:
            raise ValueError('O intervalo de idade está invertido.')
        filtrado = filtrado.loc[filtrado['age'].between(minimo, maximo, inclusive='both')]
    return filtrado.copy()


# [IA] Codex – Um registro por nome para os gráficos.
def agrupar_jogadores(df):
    return (
        df.groupby('player_name', as_index=False, dropna=True)
        .agg(
            goals=('goals', lambda valores: valores.sum(min_count=1)),
            assists=('assists', lambda valores: valores.sum(min_count=1)),
            age=('age', 'mean'),
        )
    )


# [IA] Codex – Totais e idade média sem ponderar por participações.
def calcular_indicadores(df):
    if df.empty:
        return {'gols': None, 'assistencias': None, 'idade_media': None}
    jogadores = agrupar_jogadores(df)
    gols = df['goals'].sum(min_count=1)
    assistencias = df['assists'].sum(min_count=1)
    idade = jogadores['age'].mean()
    return {
        'gols': int(gols) if pd.notna(gols) else None,
        'assistencias': int(assistencias) if pd.notna(assistencias) else None,
        'idade_media': float(idade) if pd.notna(idade) else None,
    }
