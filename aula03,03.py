soma = 0
for volta in range(6):
    numero = int(input('Digite um numero:'))
    
    if numero % 2 == 0:
       soma += numero


print(f'{soma}')
