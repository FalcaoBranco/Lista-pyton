peso_morangos = float(input('Quanto foi o pesso dos Morangos?: '))
peso_maca = float(input('Quanto foi o pesso das Maças?: '))
peso_total = peso_maca + peso_morangos

print(f'Morango {peso_morangos}Kg')
print(f'Maça {peso_maca}Kg')
if peso_morangos <= 5:
    preco_morango = peso_morangos * 2.50

elif peso_morangos > 5:
    preco_morango = peso_morangos * 2.20

if peso_maca <= 5:
    preco_masa = peso_maca * 1.80

elif peso_maca > 5:
    preco_masa = peso_maca * 1.50

peso_total = peso_maca + peso_morangos

preco_total = preco_masa + preco_morango

if peso_total > 8:
    desconto = preco_total * (10/100)
    preco_total - desconto
    preco_aredondado = round(preco_total,2)
    preco_total = preco_aredondado
    print(f'O preço total é R$:{preco_total}')

else:
    print(f'O preço total é R$:{preco_total}')