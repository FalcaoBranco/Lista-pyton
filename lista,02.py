n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2) / 2
if media >= 10:
    print('Aprovado com distinção')
elif media >= 6:
    print('Aprovado')
else: 
    print('Reprovado')