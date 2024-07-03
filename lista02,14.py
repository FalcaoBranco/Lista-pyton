nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Suas notas são {nota1} e {nota2}')

if media > 9 and media < 10:
    nota = 'A'
    print(f'Sua media é {media} Aprovado com nota {nota}')
elif media > 7.5 and media < 9:
    nota = 'B'
    print(f'Sua media é {media} Aprovado com nota {nota}')
elif media > 6 and media < 7.5:
    nota = 'C'
    print(f'Sua nota é {media} Aprovado com nota {nota}')
elif media > 4 and media < 6:
    nota = 'D'
    print(f'Sua nota é {media} Reprovado com nota {nota}')
elif media > 0 and media < 4:
    nota = 'E'
    print(f'Sua nota é {media} Reprovado com nota {nota}')

