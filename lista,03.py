n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite um ultimo numero: '))
if n1 > n2 and n1 > n3:
    print(f'O numero {n1} é o maior dos 3')
elif n2 > n1 and n2 > n3:
    print(f'O numero {n2} é o maior dos 3')
else:
    print(f'O numero {n3} é o maior dos 3')