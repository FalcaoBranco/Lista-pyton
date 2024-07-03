populacao_A = 80000
taxa_de_crecimento_A = 0.03

populacao_B  = 200000
taxa_de_crecimento_B = 0.015

anos = 0

while True:
    populacao_A += populacao_A * taxa_de_crecimento_A
    populacao_B += populacao_B * taxa_de_crecimento_B
    if populacao_A <= populacao_B:
        anos += 1

    else:
        print(int(populacao_A))
        print(int(populacao_B))
        print(f'Vai demorar {int(anos)} para a população a passar A ser maior que a de B ')

        break


#populacao_a = 80000
#taxa_crescimento_a = 0.03

#populacao_b = 200000
#taxa_crescimento_b = 0.015

#anos = 0

#while populacao_a < populacao_b:
#    populacao_a += populacao_a * taxa_crescimento_a
#    populacao_b += populacao_b * taxa_crescimento_b
#    anos += 1

#print(f'Após {anos} anos, a população do país A ultrapassou ou igualou a população do país B.')
#print(f'População do país A: {int(populacao_a)} habitantes.')
#print(f'População do país B: {int(populacao_b)} habitantes.')
