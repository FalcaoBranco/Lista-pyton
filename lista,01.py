letra = input("Digite uma letra: ")

# Verifica se a letra é uma vogal
if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("A letra digitada é uma vogal.")
# Verifica se a letra é uma consoante
elif letra.isalpha():
    print("A letra digitada é uma consoante.")
else:
    print("Caractere inválido. Por favor, digite uma letra.")

