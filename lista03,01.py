while True:
    numero = float(input('Digite uma nota entre 0 e 10: '))
    if numero < 0 or numero > 10:
        print('Erro nota não é numero valido:')
        

    else:
        print(f'Nota {numero} valida obrigado ')

        break