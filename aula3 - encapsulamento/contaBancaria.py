class Conta:
    #método construtor 
    def __init__(self, numero, titular, saldo, limite = 200):
        #quando colocamos 2 underline antes do nome do atributo, indicamos que esse atributo está com a visibilidade "privado", o contrário siginifica que está "público"
        self.__numero = numero 
        self.__titular = titular
        self.__saldo = saldo 
        self.__limite = limite 
    
    #criando os demais métodos
    def detalhes(self):
        print(f"Olá {self.__titular}, seu saldo atual é {self.__saldo}")
    
    #método que irá retornar o conteúdo do limte 
    def getLimite(self):
        return self.__limite 
    
    #método que irá alterar o valor do limite
    def setLimite(self, valor):
        if valor < 0:
            print("Informe um valor positivo para o limite")
        else:
            self.__limite = valor
    
    #criando método que para depositar valor 
    def depositar(self, valor):
        if valor < 0:
            print("Informe um valor maior que zero")
        else: 
            self.__saldo = self.__saldo + valor
    
    #criar método para sacar valor 
    def sacar(self, valor):
        if self.__saldo <= 0 or valor > self.__saldo:
            print("Saldo insuficiente")
        else:
            self.__saldo = self.__saldo - valor