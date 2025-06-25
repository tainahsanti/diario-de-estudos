#Validação com while, continue e break
#Crie um sistema de login onde só acessa se o usuário for "admin" e a senha "123". Use while True, continue e break.

while True:
    usuario = input('Digite seu usuario: ')
    if usuario.lower() == 'admin':
        senha = input('Digite sua senha: ')
        if senha == '123':
            print('Acesso concedido!')
        else:
            print('Senha incorreta, tente novamente mais tarde!')
            break
    else:
        print('Usuário incorreto, tenta novamente!')
        continue