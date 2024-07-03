numero = 10 
while True:
    advinha = int(input('Digite um numero: '))
    if advinha == numero:
        print('Miseravi acertou!')
        break
    else:
        print('Tente novamente')