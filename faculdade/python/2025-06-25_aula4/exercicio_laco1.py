#Crie a tabuada completa de 1 até 10, usando dois for aninhados.

for base in range (1,11):
    for numero in range(1,11):
        print(f'{base} x {numero} = {base * numero}')