class Servico:
    def __init__(self, pedido=0):
       self.__pedido = pedido

    def novoPedido(self):
        self.__pedido += 1

    def cancelarPedido(self):
        if self.__pedido <= 0:
            print("Não há pedidos para cancelar.")
        else:
            self.__pedido -= 1    

    def exibirPedido(self):
        return self.__pedido


