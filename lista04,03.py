lista = []
soma = 0
for i in range(4):
    nota = float(input('Digite uma nota: '))
    lista.append(nota)
    soma += nota

print('As suas notas são:')
for nota in lista:
    
    print(nota)

media = soma / 4
print(f'Sua media é {media}: ')
