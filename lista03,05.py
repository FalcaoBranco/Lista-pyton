while True:
    try:
        populacao_a = int(input('Informe a população do país A: '))
        taxa_crescimento_a = float(input('Informe a taxa de crescimento anual do país A (em decimal): '))
        populacao_b = int(input('Informe a população do país B: '))
        taxa_crescimento_b = float(input('Informe a taxa de crescimento anual do país B (em decimal): '))

        if populacao_a <= 0 or populacao_b <= 0 or taxa_crescimento_a <= 0 or taxa_crescimento_b <= 0:
            print('Informe valores válidos (populações e taxas de crescimento devem ser maiores que zero).')
            continue

        anos = 0

        while populacao_a < populacao_b:
            populacao_a += populacao_a * taxa_crescimento_a
            populacao_b += populacao_b * taxa_crescimento_b
            anos += 1

        print(f'Após {anos} anos, a população do país A ultrapassou ou igualou a população do país B.')
        print(f'População do país A: {int(populacao_a)} habitantes.')
        print(f'População do país B: {int(populacao_b)} habitantes.')

        break

    except ValueError:
        print('Informe valores numéricos válidos.')
