pessoa_mais_velha = []
quantitade_de_pessoas_menos_de_20 = 0
quantidade_de_pessoas_mais_de_40 = 0
sexo_da_pessoa_mais_nova = {}
soma_idade = 0
maior_idade = 0
menor_idade = 1000000000

for i in range(5):
    nome = input("Digite o nome da pessoa {}: ".format(i + 1))
    idade = int(input("Digite a idade da pessoa {}: ".format(i + 1)))
    sexo = input("Digite o sexo da pessoa {}: ".format(i + 1))

    soma_idade += idade

    if idade > maior_idade:
        maior_idade = idade
        pessoa_mais_velha = nome
        

    if idade < 20:
        quantitade_de_pessoas_menos_de_20 += 1

    if idade > 40:
        quantidade_de_pessoas_mais_de_40 += 1

    if idade < menor_idade:
        menor_idade = idade
        sexo_da_pessoa_mais_nova = sexo

    media = (soma_idade / 5)

print(f'A media de idade do grupo é {media}')
print(f'O nome da pessoa mais velha é {pessoa_mais_velha}')
print(f'A quantidade de pessoas com menos de 20 anos é {quantitade_de_pessoas_menos_de_20}')
print(f'A quantidade de pessosas com mais de 40 é {quantidade_de_pessoas_mais_de_40}')
print(f'O sexo da pessoa mais nova é {sexo_da_pessoa_mais_nova}')
