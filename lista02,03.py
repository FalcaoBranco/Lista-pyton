nome = input('Digite um nome com mais de 3 de caracteres: ')
while len(nome) <= 3:
    print('Seu nome deve ter mais de 3 caracteres')
    nome = input('Digite um nome com mais de 3 caracteres: ')

idade = int(input('Digite uma idade entre 0 a 150: '))
while idade < 0 or idade > 150:
    print('A idade tem que ser menor de 150 e maior que 0')
    idade = int(input('Digite uma idade maior que 0 e menor que 150: '))
        
salario = float(input('Digite um salario maior que zero: '))  
while salario < 0:
    print('Não se pode ter salario negativo: ')
    salario = float(input('Digite o valor do salario: '))

sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Biologicamente, você deve ser 'f' ou 'm': ")

estado_civil = input('Escolha um estado civil entre solteiro(s), casado(c), viuva(v), divolciado(d): ')
while (estado_civil!= 's') and (estado_civil!= 'c') and (estado_civil!= 'v') and (estado_civil!= 'd'):
    estado_civil = input('Deve digitar somente (s), (c), (v) ou (d): ')

print(f'{nome}')
print(f'{idade}')
print(f'{salario}')
print(f'{sexo}')
print(f'{estado_civil}')
