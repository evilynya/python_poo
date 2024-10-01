class Carro:
    def __init__(self, marca, modelo, ano, precoDiaria):
        self.marca = marca
        self.modelo = modelo 
        self.ano = ano
        self.precoDiaria = precoDiaria
    
    def exibirDetalhes(self):
        print(f"O carro escolhido é da marca {self.marca}, modelo {self.modelo}, do ano de {self.ano} e o preço da diária é {self.precoDiaria}")
        
    def calcularPrecoAluguel(self, dias):
        return self.precoDiaria * dias 
        