# Mapeamento técnico do notebook fornecido

Registro técnico, sem novas interpretações. Células numeradas a partir de zero.

- **Célula 37:** 11 quantitativas: age, market_value_eur_m, minutes_played, goals, assists, shots_on_target, pass_accuracy_pct, tackles, distance_covered_km, match_rating e fouls_committed.
- **Célula 37:** qualitativas: nationality, club, position, season, competition, yellow_card, red_card e injured_flag. player_name é identificação nominal; match_id é identificador numérico, excluído das medidas.
- **Célula 5:** cores lightgray, #e9d4d0, #2d223a e tab:red. Correlações usam coolwarm (células 103/105), tabelas de contingência usam magma.
- **Células 70–72:** imputação pela mediana nas três colunas com ausências. Células 67 e 76 registram a manutenção dos outliers.
- **Gráficos existentes:** histogramas com KDE (42), QQ-plot, ECDF de valor de mercado (52), histograma com média/mediana (55), boxplots e violinos (57), outliers por IQR (64), KDE antes/depois (86), barras de frequência (93), heatmaps Pearson/Spearman/Kendall (103) e Spearman triangular (105), dispersão com regressão (109), boxplot por posição (113), contingência posição/cartão (121), barras por faixa etária (126), contingência faixa/nota (133), jointplot (137) e correlograma PairGrid (142–144).
- **Dashboard 1:** usa os histogramas e o heatmap solicitados pelo aluno. Spearman acompanha o heatmap da célula 105 e a função da célula 143. O mínimo de três pares, a exclusão de constantes e as mensagens são proteções técnicas adicionadas ao app; não são novas decisões analíticas do aluno.
- **Limitações já registradas:** as células 9, 128, 150 e 154 questionam confiabilidade, citam inconsistências de informações e possível simulação. Não se validaram afirmações futebolísticas do notebook nem se corrigiram idades, gols ou valores por conhecimento externo.
- **Inconsistências de execução:** célula 12 mostra (303, 14), enquanto info/describe e o texto mostram 13.397 × 21. A célula 23 tem código de contagem e saída percentual. A célula 68 referencia ca/thal, a 74 chol, remanescentes do exemplo de cardiologia; a 114 depende de variáveis não definidas nas células anteriores fornecidas. Existem ainda textos do exemplo Heart Disease. Não é seguro executar o notebook inteiro para preparar estes dados.
- **Origem e unidade:** o CSV inclui competições de clubes e season. Portanto o app usa a descrição neutra “observações de desempenho”, sem rotular todas as linhas como partidas da Copa do Mundo. Não são 13.397 jogadores únicos.

O original permanece intacto. A preparação técnica foi isolada em script e notebook novos, com comentários de IA, sem novas análises ou conclusões.
