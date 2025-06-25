#Validação com while e break
#Faça um programa que repita a leitura de uma palavra até que o usuário digite “sair”.

while True:
   palavra = input('Digite uma palavra: ')
   if palavra.lower() == 'sair':
     break
   