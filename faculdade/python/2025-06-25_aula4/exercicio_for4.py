#Solicite dois números: início e fim. Exiba os ímpares nesse intervalo usando for.

inicio = int(input('Digite o número inicial: '))
final = int(input('Digite o número final: '))

for controle in range (inicio, final):
    if controle % 2 == 1: # Resto da divisão para verificar se o número é impar
        print(controle)
  
   
