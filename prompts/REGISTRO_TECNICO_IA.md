# Registro técnico do apoio de IA — 02/11/2026

Este registro factual foi produzido por **Codex**. Não é a declaração pessoal do aluno, não substitui assinatura ou reflexão e não afirma que o aluno já aceitou, revisou ou compreendeu o código.

## Pedido e limites

O pedido integral está em `001-pedido-original.txt`, copiado do texto fornecido. Foram lidos o notebook, as três aulas e as cinco páginas da declaração de uso de IA antes da implementação. O enunciado separado não foi fornecido; foram consultados o ROTEIRO e os READMEs de entregas/prompts no repositório público indicado na Aula 21. Essas cópias estão em `referencias/`.

O apoio foi limitado à estrutura do projeto, código, sintaxe dos visuais já solicitados, interface, preparação já decidida na EDA e verificações técnicas. Não foram escolhidas ou propostas métricas, público-alvo, filtros ou visuais do Dashboard 2. Não foram escritas interpretações, conclusões, justificativas acadêmicas nem a declaração pessoal do aluno. Os rascunhos não foram simulados.

## Ferramentas e Skills

- Ferramenta principal: **Codex**. Não se presume uma versão comercial ou um plano de assinatura do usuário; registre o que sua interface informar.
- Skill `pdf`: leitura dos PDFs e de suas restrições. Nenhum PDF foi preenchido ou modificado.
- **Skill oficial Streamlit `developing-with-streamlit`, incluída no pacote PyPI `streamlit==1.66.1`: utilizada na revisão técnica posterior à implementação inicial.** Não estava na lista de Skills no início; sua disponibilidade foi confirmada no wheel oficial baixado para a instalação.
- Foram consultados o SKILL.md oficial e as referências de dashboards, exibição de dados, tema, layout e testes. Aplicações: uso de componentes nativos, tema TOML, `width='stretch'`, textos alternativos de gráficos/tabelas, cartões com bordas e limite do cache; conferência de AppTest. Nenhum template de métricas foi adaptado para o Dashboard 2.
- Cópia do SKILL.md consultado: `streamlit-skill/SKILL.md`. Arquivo original de terceiro preservado, sem autoria atribuída ao aluno ou ao Codex. Consulte a documentação oficial: https://docs.streamlit.io/develop/api-reference/cli/skills.
- Consulta à documentação oficial de AppTest e de publicação no Community Cloud.
- Terminal/Python: leitura dos anexos, download público, exportação de dados e execução das verificações que constarem no relatório final.

## Partes com apoio

| Arquivo / parte | Apoio técnico de IA |
| --- | --- |
| app.py | Esqueleto, barra lateral, slider, abas, contagens operacionais, gráficos do Dashboard 1 e mensagens de pendência do Dashboard 2 |
| dados.py | Listas transcritas da EDA, validação, imputação, cópias, filtro e correlação |
| scripts/preparar_dados.py | Exportação e manifesto de proveniência |
| notebooks/eda-com-exportacao.ipynb | Preparação reproduzível separada da EDA |
| .streamlit/config.toml e .gitignore | Tema com cores existentes e exclusões técnicas |
| requirements.txt | Dependências para o ambiente de teste |
| tests/test_app.py | Testes técnicos de dados e de widgets |
| README, relatório, mapeamento, pendências e este registro | Documentação técnica; sem justificativas ou interpretações do aluno |
| notebooks/eda.ipynb e PDFs originais | Apenas cópia, sem alterações |
| data/clean/dataset.csv | Gerado pelo script com o tratamento já existente; não é dado inventado |

## Histórico de alterações desta sessão

1. Leitura dos materiais e confirmação das restrições.
2. Verificação de pasta inicialmente vazia e ausência de justificativas/rascunhos.
3. Cópia intacta do notebook e referências.
4. Download público do CSV, versão 2; conferência de dimensões, esquema, primeiras linhas e ausências com as saídas da EDA.
5. Implementação do laboratório e da aba pendente, com marcações `# [IA] Codex – finalidade`.
6. Separação da preparação reproduzível, manifesto, notebook de exportação e documentação técnica.
7. Consulta à Skill oficial e revisão de acessibilidade visual, cartões e cache.
8. Verificações: registrar os resultados efetivamente executados em `relatorio-tecnico.md`. Correções surgidas dos testes devem constar ali.

Este arquivo é um resumo factual, **não uma transcrição completa da conversa**. Para a Opção A da declaração, o aluno deve exportar/compartilhar a conversa completa; o pedido original e este resumo não dispensam o registro por uso da Opção B. Cabe ao aluno registrar o que aproveitou, modificou ou rejeitou e como verificou, além da reflexão e assinatura.

## Continuação: organização dos commits solicitada pelo aluno

O segundo pedido integral está em `002-pedido-commits.txt`. Foi localizado o repositório já configurado para `goodguto/AVD-20262-pratica-streamlit`, incorporadas as atualizações oficiais da professora e preservados os dois arquivos locais ainda não versionados. Foram preparadas revisões sucessivas para as etapas 21, 22 e preparação técnica da 23, todas com datas atuais e sem reescrever o histórico. Detalhamento em `ORGANIZACAO_COMMITS.md`.

O apoio adicional de Codex inclui adaptação de `src/data_loader.py`, `.gitattributes` para preservar os hashes entre sistemas, inspeção dos testes sem percorrer ambientes/Git, documentação da integração e operação do Git com a identidade configurada pelo aluno. O código adicional contém as marcações de IA. O template oficial de justificativas foi mantido sem preenchimento e nenhuma declaração pessoal foi escrita.
