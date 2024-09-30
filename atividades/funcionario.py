class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirDados(self):
        print(f"Olá {self.nome} ,seu cargo é {self.cargo} e seu salário é R${self.salario}")
        
    def verificaSalario(self):
        if self.salario <= 2000:
            print(f"{self.nome}:tem direito a bônus")
        else:
            print(f"{self.nome}:não tem direito a bônus") 
