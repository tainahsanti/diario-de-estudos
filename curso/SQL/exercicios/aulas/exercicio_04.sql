-- Lista de clientes com 100 a 200 (inclusive ambos)

SELECT IdCliente, QtdePontos

FROM clientes

WHERE QtdePontos >= 100 AND QtdePontos <= 200

-- WHERE QtdePontos BETWEEN 100 AND 200
