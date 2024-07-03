dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))
if ano < 0:
    print('Erro ano não pode ser menor que 0')
elif ano > 0:
    if mes < 0 or mes > 12:
        print('Erro mês não pode ser menor que 0 ou maior que 12')
    elif mes > 0 and mes < 12:
        if dia < 0 or dia > 30:
            print('ERRO dia não pode ser negativo nem maior que 30')
        else:
            print(f'O dia {dia,mes,ano} é uma data valida')
