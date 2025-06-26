#Peça ao usuário uma palavra e conte quantas letras "a" existem nela.

palavra = input('Digite uma palavra: ')
palavra = palavra.lower() #Tornar a palavra em minusculo para que os As fiquem iguais
quantidade = palavra.count('a') #Count = contar. Contar quantos As tem na palavra digitada pelo usuario

print(f'A palavra {palavra}, tem {quantidade} de As.')