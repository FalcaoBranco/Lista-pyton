quantidade_de_alunos = int(input('Digite a quantidade de alunos: '))
soma_idades = 0
for i in range(quantidade_de_alunos):
    anos = int(input('Quantos anos o aluno tem: '))
    while True:
        soma_idades += anos
        break
media = soma_idades / quantidade_de_alunos
print(f'A media de idade da turma é {media}')
