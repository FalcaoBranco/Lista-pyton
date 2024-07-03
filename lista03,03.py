while True:
    nome = input('Digite um nome maior que 3 caracteres: ')
    if len(nome) < 3:
        print('Seu nome tem que ter mais do que 3 caracteres')

    else:
        print('Nome aceito')

        break

while True:
    idade = int(input('Digite uma idade entre 0 a 150: '))
    if idade < 0 or idade > 150:
        print('Idade não valida ')
        print('Tente novamente')

    else:
        print('Idade valida')

        break

while True:
    salario = float(input('Digite um salario maior que zero: '))
    if salario < 0:
        print('Salario menor que 0 invalido')
        print('Digite noivamente')

    else:
        print('Salario valido')

        break

while True:
    sexo = input('Digite um sexo entre (F) Feminino (M) masculino ').upper()
    if sexo != 'F' and sexo != 'M':
        print('Sexo informado erro')
        print('Digite sexo novamente')

    else:
        print('Conformado')

        break

while True:
    estado_civil = input('Digite um estado civil entre (C) casado(a) (S) solteiro(a) (V) viuvo(a) (D) divorciado(a): ').upper()
    if estado_civil != 'C' and estado_civil != 'S' and estado_civil != 'V' and estado_civil != 'D':
        print('Estado civil erro ')
        print('Digite novamente')


    else:
        print('Estado civil valido ')
        break

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)

