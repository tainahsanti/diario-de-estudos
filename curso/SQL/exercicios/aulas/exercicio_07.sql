-- Lista de produtos que são "chápeu"
SELECT * 

FROM produtos

-- WHERE DescCategoriaProduto = 'chapeu' OU
-- "Contém chapéu"

-- Se não quisesse os produtos com 'Chapéu'?
-- WHERE IdProduto NOT LIKE '%Chapéu%'

WHERE IdProduto LIKE '%Chapéu%'

