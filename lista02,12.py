salario_bruto = float(input('Digite seu salario bruto: '))
if salario_bruto <= 900:
    desconto_IR =  salario_bruto * (0/100)
    print(f'R$:{desconto_IR} foi abatido do seu salario pelo IR')

elif salario_bruto > 900 and salario_bruto <= 1500:
    desconto_IR = salario_bruto * (5/100)
    print(f'R$:{desconto_IR} foi abatido do seu salario pelo IR')

elif salario_bruto > 1500 and salario_bruto <= 2500:
    desconto_IR = salario_bruto * (10/100)
    print(f'R$:{desconto_IR} foi abatido do seu salario pelo IR')

elif salario_bruto > 2500:
    desconto_IR = salario_bruto * (20/100)
    print(f'R$:{desconto_IR} foi abatido do seu salario pelo IR')

desconto_sindicato = salario_bruto * (3/100)
print(f'R$:{desconto_sindicato} foi abatido do seu salario pelo sindicato')

Fgts = salario_bruto * (11/100)
print(f'R$:{Fgts} foi foi pago pela empresa para o FGTS')

reducao_total_do_salario = desconto_IR + desconto_sindicato
print(f'A redução total do salario foi de R${reducao_total_do_salario}')

salario_liquido = salario_bruto - reducao_total_do_salario
print(f'Salario liquido é R${salario_liquido}')

