-- Selecione produtos que contêm 'churn' no nome

SELECT * 

FROM produtos

/* Maneira Iniciante
WHERE DescProduto = 'Churn_10pp'
OR DescProduto = 'Churn_2pp'
OR DescProduto = 'Churn_5pp'
*/

-- Outra forma melhor que a forma acima.
-- WHERE DescProduto IN ('Churn_10pp', 'Churn_2pp', 'Churn_5pp')

-- Valores "infinitos" / genericos
-- WHERE DescProduto LIKE '%pp'
-- WHERE DescProduto LIKE '%botas%'-- O porcentual é um coringa, ela começa com Churn coringa restante. Se fosse o final, começaria com %
-- WHERE DescProduto LIKE 'Churn%'

-- Melhor forma de escrever essa query, indo pela descrição do produto. Mas precisa entender como está a organização do banco de dados

WHERE DescCateogriaProduto = 'churn_model'