#Exercicio CHATGPT

#Exercício 1 — Apresentação simples
#Peça ao usuário que insira seu nome e sua idade, e exiba uma mensagem usando uma f-string.
#Desafio: transforme a idade em número e diga quantos anos a pessoa terá daqui a 5 anos.

nome = input('Qual o seu nome? ')
idade = int(input('Qual é a sua idade? '))

print(f'Seu nome é {nome} e você tem {idade} anos')

idade_futura = idade + 5

print(f'Daqui a 5 anos, você terá {idade_futura} anos')

