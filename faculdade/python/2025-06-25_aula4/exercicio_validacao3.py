#Validação com while, continue e break
#Leia números positivos. Quando o usuário digitar 0, finalize e calcule a média dos valores digitados. Ignore valores negativos com continue.

contador = 0
soma = 0

while True:
    n1 = int(input('Insira um valor positivo: '))

    if n1 < 0:        
        continue
    if n1 == 0:       
        break
    if n1 > 0:
        soma += n1
        contador += 1    
        print(f'Sua soma atual é: {soma} e foram digitados {contador} números')  
        print('Para encerrar digite 0')  
media = soma / contador
print(f'o valor da média é: {media}')


   

