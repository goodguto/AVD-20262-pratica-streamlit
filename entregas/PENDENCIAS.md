# Pendências do aluno

Este arquivo é um controle técnico produzido com auxílio de IA. Não constitui justificativa de métricas, interpretação, rascunho ou declaração pessoal.

No repositório existente, `entregas/justificativa-metricas.md` passou a conter o template oficial da professora após a atualização do modelo. Ele está incompleto, com campos vazios e dois títulos `<nome>`. Preencha-o com suas decisões, sem sugestões da IA:

1. Público-alvo e a decisão que o dashboard pretende apoiar.
2. De 3 a 5 métricas escolhidas e justificadas por você. Para cada uma: nome, variável(s), o que mede, por que escolheu, público-alvo, decisão apoiada e o que comunica. Para permitir a implementação: fórmula, unidade, agrupamento, denominador quando houver, tratamento de ausentes e de divisão por zero.
3. Unidade de análise e forma de agregação: as linhas não são jogadores únicos. Defina como tratar participações repetidas quando sua métrica exigir agregação.
4. Três visualizações complementares: tipo, variáveis/eixos, agregação e relação com os indicadores. O roteiro consultado espera Altair no Dashboard 2; a IA ainda não selecionou nem implementou esses visuais.
5. Widgets e filtros: campos, valores iniciais, regras de combinação e indicadores/gráficos afetados. Defina-os antes do rascunho do Dashboard 2.

Também faltam:

- `rascunho-dashboard1.jpg` ou `.png`: não encontrado e não elaborado pela IA. O `prof_rascunho_dashboard1.png` do modelo é exemplo da professora e não substitui seu desenho.
- `rascunho-dashboard2.jpg` ou `.png`: não encontrado; elaborar após definir as decisões anteriores.
- Revisar `prompts/DECLARACAO_IA.pdf`, já enviado pelo aluno com a reflexão preenchida. Marcar a declaração geral, preencher a data de entrega e colocar assinatura válida: o campo atual contém "Não consegui fazer". Conferir o modelo, se disponível, e os registros completos dos usos de IA.
- Conferir a consistência da reflexão: o texto menciona troca das cores do heatmap, mas `app.py` ainda usa `cmap='coolwarm'`. Revisar também a paginação e as marcações que ficaram fora das caixas no PDF enviado.
- Link real do app no README e teste publicado em janela anônima. Repositório próprio identificado: https://github.com/goodguto/AVD-20262-pratica-streamlit ; organização dos commits por aula registrada em `prompts/ORGANIZACAO_COMMITS.md`.
- Conferência do enunciado separado: não foi anexado um arquivo com esse nome. Foram consultados as aulas, a declaração e o roteiro público do repositório indicado na Aula 21. Se houver regras adicionais no Classroom, forneça o enunciado para conferência.

A implementação técnica do Dashboard 1 segue o layout textual solicitado nesta conversa. Não se afirma que ele foi gerado a partir de um desenho anterior. O roteiro pede o rascunho antes do código: essa etapa não pode ser reconstruída como se tivesse sido feita antes.
