numero01 = int(input('Digite um numero: '))
numero02 = int(input('Digite outro numero: '))

soma = 0
for i in range(numero01,numero02 + 1):
    print(i, end= ' ')
    soma += i

print(soma)