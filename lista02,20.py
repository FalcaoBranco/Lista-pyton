nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media >= 7 and media <= 9.9:
    print(f'Aprovado com nota {round(media,1)} alcançada')
elif media < 7:
    print(f'Reprovado com nota {round(media,1)} alcançada')
elif media == 10:
    print(f'Aprovado com distinção com media {round(media,1)} ')