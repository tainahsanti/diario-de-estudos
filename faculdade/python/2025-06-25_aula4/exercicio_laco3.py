#Peça a idade e o sexo de várias pessoas. Imprima uma saudação personalizada para "M" ou "F". Pare se idade < 0.

while True:   

    idade = int(input('Qual a sua idade? '))

    if idade > 0:
        genero = input('Qual o seu genero? (F/M): ')        

        if genero.lower() == 'f':
            print('Olá, senhora!')
              
        elif genero.lower() == 'm':
            print('Olá, senhor')
    
    else:
        break # Só funciona dentro de looping