-- Selecione todas transações de 50 pontos (exatos)

SELECT *

FROM transacoes

WHERE QtdePontos = 50;

-- Selecione todos clientes com mais de 500 pontos

SELECT *

FROM clientes

WHERE QtdePontos >= 500;