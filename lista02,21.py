valor_do_saque = (float(input('Quando deseja sacar entre 10 e 600 Reais : ')))
if valor_do_saque < 10 or valor_do_saque > 600:
    print(f'ERRO valor do saque não pode ser menor que R$:10 nem mais do que R$:600')

else:
    notas_100 = valor_do_saque // 100
    valor_do_saque %= 100

    notas_50 = valor_do_saque // 50
    valor_do_saque %= 50

    notas_10 = valor_do_saque // 10
    valor_do_saque %= 10

    notas_5 = valor_do_saque // 5
    valor_do_saque %= 5

    notas_1 = valor_do_saque // 1

    print("Notas a serem fornecidas:")
    print(f"Notas de 100 reais: {notas_100}")
    print(f"Notas de 50 reais: {notas_50}")
    print(f"Notas de 10 reais: {notas_10}")
    print(f"Notas de 5 reais: {notas_5}")
    print(f"Notas de 1 real: {notas_1}")