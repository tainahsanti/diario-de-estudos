/* Produtos da categoria com nome por extenso
Dificuldade: médio
Selecione IdProduto, DescProduto e DescCateogriaProduto da tabela de produtos. Crie uma coluna adicional chamada TipoConteudo usando CASE WHEN para traduzir a categoria:

— 'rpg' → 'RPG'
— 'streaming' → 'Streaming'
— Qualquer outra → 'Outros'

Filtre o resultado para trazer apenas os produtos que não sejam da categoria 'outros' (use a coluna original, não o alias). Ordene pelo nome do produto.

CASE WHEN
WHERE
!=
ORDER BY

*/

SELECT IdProduto, 
       DescProduto,
       DescCateogriaProduto,

       CASE
            WHEN DescCateogriaProduto = 'rpg' THEN 'RPG'
            WHEN DescCateogriaProduto = 'streamelements' THEN 'Streaming'
            ELSE 'Outros'
       END as TipoConteudo

FROM produtos
-- Como eu fiz:
WHERE DescCateogriaProduto = 'rpg' OR DescCateogriaProduto = 'streamelements'

-- Como poderia ter feito
-- WHERE DescCateogriaProduto IN ('rpg', 'streamelements')

/*
OR	várias condições separadas
IN	pertence a um conjunto*/

ORDER BY DescProduto