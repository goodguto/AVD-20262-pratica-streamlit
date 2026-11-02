# Relatório técnico — 02/11/2026

Produzido com apoio de IA (Codex). Relata implementação e execução técnica, sem interpretar resultados do dataset.

## Atualização — Dashboard 2 em 02/11/2026

Esta seção atualiza o estado das pendências nas seções históricas abaixo.

- O aluno confirmou público (torcedores), cálculos (total de gols, total de assistências e idade média por jogador), gráficos (barras, dispersão e histograma) e filtros (nacionalidade, posição e idade). Sua justificativa foi transcrita em `entregas/justificativa-metricas.md`, sem criar interpretações dos resultados.
- `indicadores.py` aplica os filtros a uma cópia dos dados, soma gols/assistências e calcula a média das idades agrupadas por nome. Participações repetidas não aumentam o peso de um jogador na idade média. Recortes vazios e valores inteiramente ausentes aparecem como indisponíveis.
- Os três gráficos foram implementados em Altair 6.3.0, agora declarado diretamente em `requirements.txt`. As barras incluem todos os nomes do recorte em área com rolagem; a dispersão tem um ponto por nome e o histograma usa um registro por nome.
- Dois layouts técnicos com indicação de IA e data foram produzidos. O do Dashboard 1 documenta código anterior; não representa uma etapa de desenho anterior à implementação. O do Dashboard 2 foi preparado após as escolhas do aluno, antes da nova função de interface.
- Suíte completa: **27 testes aprovados em 42,277 segundos**, sem testes ignorados. Inclui os 18 testes anteriores e nove testes novos de agregação, peso igual de idade, filtros combinados, ausência de dados e widgets do Dashboard 2. Execução em uma cópia integral do projeto em `work/`, com o dado bruto presente para o teste de preparação. Log: `evidencias/testes-dashboard2.txt`.
- `pip check`: **No broken requirements found**. Mesmo ambiente Python 3.12 descrito abaixo, com Altair 6.3.0.
- O AppTest confirmou os três elementos Vega-Lite e os valores dos indicadores; ele não verifica pixels nem a interação gráfica renderizada no navegador. A inspeção visual anterior do Dashboard 1 continua sendo apenas a evidência histórica descrita abaixo.
- O controle do navegador terminou durante a tentativa de autenticação, porque a ferramenta não conseguiu confirmar o endereço da janela do Chrome. **Publicação e teste em janela anônima não executados**. Não existe URL pública confirmada. Instruções em `PUBLICAR.md`.
- A declaração, a reflexão, os notebooks originais e os CSVs foram preservados. A parte 4 foi excluída pelo aluno. O novo uso de IA foi registrado em `prompts/006-dashboard2-e-publicacao.txt`.

## Entregue

- `app.py`: configuração inicial, tema, barra lateral, seletor com as 11 quantitativas da EDA, variável de filtro, slider inclusivo, duas abas e contagens operacionais com `st.metric`.
- Dashboard 1: correlação de Spearman e um histograma com KDE por variável selecionada. Atualização com o filtro, exclusão de identificadores/booleanos da correlação, mascaramento de pares indefinidos e mensagens nos casos de borda. KDE desativada para constantes.
- Dashboard 2: aba com estrutura e lista de decisões pendentes. Nenhuma métrica de futebol, fórmula de KPI, visual complementar, filtro analítico, justificativa ou interpretação foi escolhido pela IA.
- `dados.py`, `scripts/preparar_dados.py`, `notebooks/eda-com-exportacao.ipynb`: validação, exportação e reprodução da imputação já definida no notebook.
- `data/raw/` e `data/clean/`: cópias separadas. O app somente lê o tratado. SHA-256 e fonte registrados em `data/proveniencia.json`.
- `requirements.txt`, `.streamlit/config.toml`, `.gitignore`, `README.md`, testes, pendências, registro técnico de IA e referências.
- `notebooks/eda.ipynb`: cópia intacta do notebook fornecido. PDFs originais também preservados em `referencias/`.
- Evidências do navegador: `evidencias/desktop.png`, `evidencias/mobile.png` e `evidencias/histogramas.png`. São capturas posteriores da implementação; **não são os rascunhos acadêmicos**.

## Ambiente efetivamente executado

Windows, Python 3.12.14, ambiente virtual isolado em `work/` fora do projeto entregue. Bibliotecas importadas: Streamlit 1.66.1, pandas 3.1.0, Matplotlib 3.11.2, Seaborn 0.13.2 e SciPy 1.18.1. As versões diretas coincidem com `requirements.txt`.

Na integração, o `.venv` preexistente do aluno foi inspecionado: Python 3.15.1 e pandas 3.1.0, sem as demais bibliotecas do app. Esse ambiente foi preservado. A suíte no repositório real usou o ambiente isolado de Python 3.12.14, com **18 testes aprovados em 33,331 segundos**. O README orienta criar um ambiente separado com Python 3.12 para não sobrescrever o existente.

`python -m pip check`: **No broken requirements found**. A instalação do ambiente resolveu e instalou as dependências do projeto. Não foram testados outros sistemas ou versões do Python.

## Testes automatizados

Comando: `python -m unittest discover -s tests -v`.

Resultado: **18 testes, OK; sem falhas** na entrega técnica inicial. A suíte também foi executada na integração ao repositório existente; o log correspondente está em `evidencias/testes-repositorio.txt`.

| Grupo | Verificação executada | Resultado |
| --- | --- | --- |
| Dados | 13.397 linhas, 21 colunas, identificadores/booleanos excluídos das quantitativas | Passou |
| Preparação | Imputação reproduzida, igualdade com o tratado e original sem mutação | Passou |
| Filtro | Limites inclusivos, valores esperados e alteração do recorte sem alterar a base | Passou |
| Filtro vazio | Recorte sem observações e matriz vazia | Passou |
| Validação | Coluna de filtro inadequada e intervalo invertido | Passou |
| Correlação | Spearman conhecido em fixture, ausentes, constantes e identificação numérica excluída | Passou |
| Seleções | Nenhuma variável e menos de três pares | Passou |
| Integridade | Hash do CSV tratado coincide com o manifesto | Passou |
| Sintaxe | AST dos arquivos Python do projeto, excluindo Git, ambiente virtual e caches | Passou |
| Credenciais | Busca de arquivos .env/secrets.toml/kaggle.json e padrões de chaves privadas, tokens GitHub/OpenAI e IDs de acesso AWS | Nenhum padrão encontrado |
| Interface | Duas abas, aviso de pendência e 12 imagens geradas: heatmap + 11 histogramas | Passou |
| Interface | 0, 1 e 2 variáveis, com quantidade de gráficos adequada | Passou |
| Interface | Slider 30–60 minutos, contagem conferida com pandas e retorno ao intervalo completo | Passou |
| Interface | Troca da variável e intervalo 100,01–100,01 sem observações | Passou |
| Interface | Histograma constante com KDE desativada | Passou |
| Interface | Falta de arquivo mostra erro e mantém a segunda aba | Passou |
| Interface | Variável de filtro constante ou inteiramente ausente, sem slider inválido | Passou |
| Interface | Histograma sem valores disponíveis | Passou |

Os testes com ausência total/constantes usam fixtures explícitas; não alteram o CSV entregue. A busca automatizada de credenciais cobre os padrões descritos, não constitui auditoria completa de todos os metadados ou dados pessoais dos anexos originais. Os nomes de jogadores pertencem ao dataset público solicitado.

Verificações adicionais: o código da célula de `eda-com-exportacao.ipynb` foi executado por Python a partir de `notebooks/`, sem Jupyter. A reexportação preservou o hash do CSV tratado. O hash da cópia de `eda.ipynb` também foi comparado com o anexo e permaneceu idêntico. O log da suíte e as versões constam em `evidencias/`.

## Correções e observações da execução

A primeira rodada terminou com cinco falhas nos próprios testes, que procuravam imagens pelo identificador interno antigo `imgs`. A inspeção da versão instalada confirmou que a API do AppTest as expõe como `image`. A consulta dos testes foi corrigida; a segunda execução completa passou. Não houve remoção de verificações para obter esse resultado.

No ambiente restrito, Matplotlib inicialmente não pôde gravar seu cache padrão de usuário e usou uma pasta temporária. Na execução final dos testes foi definido `MPLCONFIGDIR` para uma pasta gravável em `work/`. Isso não exigiu mudar os gráficos nem escrever configuração no perfil do usuário. O AppTest emite avisos esperados sobre ausência de runtime/contexto durante inicialização e limpeza do cache; não houve exceções do app na execução final.

## Verificação no navegador local

Servidor iniciado com `streamlit run app.py --server.address 127.0.0.1 --server.port 8501 --server.headless true`. Interface aberta no navegador integrado.

- Confirmados o carregamento da interface, o heatmap e os histogramas no navegador.
- Clicada a aba de indicadores e conferida a lista de pendências; retorno à aba do laboratório.
- Slider alterado de 1–90 para 2–90 minutos pelo teclado: a contagem passou de 13.397 para 13.312 e os textos de quantidade dos histogramas atualizaram. Intervalo completo restaurado.
- Layout revisado em 1366 × 900 e 390 × 844: cartões empilham na tela estreita, barra lateral recolhe e abas têm rolagem própria. Na tela de 390 pixels, `document.body.scrollWidth` foi 390. O mapa de calor completo tem muitos rótulos; em tela estreita há botão de tela cheia e tabela de coeficientes.

Esta revisão não equivale a testes em todos os dispositivos, e AppTest não verifica pixels. Capturas e inspeção do navegador complementaram os testes de lógica.

## Não executado / não entregue por depender do aluno

- Publicação no Streamlit: não realizada. O repositório GitHub já existente foi identificado e a integração foi organizada em três commits, com a identidade Git já configurada do aluno. Não foram usados commits com datas anteriores nem reescrita do histórico da professora. Consulte `prompts/ORGANIZACAO_COMMITS.md` e o histórico do Git.
- Teste de versão publicada em janela anônima: **NÃO EXECUTADO**, registrado separadamente em `entregas/TESTE_PUBLICADO.md`.
- Execução integral da EDA original: não realizada, pois há Colab e trechos remanescentes incompatíveis com este dataset. O arquivo original não foi corrigido nem reexecutado.
- Fórmulas, KPIs, filtros e três visuais do Dashboard 2: aguardam decisões acadêmicas documentadas.
- Dois rascunhos do aluno, preenchimento do template de justificativa, declaração pessoal/reflexão/assinatura e eventual enunciado adicional: pendentes em `entregas/PENDENCIAS.md`.

## Integração ao repositório do aluno

Repositório: https://github.com/goodguto/AVD-20262-pratica-streamlit . Foram incorporadas por avanço direto as quatro atualizações oficiais do modelo que faltavam no clone local. O template de justificativas continua vazio; o rascunho da professora continua identificado como exemplo.

Os arquivos locais previamente sem commit `notebooks/eda-original-augusto.ipynb` e `data/clean/fifa2026_player_performance.csv` foram preservados e versionados. O segundo contém 23 colunas: suas 21 colunas de base coincidem integralmente com o CSV usado no app; as duas categorias derivadas permanecem no arquivo original local. O exemplo Heart Disease foi preservado em `data/exemplos/heart-disease.csv`.

O carregamento foi adaptado ao módulo `src/data_loader.py` do modelo. O teste de sintaxe e a busca de credenciais passaram a excluir `.git`, `.venv` e caches, mantendo a inspeção dos arquivos do projeto. `.gitattributes` preserva os bytes dos CSVs validados e dos notebooks originais, evitando quebra dos hashes por conversão de finais de linha em outro checkout.

O esqueleto da Aula 21 foi executado antes do primeiro commit: 11 opções no seletor, slider 30–60, contagem conferida com pandas e nenhum gráfico ainda renderizado. A implementação completa e seus testes entraram no commit da Aula 22. A etapa técnica da Aula 23 consolida a documentação e a preparação para deploy; não declara o projeto acadêmico concluído.

## Uso de IA

Todo código novo ou modificado nesta sessão contém marcações `# [IA] Codex – finalidade`. A interface, operações técnicas, testes, configuração e documentação técnica precisam ser declarados. A Skill oficial `developing-with-streamlit` do Streamlit 1.66.1 foi usada na revisão; a Skill `pdf` auxiliou na leitura. O pedido original e o registro factual estão em `prompts/`. O aluno deve completar sua própria declaração; este relatório não a substitui.
