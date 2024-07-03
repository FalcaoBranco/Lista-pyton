
while True:
    usuario = input('Digite um usuario: ')
    senha = input('Digite uma senha diferente do usuario: ')
    if usuario == senha:
        print('Erro senha e igual ao usuario')
        print('Tente novamente:')

    else:
        print('Bem vindo ao sistema: ')
        break