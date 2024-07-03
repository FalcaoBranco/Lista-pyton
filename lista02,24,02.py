numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite outro numero: '))

operacao = int(input('Qual opereção você quer realisar Digite 1 para soma 2 para subitrair 3 para multiplicar e 4 para dividir: '))

if operacao == 1:
    numero = numero1 + numero2
    operacao_texto = 'Soma'

elif operacao == 2:
    numero = numero1 - numero2
    operacao_texto = 'Subitração'

elif operacao == 3:
    numero = numero1 * numero2
    operacao_texto = 'Multiplicação'

elif operacao == 4:
    numero = numero1 / numero2
    operacao_texto = 'Divisão'

else:
    print('Opereção inválida.')

print(f'O resultado da {operacao_texto} é {numero}: ')

resto = numero % 2
numero_aredondado = round(numero)
if resto == 0:
    print('O numero é par')
else:
    print('O numro é impar')

if numero > 0:
    print('O numero é positivo')

else:
    print('O numero é nagativo')

if numero == numero_aredondado:
    print('O numero é inteiro')

else:
    print('O numero é decimal') 

