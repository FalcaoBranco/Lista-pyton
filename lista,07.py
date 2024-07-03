t = input('Em qual turno você estuda? Digite V para vespertinno M para matutino ou N para noturno: ')
if t == 'V' or t == 'v' : 
    print('Bom dia')
elif t == 'M' or t == 'm':
    print('Boa tarde')
elif t == 'N'or t == 'n':
    print('Boa noite')
else:
    print('Valor Inválido!')