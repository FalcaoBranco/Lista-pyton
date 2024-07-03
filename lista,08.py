salario = float(input('Digite o seu salario R$: '))
if salario <= 280:
    print(f'Seu salario era {salario}')
    print('Seu salario tera um aumento de 20%')
    aumento = salario * (20/100)
    print(f'O valor que vai aumenta no seu salario é de {aumento}')
    novosalario = salario + aumento 
    print(f'Seu novo salario é {novosalario}')
elif salario >= 281 and salario < 700:
    print(f'Seu salario era {salario}')
    print('Seu salario tera um aumento de 15%')
    aumento = salario * (15/100)
    print(f'O valor que vai aumenta no seu salario é de {aumento}')
    novosalario = salario + aumento 
    print(f'Seu novo salario é {novosalario}')
elif salario >= 701 and salario < 1500:
    print(f'Seu salario era {salario}')
    print('Seu salario tera um aumento de 10%')
    aumento = salario * (10/100)
    print(f'O valor que vai aumenta no seu salario é de {aumento}')
    novosalario = salario + aumento 
    print(f'Seu novo salario é {novosalario}')
elif salario >= 1501 :
    print(f'Seu salario era {salario}')
    print(f'Seu salario tera um aumento de 5%')
    aumento = salario * (5/100)
    print(f'O valor que vai aumenar do seu salario é de {aumento}')
    novosalario = salario + aumento
    print(f'Seu novo salario é {novosalario}')
