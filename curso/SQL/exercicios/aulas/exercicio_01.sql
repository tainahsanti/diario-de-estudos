-- Lista transações com apenas 1 ponto

/* SELECT * 

FROM transacoes

WHERE QtdePontos = 1; */

-- Garantir que está pegando apenas as transações com 1 ponto, seleciona a coluna IdTransação + QtdePontos


SELECT IdTransacao, QtdePontos
FROM transacoes
WHERE QtdePontos = 1;