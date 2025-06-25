#Crie um programa que peça um número positivo. Enquanto o usuário digitar um valor inválido, solicite novamente.

n1 = int(input('Insira um número positivo: '))

while n1 <= 0:
    n1 = int(input('Valor inválido. Digite um número positivo: '))

print(f'{n1} é um número positivo.')
    