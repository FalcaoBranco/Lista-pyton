n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero : '))
n3 = float(input('Digite um ultimo numero: '))
maior = max(n1,n2,n3)
menor = min(n1,n2,n3)
print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')

if n1 == n2 :
    
    print(f'existem numeros iguais e eles são {n1} e {n2}')

elif n1 == n3:
     
     print(f'existem numeros iguais e eles são {n1} e {n3}')

elif n2 == n3:
     
     print(f'existem numeros iguais e eles são {n2} e {n3}')

else:
     print('Não existem numeros iguais')