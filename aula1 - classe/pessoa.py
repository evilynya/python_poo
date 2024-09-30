class Pessoa:
    #atributos 
    nome = "evilyn"
    idade = 18
    altura = 1.68

    #métodos - são os comportamentos da classe
    def falar(self,texto):
        print(f"Teho algo para te falar: {texto}")
    # self é um parâmetro obrigatório do python que informa que o método pertence à própria classe que foi criada 

#CRIANDO OBJETOS
pessoal = Pessoa() #dessa forma estamos criando um objeto do tipo pessoa

print(pessoal.nome, pessoal.idade)
pessoal.falar("Bom dia, hoje é segunda-feira")