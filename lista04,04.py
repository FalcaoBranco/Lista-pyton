lista = []
consoantes = 0
for i in range(10):
    letra = input('Digite uma letra: ').lower()
    lista.append(letra)
    if letra not in ['a','e','i','o','u']:
        consoantes += 1

print('As consoantes digitadas foram: ')
for letra in lista:
    if letra not in ['a','e','i','o','u']:
        print(letra)
        
        
print(f'O total de consoantes é {consoantes}')