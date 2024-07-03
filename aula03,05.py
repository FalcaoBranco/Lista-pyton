pares = 0
impares = 0 
for voltas in range(100):
    if voltas % 2 == 0:
        pares += 1
    else:
        impares += 1

for voltas in range(1,100,2):
    if voltas % 2 == 0:
        pass
    else:
        print(voltas)
print(f'A  quantidade de numeros pares entre 1 e 100 é {pares}')
print(f'A  quantidade de numeros inpares entre 1 e 100 é {impares}')