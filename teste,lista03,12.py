numero = int(input("Digite um número de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Número inválido. Digite um número de 1 a 10: "))

print(f"Tabuada do número {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
