print("Responda 'Sim' ou 'Não' para as seguintes perguntas:")

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas = []

for pergunta in perguntas:
    resposta = input(pergunta + " ")
    if resposta.lower() == 'sim':
        respostas.append(True)
    else:
        respostas.append(False)

quantidade_respostas_positivas = sum(respostas)

if quantidade_respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= quantidade_respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif quantidade_respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("Classificação:", classificacao)
