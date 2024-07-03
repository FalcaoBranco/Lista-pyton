salario = float(input('Digite seu antigo salario: '))

if salario <= 280:
    novo_salario = salario + salario * (20/100)
    valor_aumentado = salario * (20/100)
    print(f'Seu salario passa a ser {novo_salario}')
    print(f'Seu antigo salario era {salario}')
    print('Seu salario sofreu um ajuste de 20%')
    print(f'Voce teve um aumento de {valor_aumentado}')
    
elif salario > 280 and salario < 700:
    novo_salario = salario + salario * (15/100)
    valor_aumentado = salario * (15/100)
    print(f'Seu antigo salario era {salario}')
    print('Seu salario sofreu um ajuste de 15%')
    print(f'Voce teve um aumento de {valor_aumentado}')
    print(f'Seu salario passa a ser {novo_salario}')

elif salario >= 700 and salario < 1500:
    novo_salario = salario + salario * (10/100)
    valor_aumentado = salario * (10/100)
    print(f'Seu antigo salario era {salario}')
    print('Seu salario sofreu um ajuste de 10%')
    print(f'Voce teve um aumento de {valor_aumentado}')
    print(f'Seu salario passa a ser {novo_salario}')

elif salario >= 1500:
    novo_salario = salario + salario * (5/100)
    valor_aumentado = salario * (5/100)
    print(f'Seu antigo salario era {salario}')
    print('Seu salario sofreu um ajuste de 5%')
    print(f'Voce teve um aumento de {valor_aumentado}')
    print(f'Seu salario passa a ser {novo_salario}')