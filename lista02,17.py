ano = int(input('Digite um ano: '))
bissexto = ano % 4
if bissexto == 0:
    print('Esse ano é bissexto')
else:
    print('Esse ano não é bissexto')