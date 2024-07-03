class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def definir_nome(self, nome):
        self.nome = nome

    def definir_idade(self, idade):
        self.idade = idade

    def obter_nome(self):
        return self.nome

    def obter_idade(self):
        return self.idade


pessoa1 = Pessoa("Alice", 30)

print(f"Nome: {pessoa1.obter_nome()}")
print(f"Idade: {pessoa1.obter_idade()}")

pessoa1.definir_nome("Bob")
pessoa1.definir_idade(25)

print(f"Novo Nome: {pessoa1.obter_nome()}")
print(f"Nova Idade: {pessoa1.obter_idade()}")
