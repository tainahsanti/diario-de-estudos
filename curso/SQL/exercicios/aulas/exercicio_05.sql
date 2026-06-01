-- Lista de produtos com nome que começa com "Venda de"
SELECT IdProduto, DescNomeProduto

FROM produtos

-- Adicionar o % pra mostrar que pode puxar qualquer coisa que começa com 'Venda de'
WHERE DescNomeProduto LIKE 'Venda de%' 

