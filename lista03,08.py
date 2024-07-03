lista = []
soma = 0
for i in range(5):
    numero = float(input('Digite um numero: '))
    lista.append(numero)
    soma += numero
media = soma / 5
print(soma)
print(media)  