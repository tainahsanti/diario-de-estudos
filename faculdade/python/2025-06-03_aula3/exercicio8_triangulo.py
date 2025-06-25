# Exercicio ChatGPT

#📐 8. Classificação de Triângulo
#Peça os 3 lados de um triângulo e:
#Verifique se é um triângulo válido.
#Classifique como: equilátero, isósceles ou escaleno.

n1 = int(input('Digite o primeiro lado do triangulo: '))
n2 = int(input('Digite o segundo lado do triangulo: '))
n3 = int(input('Digite o terceiro lado do triangulo: '))

if n1 == n2 == n3:
    print('Esse triângulo é um equilátero')

elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Esse triângulo é um isósceles')

elif n1 != n2 and n1 != n3 and n2 != n3:
    print('Esse triângulo é um escanleno')
