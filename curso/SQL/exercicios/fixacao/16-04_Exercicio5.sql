/*Perfil completo do cliente com flags e categoria
Dificuldade: desafiador
Monte uma query que traga IdCliente, QtdePontos e DtCriacao da tabela clientes, e adicione três colunas calculadas:

1. NivelCliente: CASE WHEN com faixas de pontos à sua escolha (mínimo 3 faixas + ELSE)
2. flMultiPlataforma: valor 1 se o cliente estiver em pelo menos 2 plataformas (Email, Twitch, YouTube, BlueSky ou Instagram), 0 caso contrário
3. MesIngresso: o mês de criação da conta extraído de DtCriacao

Filtre apenas clientes com mais de 500 pontos e ordene por pontos de forma decrescente.

CASE WHEN
*/

SELECT IdCliente, 
       QtdePontos,
       DtCriacao,

       CASE
            WHEN QtdePontos <= 500 THEN 'Junior'
            WHEN QtdePontos <= 2500 THEN 'Pleno'
            WHEN QtdePontos <= 5000 THEN 'Pleno Senior' 
            ELSE 'Senior'
       END AS Nivel,

       CASE
       -- Como eu fiz:
            WHEN FlBlueSky = 1 AND FlEmail = 1 THEN 1
            WHEN FlBlueSky = 1 AND FlInstagram = 1 THEN 1
            WHEN FlBlueSky = 1 AND FlTwitch = 1 THEN 1
            WHEN FlBlueSky = 1 AND FlYouTube = 1 THEN 1            
            WHEN FlEmail = 1 AND FlInstagram = 1 THEN 1
            WHEN FlEmail = 1 AND FlTwitch = 1 THEN 1
            WHEN FlEmail = 1 AND FlYouTube = 1 THEN 1
            WHEN FlInstagram = 1 AND FlTwitch = 1 THEN 1
            WHEN FlInstagram = 1 AND FlYouTube = 1 THEN 1            
            WHEN FlYouTube = 1 AND FlTwitch = 1 THEN 1
            ELSE 0
        -- Como poderia ser:
       -- WHEN (FlBlueSky + FlEmail + FlInstagram + FlTwitch + FlYouTube) >= 2 THEN 1

       END AS flMultiPlataforma, -- Verificar virgula sempre

       strftime('%m', datetime(substr(DtCriacao, 1, 19))) AS MesIngresso

FROM clientes

WHERE QtdePontos > 500

ORDER BY QtdePontos DESC