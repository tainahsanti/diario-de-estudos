# Exercicio ChatGPT

#Exercício 7 — Classificação Etária
#Peça ao usuário que digite a sua idade e classifique a pessoa em uma das seguintes categorias:
#Criança (0 a 12 anos)
#Adolescente (13 a 17 anos)
#Adulto (18 a 59 anos)
#Idoso (60 anos ou mais)
#Exiba na tela: "Você é um(a) [categoria]"

idade = int(input('Quantos anos você tem? '))

if 0 <= idade <= 12:
    print('Você é uma criança')

elif 13 <= idade <= 17:
    print('Você é um(a) adolescente')

elif 18 <= idade <= 59:
    print('Você é um(a) adulto')
    
elif idade >= 60:
    print('Você é um(a) idoso)')