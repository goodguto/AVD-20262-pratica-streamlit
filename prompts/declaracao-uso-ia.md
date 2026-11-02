# Declaração de uso de IA

- **Nome:** Augusto Malheiros de Souza
- **Turma:** 5A
- **E-mail:** ams10@cesar.school
- **Data dos usos registrados:** 02/11/2026
- **Data de entrega:** preencher
- **Repositório:** https://github.com/goodguto/AVD-20262-pratica-streamlit

O PDF enviado pelo aluno está em `DECLARACAO_IA.pdf`, copiado sem alterações. A reflexão individual foi preenchida pelo aluno. Ainda faltam a confirmação da declaração geral, a data de entrega e uma assinatura válida.

## Ferramentas

- Codex, plano Plus informado pelo aluno. Modelo específico não informado.
- Skill oficial `developing-with-streamlit`, incluída no Streamlit 1.66.1: usada na revisão da interface, API, cache e testes.
- Skill `pdf`: leitura dos materiais e preenchimento técnico desta minuta.
- ChatGPT na EDA anterior, conforme o registro original do notebook. O notebook menciona apoio em código, compreensão dos gráficos, heatmap, Spearman e nas últimas duas etapas da conclusão. Esse uso anterior foi preservado e não foi refeito nesta etapa.

## Registro dos usos

### 1. Estrutura e dados

Pedido: montar o app com os filtros solicitados e manter o tratamento da EDA.

Incorporado: código de carregamento, filtro em cópias, imputação pela mediana e exportação. A EDA original e as observações foram mantidas. O esqueleto partiu do pedido textual; não havia rascunho do aluno.

Verificação pelo Codex: importações, hashes e testes dos dados. Pedido completo em `001-pedido-original.txt`.

### 2. Gráficos e testes

Pedido: implementar o heatmap e os histogramas já solicitados, com tratamento de casos vazios, constantes e ausências.

Incorporado: código dos visuais e dos testes. Foi corrigida a consulta de imagens no AppTest. Não foram escritas novas interpretações dos resultados.

Verificação pelo Codex: 18 testes técnicos e inspeção no navegador. Registros em `relatorio-tecnico.md` e `evidencias/`.

### 3. Interface e Skill do Streamlit

Pedido: usar a Skill oficial se disponível e organizar a interface.

Incorporado: tema com as cores da EDA, largura dos gráficos, textos alternativos, cartões e cache. A Skill oficial do Streamlit foi consultada na revisão.

Verificação pelo Codex: consulta à Skill, API instalada e inspeção visual.

### 4. Git, documentação e declaração

Pedido: organizar os commits por aula, esperar 40 e 23 minutos reais, encurtar comentários e preparar esta declaração.

Incorporado: configuração técnica, instruções no README, registros de uso, operação do Git, comentários mais curtos e esta minuta. Os intervalos foram esperas reais, não tempo de desenvolvimento. A reflexão e a assinatura não foram produzidas pela IA.

Verificação pelo Codex: hashes remotos, checkout e revisão do PDF. Pedidos em `002-pedido-commits.txt`, `003-pedido-estilo-tempo.txt` e `004-pedido-declaracao.txt`.

## Partes com apoio de IA

- `app.py`, `dados.py`, `src/data_loader.py` e preparação/exportação dos dados.
- Dashboard 1, configuração visual e testes.
- Dashboard 2: somente estrutura da aba e avisos; sem KPIs, fórmulas ou visuais escolhidos pela IA.
- README, registros técnicos, Git e esta minuta. Deploy não realizado.

Os trechos de código têm marcações `# [IA] Codex - finalidade`. A conferência e a compreensão individuais do aluno ainda precisam ser confirmadas por ele. Os arquivos de prompts e os resumos não equivalem à transcrição completa da conversa; o PDF usa registro por usos da Opção B.

## Reflexão individual

A reflexão escrita pelo aluno consta no PDF enviado. Antes da entrega, conferir a referência à troca de cores do heatmap: o código atual ainda usa a paleta coolwarm.

## Assinatura

Assinatura: ____________________________________

Data: ____________________
