# Exercícios SQL - Curso Teo Me Why

O curso é dividido em **5 rounds** de exercícios. Atualmente, completei o **Round 1**.

---

## Round 1 - Lista de Consultas

| # | Exercício | Solução SQL |
|---|-----------|-------------|
| 1 | Transações com apenas 1 ponto | `WHERE pontos = 1` |
| 2 | Pedidos realizados no fim de semana | strftime` * |
| 3 | Clientes com 0 pontos | `WHERE pontos = 0` |
| 4 | Clientes com 100 a 200 pontos | `WHERE pontos BETWEEN 100 AND 200` |
| 5 | Produtos com nome começando com "Venda de" | `WHERE nome LIKE 'Venda de%'` |
| 6 | Produtos com nome terminando com "Lover" | `WHERE nome LIKE '%Lover'` |
| 7 | Produtos que são "chapéu" | `LIKE '%Chapéu%'` |
| 8 | Transações com produto "Resgatar Ponei" | `WHERE IdProduto = 15` |
| 9 | Transações com classificação de pontos | `CASE WHEN ... END` |

