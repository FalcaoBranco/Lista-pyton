numero = int(input('Digite um numero menor que 1000: '))
if numero >= 1000:
    print('ERRO o numero é maior que 1000')
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10

    print(f'Seu numero tem {centenas} centenas')
    print(f'Seu numero tem {dezenas} dezenas')
    print(f'Seu numero tem {unidades} unidades')


