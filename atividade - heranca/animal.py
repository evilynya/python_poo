class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def exibirInfo(self):
        print(f"Nome: {self._nome}, Idade: {self._idade}")

    def som(self, tipoSom):
        print(f"Este animal faz o som: {tipoSom}")


class Mamifero(Animal):
    def alimentarFilhotes(self):
        print(f"O mamífero: {self._nome} está alimentando seus filhotes.")


class Reptil(Animal):
    def mudarPele(self):
        print(f"O réptil: {self._nome} está trocando de pele.")
