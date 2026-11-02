# FIFA 2026 — Streamlit

Aplicação da disciplina Análise e Visualização de Dados, baseada na EDA do FIFA 2026 Player Performance.

## Rodar

Use Python 3.12. Se já tiver um ambiente de outra versão, crie um separado.

```powershell
# [IA] Codex – Instalação e execução.
py -3.12 -m venv .venv-avd
.venv-avd\Scripts\python -m pip install -r requirements.txt
.venv-avd\Scripts\python -m streamlit run app.py
```

## Dados

Fonte: [Kaggle — FIFA 2026 Player Performance](https://www.kaggle.com/datasets/debayank2024/fifa-2026-player-performance), versão 2.

O app lê `data/clean/dataset.csv`. As ausências de `market_value_eur_m`, `pass_accuracy_pct` e `distance_covered_km` foram preenchidas pela mediana, como na EDA. Os outliers foram mantidos. Cada linha é uma observação de desempenho, não um jogador único.

A EDA original está em `notebooks/eda.ipynb`. Para refazer a exportação, coloque o CSV original em `data/raw/` e execute `scripts/preparar_dados.py`. O dado bruto não é versionado.

## Dashboards

- Dashboard 1: seleção de variáveis, filtro de intervalo, correlação de Spearman e histogramas.
- Dashboard 2: estrutura pronta. As métricas, os três visuais e os filtros aguardam as decisões em `entregas/justificativa-metricas.md`.

`app.py` organiza a interface. `dados.py` valida e filtra os dados. `src/data_loader.py` faz o carregamento. Os filtros trabalham em uma cópia da base.

## Testes

```powershell
# [IA] Codex – Testes técnicos.
.venv-avd\Scripts\python -m unittest discover -s tests -v
.venv-avd\Scripts\python -m pip check
```

Resultados em `relatorio-tecnico.md` e `evidencias/`.

## Publicação e entrega

Repositório: [goodguto/AVD-20262-pratica-streamlit](https://github.com/goodguto/AVD-20262-pratica-streamlit).

No Streamlit Community Cloud, selecione esse repositório, a branch `main`, o arquivo `app.py` e Python 3.12. Após publicar, teste em janela anônima e registre o resultado em `entregas/TESTE_PUBLICADO.md`.

Link do app: pendente. Também faltam os dois rascunhos do aluno, as decisões do Dashboard 2 e a declaração assinada. Veja `entregas/PENDENCIAS.md`.

## Uso de IA

Houve apoio de Codex no código, na interface, nos testes e na documentação técnica. Os trechos estão marcados com `# [IA] Codex – finalidade`. A Skill oficial `developing-with-streamlit`, do Streamlit 1.66.1, foi usada na revisão. Os pedidos e registros estão em `prompts/`; a declaração pessoal deve ser preenchida pelo aluno.
