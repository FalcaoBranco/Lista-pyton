Gasolina_ou_Alcool = input('Sera gasolina (G) ou alcool? (A): ')
litros = int(input('Quantos litros?: '))
if Gasolina_ou_Alcool == 'G':
    if litros < 20:
        custo = litros * 2.50
        descontos = custo * (4/100)
        total_a_pagar = custo - descontos
        print(f'O custo nomal é {custo}')
        print(f'O desconto foi de {descontos}')
        print(f'O total ficou {total_a_pagar}')
    elif litros >= 20:
        custo = litros * 2.50
        descontos = custo * (6/100)
        total_a_pagar = custo - descontos
        print(f'O custo nomal é {custo}')
        print(f'O desconto foi de {descontos}')
        print(f'O total ficou {total_a_pagar}')

elif Gasolina_ou_Alcool == 'A':
    if litros < 20:
        custo = litros * 1.90
        descontos = custo * (3/100)
        total_a_pagar = custo - descontos
        print(f'O custo nomal é {custo}')
        print(f'O desconto foi de {descontos}')
        print(f'O total ficou {total_a_pagar}')
    elif litros >= 20:
        custo = litros * 1.90
        descontos = custo * (5/100)
        total_a_pagar = custo - descontos
        print(f'O custo nomal é {custo}')
        print(f'O desconto foi de {descontos}')
        print(f'O total ficou {total_a_pagar}')