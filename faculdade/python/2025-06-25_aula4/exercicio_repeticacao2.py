#Peça ao usuário um valor inicial e final e exiba os números nesse intervalo usando while.

inicial = int(input('Digite um valor inteiro inicial: '))
final = int(input('Digite um valor inteiro final: '))

controle = inicial

while controle < final:    
    print(controle)
    controle += 1
