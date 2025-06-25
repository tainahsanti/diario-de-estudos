#📊 5. Verificação de Intervalo
#Peça um número inteiro. Verifique se ele está dentro dos intervalos permitidos:
#Entre -100 e -1
#Ou entre 1 e 100
#Se estiver, exiba uma mensagem.

numero = int(input('Digite um número inteiro: '))

if (-100 <= numero <= -1) or (1 <= numero <= 100):
    print('Olá!')

