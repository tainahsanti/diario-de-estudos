-- Selecione todos os clientes com e-mail cadastrado

-- Código escrito: Seleciona todas as colunas, da tabela cliente, onde as linhas sejam 1 = e-mail cadastrado

SELECT *

FROM clientes

-- WHERE FlEmail = 1

-- outras opções
-- WHERE FlEmail != 0
WHERE FlEmail <> 0

