# Justificativa das métricas - Dashboard 2

## Decisões do aluno

- Público-alvo: torcedores.
- Métricas: total de gols, total de assistências e idade média por jogador.
- Filtros: nacionalidade, posição e intervalo de idade.
- Visuais: barras de gols por jogador, dispersão de gols × assistências e histograma de idades.

Justificativa enviada pelo aluno para as três escolhas:

> pois é o que a maioria dos torcedores querem olhar. eles olham essas 3 primeiras estatisticas antes de todo resto

As escolhas e a justificativa acima foram fornecidas pelo aluno nesta conversa. O apoio de IA nesta etapa foi o registro dessas decisões e sua implementação técnica, sem criar uma justificativa adicional.

## Total de gols

- Variável: `goals`.
- O que mede: soma dos gols nas observações que passaram pelos filtros.
- Por que foi escolhida: justificativa conjunta do aluno, transcrita acima.
- Público-alvo: torcedores.
- Uso declarado: consultar essas estatísticas antes das demais, conforme a justificativa fornecida.
- O que comunica: quantidade total de gols registrada no recorte.
- Fórmula: soma de `goals` no recorte. Não se soma apenas um valor por jogador: as observações representam participações diferentes.

## Total de assistências

- Variável: `assists`.
- O que mede: soma das assistências nas observações filtradas.
- Por que foi escolhida: justificativa conjunta do aluno, transcrita acima.
- Público-alvo: torcedores.
- Uso declarado: consultar essas estatísticas antes das demais.
- O que comunica: quantidade total de assistências registrada no recorte.
- Fórmula: soma de `assists` no recorte.

## Idade média por jogador

- Variáveis: `age` e `player_name`.
- O que mede: idade média com o mesmo peso para cada jogador presente no recorte.
- Por que foi escolhida: justificativa conjunta do aluno, transcrita acima.
- Público-alvo: torcedores.
- Uso declarado: consultar essas estatísticas antes das demais.
- O que comunica: média das idades dos jogadores representados no recorte.
- Fórmula: agrupar por `player_name`, obter a idade média de cada nome e calcular a média entre esses nomes. No CSV fornecido, cada nome tem uma única idade. Assim, participações repetidas não dão peso maior a um jogador na média.

## Unidade de análise e gráficos

Os totais de gols e assistências usam todas as observações filtradas. A tabela para os gráficos agrupa por nome, somando gols e assistências e calculando a idade média de cada nome. O agrupamento usa `player_name`, pois o arquivo não fornece um identificador próprio de jogador; não se presume que `match_id` seja esse identificador.

- Barras: um total de gols para cada jogador do recorte, sem limitar a um ranking parcial.
- Dispersão: um ponto por jogador, com total de gols no eixo X e de assistências no eixo Y.
- Histograma: idades dos jogadores, com um registro por nome.

Os três filtros afetam os três indicadores e os três gráficos. Sem observações, o app mostra os indicadores como indisponíveis e uma mensagem. Valores ausentes são ignorados nos cálculos; uma coluna inteiramente ausente não vira zero. Não há divisão por zero nas métricas escolhidas.

Não foram produzidas interpretações ou conclusões sobre os resultados.
