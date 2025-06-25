# Exercicio ChatGPT

#🛒 6. Bônus com faixas
#Um funcionário recebe:
#30% de bônus se tiver mais de 10 anos de empresa
#20% se tiver entre 6 e 10 anos
#10% caso contrário
#Peça salário e ano de admissão e calcule a bonificação.

anoAtual = int(input('Digite o ano atual: '))
funcionario = input(f'Nome do funcionario: ')
salario = float(input(f'Salario do {funcionario}: '))
anoAdmissao = int(input(f'Ano que o {funcionario} foi contratado: '))

anosTrabalhados = anoAtual - anoAdmissao

if  anosTrabalhados > 10:
    bonus30 = salario * 0.3
    print(f'O {funcionario} recebe 30% de bônus. Neste caso o valor de bônus que ele irá receber é de R$ {bonus30}')

elif 6 <= anosTrabalhados <= 10:
    bonus20 = salario * 0.2
    print(f'O {funcionario} recebe 20% de bônus. Nesse caso o valor de bônus que ele irá receber é de R$ {bonus20}')

else:
    bonus10 = salario * 0.1
    print(f'O {funcionario} recebe 10% de bônus. Nesse caso o valor de bônus que ele irá receber é de R$ {bonus10}')


