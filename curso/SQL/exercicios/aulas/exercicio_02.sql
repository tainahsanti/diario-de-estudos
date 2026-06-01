-- Lista de pedidos realizados no fim de semana

SELECT IdTransacao,
       DtCriacao,
       strftime('%w', datetime(substr(DtCriacao, 1, 19))) AS diaSemana -- Substr pega os 19 primeiros elementos da data convertendo para datetime e apartir do datetime está pegando a semana (lendo <-)

FROM transacoes

-- Não é todo banco que deixa usar o AS pra puxar 
WHERE diaSemana IN ('6','0')


/*
0 - Domingo
01 - Segunda
02 - Terça
03 - Quarta
04 - Quinta
05 - Sexta
06 - Sábado
 */