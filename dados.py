# [IA] Codex – Variáveis.
from pathlib import Path
import hashlib

import pandas as pd

RAIZ = Path(__file__).resolve().parent
CSV_ORIGINAL = RAIZ / 'data/raw/fifa2026_player_performance_clean.csv'
CSV_TRATADO = RAIZ / 'data/clean/dataset.csv'
SHA_ORIGINAL = 'dea694afdac57d81b312426e7f576fbe0d6ef82a8fc7e30be0aa018f3fafa8b3'
QUANTITATIVAS = [
    'age', 'market_value_eur_m', 'minutes_played', 'goals', 'assists',
    'shots_on_target', 'pass_accuracy_pct', 'tackles', 'distance_covered_km',
    'match_rating', 'fouls_committed',
]
QUALITATIVAS = [
    'nationality', 'club', 'position', 'season', 'competition',
    'yellow_card', 'red_card', 'injured_flag',
]
COLUNAS = [
    'player_name', 'nationality', 'club', 'position', 'age', 'market_value_eur_m',
    'season', 'competition', 'match_id', 'minutes_played', 'goals', 'assists',
    'shots_on_target', 'pass_accuracy_pct', 'tackles', 'distance_covered_km',
    'match_rating', 'yellow_card', 'red_card', 'fouls_committed', 'injured_flag',
]
IMPUTAR = ['market_value_eur_m', 'pass_accuracy_pct', 'distance_covered_km']
COR_NEUTRA = 'lightgray'
COR_CONTEXTO = '#e9d4d0'
COR_DESTAQUE = '#2d223a'
COR_ALERTA = 'tab:red'


# [IA] Codex – Validar dados.
def validar_dados(df):
    if list(df.columns) != COLUNAS:
        raise ValueError('O CSV não tem as 21 colunas esperadas, na ordem da EDA.')
    if len(df) != 13397:
        raise ValueError('O CSV não tem as 13.397 observações da EDA.')
    for coluna in QUANTITATIVAS:
        if not pd.api.types.is_numeric_dtype(df[coluna]) or pd.api.types.is_bool_dtype(df[coluna]):
            raise ValueError(f'Tipo quantitativo inválido: {coluna}.')


# [IA] Codex – Imputação pela mediana.
def tratar_dados(original):
    tratado = original.copy(deep=True)
    for coluna in IMPUTAR:
        tratado[coluna] = tratado[coluna].fillna(tratado[coluna].median())
    return tratado


# [IA] Codex – Carregar dados.
def carregar_dados():
    import json

    manifesto = RAIZ / 'data/proveniencia.json'
    if not manifesto.exists() or not CSV_TRATADO.exists():
        raise FileNotFoundError('Execute python scripts/preparar_dados.py para preparar os dados.')
    registro = json.loads(manifesto.read_text(encoding='utf-8'))
    if hashlib.sha256(CSV_TRATADO.read_bytes()).hexdigest() != registro['sha256_tratado']:
        raise ValueError('O CSV tratado foi alterado. Refaça a preparação para validar sua origem.')
    df = pd.read_csv(CSV_TRATADO)
    validar_dados(df)
    return df


# [IA] Codex – Filtrar observações.
def filtrar_intervalo(df, coluna, intervalo):
    if coluna not in QUANTITATIVAS or coluna not in df:
        raise ValueError('Selecione uma variável quantitativa válida.')
    minimo, maximo = intervalo
    if minimo > maximo:
        raise ValueError('O limite mínimo não pode ser maior que o máximo.')
    return df.loc[df[coluna].between(minimo, maximo, inclusive='both')].copy()
