# Exercicio ChatGPT

#🧮 4. Verificação de Aprovação
#Um aluno cursa 3 matérias. Solicite a nota final de cada uma.
#Informe se ele foi aprovado somente se todas as notas forem maiores ou iguais a 7.

materia1 = input('Qual o nome da primeira materia? ')
materia2 = input('Qual o nome da segunda materia? ')
materia3 = input('Qual o nome da terceira materia? ')

nota1 = float(input(f'Nota da disciplina {materia1}: '))
nota2 = float(input(f'Nota da discipliana {materia2}: '))
nota3 = float(input(f'Nota da disciplina {materia3}: '))

if nota1 >= 7 and nota2 >= 7 and nota3 >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado')

