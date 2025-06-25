
qnt = int(input('Quantas notas deseja calcular? '))

soma = 0 
contador = 0 

while contador < qnt:
   nota = float(input('Insira uma nota: '))
   soma += nota # Soma recebe os valores das notas digitadas
   contador += 1 #Limita o looping
media = soma / qnt
print(f'O valor dá média é {media:.2f}')
