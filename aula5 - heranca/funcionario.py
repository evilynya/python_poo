class Pessoa: #superclasse ou classe-mãe
    def __init__(self, nome, cargo):
        #estamos mudando a visibilidade do atributo de privado para protegido, dessa forma as classes filhgas poderão acessar os atributos da classe mãe
        self._nome = nome
        self._cargo = cargo
    
    def informacoes(self):
        print(f"Olá {self._nome}, na empresa seu cargo é: {self._cargo}")
    
#criando classe filha 
class Engenheiro(Pessoa): #a classe Engenheiro está herdando as características da classe Pessoa, que será a classe mãe 
    def mostraDetalhes(self):
        print(f"Olá, meu nome é {self._nome} e eu sou engenheiro")

class Secretario(Pessoa): #a classe Engenheiro está herdando as características da classe Pessoa, que será a classe mãe 
    def relatorio(self):
        print(f"Olá, meu cargo é {self._cargo}")
