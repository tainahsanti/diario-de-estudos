#Faça um relógio digital com hora, minuto e segundo entre dois horários definidos pelo usuário.

hora_inicial = int(input('Digite a hora inicial: '))
minuto_inicial = int(input('Digite a minuto inicial: '))
segundo_inicial = int(input('Digite o segundo inicial: '))

hora_fim = int(input('Digite a hora fim: '))
minuto_fim = int(input('Digite a minuto fim: '))
segundo_fim = int(input('Digite o segundo fim: '))

hora_atual = hora_inicial
minuto_atual = minuto_inicial
segundo_atual = segundo_inicial

while (hora_atual, minuto_atual, segundo_atual) <= (hora_fim, minuto_fim, segundo_fim):

    segundo_atual += 1 

    if segundo_atual == 60:
        segundo_atual = 0
        minuto_atual += 1
    if minuto_atual == 60:
        minuto_atual = 0
        hora_atual += 1

    print(f'{hora_atual:02}:{minuto_atual:02}:{segundo_atual:02}')