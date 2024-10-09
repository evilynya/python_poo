class Pessoa: #superclasse ou classe mãe
    def  __init__(self, nome, idade):
        self._nome = nome 
        self._idade = idade
    
    def info(self):
        print(f"Nome: {self._nome}. Idade: {self._idade}")

#classe filha 1 - Aluno 
class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self._serie = serie
    
    def estudar(self):
        print(f"O aluno {self._nome} está estudando na série {self._serie}")

#classe filha 2 - Professor 
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def ensinar(self):
        print(f"{self._nome}, professor da disciplina {self._disciplina}, está ensinando")