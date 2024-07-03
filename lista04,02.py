lista = []
for i in range(5):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

for numero in reversed(lista):
    print(numero)