class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        pass

class Carro(Veiculo):
    def mover(self):
        return f"O carro {self.nome} está se deslocando na estrada."

class Bicicleta(Veiculo):
    def mover(self):
        return f"A bicicleta {self.nome} está pedalando na ciclovia."

meu_carro = Carro("Sedan")
minha_bicicleta = Bicicleta("Mountain Bike")

veiculos = [meu_carro, minha_bicicleta]

for veiculo in veiculos:
    print(veiculo.mover())
