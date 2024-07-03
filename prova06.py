pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}

idade_joao = pessoas["João"]

print(f'A idade de joão é {idade_joao}')

pessoas['Ana'] = 31

print(pessoas)

maior_idade = max(pessoas.values())
for nome, idade in pessoas.items():
    if idade == maior_idade:
        pessoa_maior_idade = nome
        break

print(pessoa_maior_idade)