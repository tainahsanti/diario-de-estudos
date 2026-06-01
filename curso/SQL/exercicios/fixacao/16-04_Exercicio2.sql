/*
Ano e mês de cadastro dos clientes mais antigos
Dificuldade: iniciante-médio
Selecione o IdCliente e crie duas colunas novas: uma com o ano de criação da conta e outra com o mês, ambas extraídas da coluna DtCriacao.

Ordene pelo mais antigo primeiro e limite a 20 resultados.

SELECT
strftime
AS
ORDER BY
LIMIT

*/

SELECT IdCliente,
    -- Dificuldade grande usando strftime
    strftime('%m', datetime(substr(DtCriacao, 1, 19))) AS Mes, 
    strftime('%Y', datetime(substr(DtCriacao, 1, 19))) AS Ano
    -- Substr corta a data (porque pode ter milissegundos ou formato estranho)
    -- Datetime transforma em data válida do SQLite
    -- strftime '%m' extrai o mês

FROM clientes

ORDER BY DtCriacao ASC

LIMIT 20