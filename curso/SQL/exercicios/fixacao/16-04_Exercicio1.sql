/*  Clientes engajados em múltiplas plataformas
Dificuldade: iniciante
Selecione o IdCliente, QtdePontos e a DtCriacao de todos os clientes que estão cadastrados simultaneamente no YouTube, no Instagram e no BlueSky.

Ordene o resultado pelos clientes com mais pontos primeiro. Traga apenas os 15 primeiros.

Mudei o where devido aos dados do banco, pois não temos pessoas cadastradas simultaneamente nos canais sugerido.


*/

SELECT IdCliente,
       QtdePontos, 
       DtCriacao

FROM clientes

WHERE FlEmail = 1 AND FlTwitch = 1 

ORDER BY QtdePontos DESC

LIMIT 15



