# Inicializa as variáveis para armazenar os dados
pessoas = []
soma_idade = 0
maior_idade = 0
nome_mais_velho = ""
contador_menos_20 = 0
contador_mais_40 = 0
sexo_pessoa_mais_nova = ""
menor_idade = 1000000000

# Loop para ler os dados das 5 pessoas
for i in range(5):
    nome = input("Digite o nome da pessoa {}: ".format(i + 1))
    idade = int(input("Digite a idade da pessoa {}: ".format(i + 1)))
    sexo = input("Digite o sexo da pessoa {}: ".format(i + 1))

    # Atualiza as variáveis conforme os dados informados
    soma_idade += idade

    if idade > maior_idade:
        maior_idade = idade
        nome_mais_velho = nome

    if idade < 20:
        contador_menos_20 += 1

    if idade > 40:
        contador_mais_40 += 1

    if i == 0:
        sexo_pessoa_mais_nova = sexo

    elif idade < menor_idade:
        menor_idade = idade
        sexo_pessoa_mais_nova = sexo

    # Cria um dicionário com os dados da pessoa atual e adiciona à lista de pessoas
    pessoa = {'nome': nome, 'idade': idade, 'sexo': sexo}
    pessoas.append(pessoa)

# Calcula a média de idade do grupo
media_idade = soma_idade / 5

# Exibe os resultados
print("Média de idade do grupo:", media_idade)
print("Nome da pessoa mais velha:", nome_mais_velho)
print("Quantidade de pessoas com menos de 20 anos:", contador_menos_20)
print("Quantidade de pessoas com mais de 40 anos:", contador_mais_40)
print("Sexo da pessoa mais nova:", sexo_pessoa_mais_nova)
