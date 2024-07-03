print('Qual sua relação com a vitima?')
print('Responda com Sim ou Não: ')

Telefonou = input("Telefonou para a vítima?: ")
Esteve = input("Esteve no local do crime?: ")
Mora = input("Mora perto da vítima?: ")
Devia = input("Devia para a vítima?: ")
Trabalhou = input("Já trabalhou com a vítima?: ")

if Telefonou == 'sim':
    print('Inocente')

elif Esteve == 'sim':
    print('Suspeita')

elif Mora == 'sim' or Devia == 'sim':
    print('Cumplice')

elif Trabalhou == 'sim':
    print('Assassino')

