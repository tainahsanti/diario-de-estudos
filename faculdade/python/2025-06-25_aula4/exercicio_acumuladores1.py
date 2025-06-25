#Escreva um programa que peça 7 números e calcule a soma total e a média deles.

i = 0
soma = 0

while i < 7:    
    valor = float(input('Digite um valor: '))
    i += 1
    soma += valor
media = soma / 7
print(f'O valor total é de {soma:.2f} e a média do valor é de {media:.2f}')

