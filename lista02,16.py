import math
A = float(input('De um numero para a aquação: '))
B = float(input('De um segundo numero para a aquação: '))
C = float(input('De um terceiro numero para a aquação: '))

delta = B**2 - 4*A*C

if A == 0:
    print(f'A não pode ser zero')

elif delta < 0:
    print(f'O delta informado é negativo logo não possui raizes reais ')
    print('Programa encerrado')

elif delta == 0:
    raiz = -B / (2*A)
    print(f'A equação possui só {raiz} como raiz real')

elif delta > 0:
    raiz1 = (-B + math.sqrt(delta)) / (2*A)
    raiz2 = (-B - math.sqrt(delta)) / (2*A)
    print(f'A equação possui duas raizes que são {raiz1} e {raiz2}')
    