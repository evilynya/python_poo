class Personagem:
    def __init__(self, nome, vida=5):
        self._nome = nome
        self._vida = vida

    def atacar(self):
        print(f"{self._nome} está atacando!")

    
class Jogador(Personagem):
    def __init__(self, nome, raca, inventario, vida=5):
        super().__init__(nome, vida)
        self._raca = raca
        self._inventario = inventario
    
    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}, Raça: {self._raca}")

    def usarHabilidade(self, poder):
        print(f"Habilidade ativada: {poder}")

    def coletarItem(self, item):
        print(f"Item coletado: {item}. Itens no inventário: {self._inventario}")

class Monstro(Personagem):
    def __init__(self, nome, tipo, forca, vida=20):
        super().__init__(nome, vida)
        self._tipo = tipo
        self._forca = forca

    def exibirInformacoes(self):
        print(f"Nome: {self._nome}, Tipo: {self._tipo}, Vida: {self._vida}, Força: {self._forca}")

    def invocarAliado(self, nomeAliado, tipoAliado):
        novo_aliado = Monstro(nomeAliado, tipoAliado, forca=10)  
        print(f"{self._nome} invocou {novo_aliado._nome}, o {novo_aliado._tipo}!")

    def defender(self):
        self._vida -= 1
        print(f"{self._nome} se defendeu! Vida restante: {self._vida}")
