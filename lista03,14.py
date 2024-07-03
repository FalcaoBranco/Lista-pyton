impares = 0
pares = 0
for i in range(10):
    numero = int(input('Digite um numero: '))
    resto = numero % 2
    if resto == 0:
        pares += 1
    else:
        impares += 1

print(f'O numero total de numeros pares é {pares}')
print(f'O numero total de numeros impares é {impares}')
    
