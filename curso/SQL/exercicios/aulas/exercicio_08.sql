-- Lista de transação com o produto "Resgatar Ponei

/*
A tabela de transação não tem as informações da tabela produto, então precisamos puxar uma tabela que contenha essas informações

A tabela de transacao_produto ontem o Id da transação + o Id do produto, mas o ID não tem descrição é apenas númerico, então é preciso verificar na tabela de produtos qual o ID de 'Resgatar o ponei' para depois fazer a seleção.

SELECT * 
FROM produtos 
WHERE DescNomeProduto LIKE '%ponei'
O id do produto é 15
*/

SELECT * 

FROM transacao_produto

WHERE IdProduto = 15