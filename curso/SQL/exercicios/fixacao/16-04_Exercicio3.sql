/*
Classificação de pontos com CASE WHEN
Dificuldade: médio
Selecione IdCliente e QtdePontos da tabela de clientes. Crie uma coluna chamada Categoria usando CASE WHEN com as seguintes regras:

— Até 200 pontos → 'Inativo'
— De 201 até 1000 → 'Iniciante'
— De 1001 até 5000 → 'Intermediário'
— Acima de 5000 → 'Avançado'

Ordene do mais pontos para o menos.

CASE WHEN
THEN
ELSE
END AS
ORDER BY DESC

*/

SELECT IdCliente, 
       QtdePontos,

       CASE
            WHEN QtdePontos <= 200 THEN 'Inativo'
            WHEN QtdePontos <= 1000 THEN 'Iniciante'
            WHEN QtdePontos <= 5000 THEN 'Intermédiario'
            ELSE 'Avançado'
       END AS Categoria

FROM clientes

ORDER BY QtdePontos DESC