-- Lista de produtos com nome que termina com "Lover"
SELECT * 

FROM produtos

-- Adicionar o % pra mostrar que pode puxar qualquer coisa que termina com 'Lover'
WHERE DescNomeProduto LIKE '%Lover'