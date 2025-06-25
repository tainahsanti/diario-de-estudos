#Crie a tabuada de multiplicação de um número informado pelo usuário (1 a 10) usando for.

num = int(input('Digite um número para calcular a tabuaba: '))

print(f'Tabuada do número {num}')

for i in range (1, 11, 1):
    print(f'{i} x {num} = {i * num}')