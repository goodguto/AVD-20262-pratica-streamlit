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
- Dashboard 2: total de gols, total de assistências e idade média por jogador; barras de gols por jogador, dispersão de gols × assistências e histograma de idades. Filtros de nacionalidade, posição e idade. As escolhas do aluno estão em `entregas/justificativa-metricas.md`.

`app.py` organiza a interface. `indicadores.py` calcula as métricas do Dashboard 2. `dados.py` valida e filtra os dados. `src/data_loader.py` faz o carregamento. Os filtros trabalham em uma cópia da base.

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

Link do app: [Abrir aplicação publicada](https://avd-20262-pratica-app-zzfzzvjyqwrueqr5bjmtdh.streamlit.app/).

Endereço informado pelo aluno. A conferência independente do app em janela anônima continua pendente de registro em `entregas/TESTE_PUBLICADO.md`. Veja `entregas/PENDENCIAS.md`.

Layouts técnicos produzidos com apoio de IA: [Dashboard 1](entregas/rascunho-dashboard1.png) e [Dashboard 2](entregas/rascunho-dashboard2.png). O desenho do Dashboard 1 foi feito após sua implementação, como indicado na imagem; não comprova um rascunho anterior ao código.

## Uso de IA

Houve apoio de Codex no código, na interface, nos testes e na documentação técnica. Os trechos estão marcados com `# [IA] Codex – finalidade`. A Skill oficial `developing-with-streamlit`, do Streamlit 1.66.1, foi usada na revisão. Os pedidos e registros estão em `prompts/`; a declaração pessoal deve ser preenchida pelo aluno.

Declaração enviada pelo aluno: `prompts/DECLARACAO_IA.pdf`. A reflexão foi preenchida; confirmação geral, data de entrega e assinatura válida continuam pendentes.
