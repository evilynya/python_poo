class Pessoa:
    #criando o método construtor 
    def __init__(self, nome, hobby, endereco):
        #estamos criando os atributos da classe utilizando o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como valores dos atirbutos
        self.nome = nome
        self.hobby = hobby
        self.endereco = endereco
    
    #criando os métodos normais 
    def exibirDados(self):
        print(f"Olá {self.nome} ,seu hobby é {self.hobby} e seu endereço é {self.endereco}")
    
#CRIANDO OS OBJETOS 
pessoa1 = Pessoa("Evilyn", "dança", "Rua 5 Cohab")
pessoa1.exibirDados() #chamando o método da classe

pessoa2 = Pessoa("Karla", "artes marciais", "Rua 10 Cohama")
print(pessoa2.nome)

    