#Faça um programa que peça dois números e imprima todos os múltiplos de 5 entre eles usando while.

valor1 = int(input('Insira um número inteiro: '))
valor2 = int(input('Insira outro número inteiro: '))

controle = valor1

while controle <= valor2:
    if controle % 5 == 0: # O operador % retorna o resto da divisão. Se atual % 5 == 0, então o número atual é divisível por 5, ou seja, é múltiplo de 5.
        print(controle)
    controle += 1
    


