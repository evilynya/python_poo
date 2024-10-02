class Funcionario:
    def __init__(self, cargo, salario=2000):
        self.__cargo = cargo
        self.salario = salario #esse trabalho está opcional, caso não seja informado outro valor será atribuido o valor padrão de R$2000
    
    def getCargo(self):
        return self.__cargo
    
    def setCargo(self, novoCargo):
        self.__cargo = novoCargo

#IREMOS UTILIZAR UMA FORMA ÚNICA DO PYTHON PARA ACESSAR OS ATRIBUTOS PRIVADOS
# Criando o 'get' do salário     
    @property
    def salario(self, valor):
        self.__salario = valor
    
    @salario.setter #irá criar um set para o salário mais amigável
    def salario(self, valor):
        if valor <= 0 :
            print("Informe um valor positivo")
        else:
            self.__salario = valor