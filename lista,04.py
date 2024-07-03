n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
if n1 > n2 and n1 > n3 and  n2 > n3:
    print(f'O numero {n1} é o maior e {n3} é o menor')
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(f'O numero {n1} é o mair e {n2} é o menor')
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'O numero {n2} é o maior e o {n3} é o menor')
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'O numero {n2} é o maior e {n1} é o menor')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'O numero {n3} é o mairo e {n2} é o maior ')
else:
    print(f'O  numero {n3} é o maior e {n1} é o menor')