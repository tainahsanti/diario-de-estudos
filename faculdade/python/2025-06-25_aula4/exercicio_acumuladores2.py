#Faça um programa que leia 10 valores e conte quantos deles são maiores que 50.

i = 0
numeros = 0

while i < 10:
    valores = int(input('Insira um valor: '))       
    if valores > 50:
        numeros +=1
    i += 1 
print(f'Total: {numeros}')           
