lista_numeros = []
def calcular_media():
    while True:
        numero = int(input('Digite um numero: '))
        lista_numeros.append(numero)
        continuar = input('Você quer mais um numero? S/N: ').upper()
        if continuar == "N":
            break
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

media_calculada = calcular_media()
print(f'A média dos números é: {media_calculada}')
