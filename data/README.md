# Dados e proveniência

Fonte solicitada: https://www.kaggle.com/datasets/debayank2024/fifa-2026-player-performance — versão 2, baixada em 02/11/2026, sem autenticação, pela API pública do Kaggle.

O ZIP contém `fifa2026_player_performance_clean.csv`. Apesar de `clean` no nome, há ausências, como no notebook. O original fica em `raw/` e nunca é sobrescrito pelo app. Para reproduzir em outro computador, baixe a versão 2 e coloque esse arquivo em `data/raw/`; execute `python scripts/preparar_dados.py`.

A conferência encontrou as mesmas dimensões (13.397 × 21), colunas, primeiras cinco observações e contagens de ausências das saídas da EDA. O CSV original usado na sessão Colab não foi anexado; por isso não se afirma identidade binária com aquele arquivo. O SHA-256 do arquivo efetivamente obtido é registrado em `proveniencia.json`.

Tratamento reaplicado antes de filtros: `market_value_eur_m` → mediana 12,57; `pass_accuracy_pct` → 77,3; `distance_covered_km` → 6,31. Foram preenchidas respectivamente 270, 807 e 679 ausências. Nenhuma linha, valor extremo ou identificador foi removido. Não há deduplicação por jogador.

`clean/dataset.csv` contém as 21 colunas de base após imputação. As categorias derivadas `faixa_etaria` e `rating_categoria`, usadas em outras partes da EDA, não são necessárias ao laboratório e não foram acrescentadas nem escolhidas para o Dashboard 2. A transformação de colesterol do exemplo de cardiologia não se aplica.

Não há download durante o uso do dashboard. Versione `clean/dataset.csv` e `proveniencia.json`; `raw/*.csv` está ignorado no Git conforme as aulas.
