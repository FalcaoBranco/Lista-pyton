
x = 17
Quantidade = 0
while True:
    numero = int(input('Acerte o numero que estou pensando: '))
    if x < numero:
        print(f'O numero que eu estou pensando é menor que {numero}')
        Quantidade += 1

    elif x > numero:
        print(f'O numero que estou pensando é maior que {numero}')
        Quantidade += 1

    elif x == numero:
        print(f'Exatamente {x} é o numero que eu estou pensando')
        print(f'Voce demorou {Quantidade} de vezes para acertar')
        break