n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite um ultimo numero: '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(f'{n1} {n2} {n3}')
elif n1 > n2 and n1 >n1 and n3 > n2:
    print(f'{n1} {n3} {n2}')
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(f'{n2} {n1} {n3}')
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(f'{n2} {n3} {n1}')
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(f'{n3} {n1} {n2}')
else:
    print(f'{n3} {n2} {n1}') 


