# Exercicio ChatGPT

#🚦 3. Bônus por tempo de empresa
#Solicite o salário e o tempo de empresa do usuário.
#Se o tempo for superior a 5 anos, ele recebe bônus de 20%.
#Caso contrário, o bônus é de 10%.

nome = input('Nome do funcionario: ')
salario = float(input('Valor do salario: '))
tempoEmpresa = int(input('Quantos anos trabalha na empresa? '))

if tempoEmpresa >= 5:
    bonus20 = salario * 0.20
    salarioBonus20 = salario + bonus20
    print(f'O valor do bônus do {nome} é de R$ {bonus20}, o total do salario será de R$ {salarioBonus20}')

elif tempoEmpresa <= 4:
    bonus10 = salario * 0.10
    salarioBonus10 = salario + bonus10
    print(f'O valor do bônus do {nome} é de R$ {bonus10}, o total do salario será R$ {salarioBonus10}')