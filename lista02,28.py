tipo_de_carne = input('Qual vai ser o tipo de carne digite (F) para File Duplo (A) para Alcatra ou (P) para Picanha só podera escolher uma: ').upper()
cartao = input('Tem cartão Tabajara S/N: ').upper()
if tipo_de_carne == 'F':
    peso_da_carne = float(input('Peso da carne: '))
    peso_da_carne_aredondado = round(peso_da_carne,2)
    peso_da_carne = peso_da_carne_aredondado
    if peso_da_carne <= 5:
        preco_carne = peso_da_carne * 4.90
        preco_total = preco_carne
        if cartao == 'S':
            desconto = preco_carne * (5/100)
            desconto_aredondado = round(desconto,2)
            desconto = desconto_aredondado
            preco_total = preco_carne - desconto
            print(f'Carne tipo File Duplo')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto de {desconto}')
        elif cartao == 'N':
            preco_total = preco_carne 
            print(f'Carne tipo File Duplo')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto sem desconto')
    
    elif peso_da_carne > 5:
        preco_carne = peso_da_carne * 5.80
        preco_total = peso_da_carne
        if cartao == 'S':
            desconto = preco_carne * (5/100)
            preco_total = preco_carne - desconto
            print(f'Carne tipo File Duplo')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto de {desconto}')
        elif cartao == 'N':
            preco_total = preco_carne 
            print(f'Carne tipo File Duplo')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto sem desconto')



elif tipo_de_carne == 'A':
    peso_da_carne = float(input('Peso da carne: '))
    peso_da_carne_aredondado = round(peso_da_carne,2)
    peso_da_carne = peso_da_carne_aredondado
    if peso_da_carne <= 5:
        preco_carne = peso_da_carne * 5.90
        preco_total = preco_carne
        if cartao == 'S':
            desconto = preco_carne * (5/100)
            preco_total = preco_carne - desconto
            print(f'Carne tipo Alcatra')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto de {desconto}')
        elif cartao == 'N':
            preco_total = preco_carne 
            print(f'Carne tipo Alcatra')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto sem desconto')

    elif peso_da_carne > 5:
        preco_carne = peso_da_carne * 6.80
        preco_total = preco_carne
        if cartao == 'S':
            desconto = preco_carne * (5/100)
            preco_total = preco_carne - desconto
            print(f'Carne tipo Alcatra')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto de {desconto}')
        elif cartao == 'N':
            preco_total = preco_carne 
            print(f'Carne tipo Alcatra')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto sem desconto')

elif tipo_de_carne == 'P':
    peso_da_carne = float(input('Peso da carne: '))
    peso_da_carne_aredondado = round(peso_da_carne,2)
    peso_da_carne = peso_da_carne_aredondado
    if peso_da_carne <= 5:
        preco_carne = peso_da_carne * 6.90
        preco_total = preco_carne
        if cartao == 'S':
            desconto = preco_carne * (5/100)
            preco_total = preco_carne - desconto
            print(f'Carne tipo Picanha')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto de {desconto}')
        elif cartao == 'N':
            preco_total = preco_carne 
            print(f'Carne tipo Picanha')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto sem desconto')

    elif peso_da_carne > 5:
        preco_carne = peso_da_carne * 7.80
        preco_total = preco_carne
        if cartao == 'S':
            desconto = preco_carne * (5/100)
            preco_total = preco_carne - desconto
            print(f'Carne tipo Picanha')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto de {desconto}')
        elif cartao == 'N':
            preco_total = preco_carne 
            print(f'Carne tipo Picanha')
            print(f'Peso total {peso_da_carne}')
            print(f'Total a pagar {preco_total}')
            print(f'Desconto sem desconto')