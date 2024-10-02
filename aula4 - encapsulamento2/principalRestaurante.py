from restaurante import Servico

servico = Servico(6)
print("O número de pedidos é: " ,servico.exibirPedido())

servico.novoPedido()
servico.novoPedido()
print("O novo número de pedidos é: ", servico.exibirPedido()) 

servico.cancelarPedido()
print("Pedido atual é: ", servico.exibirPedido())  

  


