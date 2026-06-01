-- Lista de clientes com zero pontos

SELECT IdCliente, DtCriacao, QtdePontos

FROM CLIENTES

WHERE QtdePontos = 0