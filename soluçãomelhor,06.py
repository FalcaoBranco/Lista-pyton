# Solicitar três números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Ordenar os números em ordem decrescente
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
meio = (num1 + num2 + num3) - (maior + menor)

# Mostrar os números em ordem decrescente
print("Três números em ordem decrescente:")
print(maior, meio, menor)
