#Solicite ao usuário uma frase com no mínimo 10 e no máximo 30 caracteres. Mostre a frase com e sem espaços.

print('Frase com no mínimo 10 e no máximo 30 caracteres')

while True:
   
    frase = input('Escrava uma frase: ')

    if 10 <= len(frase) <= 30:
        print(f'Frase original: {frase}, contém {len(frase)} caracteres')
        print(f'Frase em espaço: {frase.replace(' ', '')}')
        break
        
    else:
        print('Frase invalida! Tente novamente')
        continue
    