# [IA] Codex – Exportar dados.
from pathlib import Path
import hashlib
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pandas as pd
from dados import CSV_ORIGINAL, CSV_TRATADO, SHA_ORIGINAL, IMPUTAR, RAIZ, tratar_dados, validar_dados


# [IA] Codex – Validar o CSV.
def preparar():
    if not CSV_ORIGINAL.exists():
        raise FileNotFoundError('Coloque o CSV da versão 2 do Kaggle em data/raw/. Consulte data/README.md.')
    sha_original = hashlib.sha256(CSV_ORIGINAL.read_bytes()).hexdigest()
    if sha_original != SHA_ORIGINAL:
        raise ValueError('CSV original diferente da versão validada nesta implementação.')
    original = pd.read_csv(CSV_ORIGINAL)
    validar_dados(original)
    esperadas = {'market_value_eur_m': 270, 'pass_accuracy_pct': 807, 'distance_covered_km': 679}
    if original[IMPUTAR].isna().sum().to_dict() != esperadas:
        raise ValueError('Contagens de ausências incompatíveis com a EDA.')
    tratado = tratar_dados(original)
    CSV_TRATADO.parent.mkdir(parents=True, exist_ok=True)
    tratado.to_csv(CSV_TRATADO, index=False, lineterminator='\n')
    registro = {
        'fonte': 'https://www.kaggle.com/datasets/debayank2024/fifa-2026-player-performance',
        'versao_kaggle': 2, 'obtido_em': '2026-11-02',
        'arquivo_original': CSV_ORIGINAL.name,
        'sha256_original': sha_original,
        'sha256_tratado': hashlib.sha256(CSV_TRATADO.read_bytes()).hexdigest(),
        'linhas': len(original), 'colunas': len(original.columns),
        'ausencias_antes': esperadas,
        'medianas': original[IMPUTAR].median().to_dict(),
        'tratamento': 'Mediana da base completa; outliers e linhas preservados; sem agregação.',
        'compatibilidade_eda': 'Dimensões, colunas, primeiras cinco linhas e ausências coincidem; o CSV original da sessão Colab não foi fornecido.',
    }
    (RAIZ / 'data/proveniencia.json').write_text(json.dumps(registro, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Exportadas {len(tratado)} observações para data/clean/dataset.csv.')


# [IA] Codex – Executar preparação.
if __name__ == '__main__':
    preparar()
