soma = 0
mulheres = 0
media = 0
maior = 0
maisvelha = "Renan"
menor20 = 0
for contagem in range(1,4):
    nome = input('Digite o nome: ')
    sexo = input('Masculino ou Feminino? [M/F]').upper()
    idade = int(input('Digite a idade: '))

    soma += idade
    if sexo == 'M' and idade > maior:
        maior = idade
        maisvelha = nome

    if sexo == 'F' and idade > maior:
        maior = idade
        maisvelha = nome
        mulheres += 1

    if idade < 20:
        menor20 += 1
soma = 0

print('Medias das idades é de {:.2f}'.format(media))
print(f'O nome da pessoa mais velha é {maisvelha} e sua idade é {maior}')

if mulheres == 0:
    print('Não temos mulheres no grupo')
else:
    print(f'Ao todo temos {mulheres}')

print(f'Temos {menor20} com menos de 20 anos.')