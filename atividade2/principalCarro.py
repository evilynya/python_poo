from carro import Carro

carro1 = Carro("Audi", "A5 Sportback", 2023, 200.00)
carro2 = Carro("Bentley", "Continental GT", 2021, 270.00)

carro1.exibirDetalhes()
dias1 = 12
preco1 = carro1.calcularPrecoAluguel(dias1)
print(f"Custo do aluguel para {dias1} dias: R$ {preco1:.2f}\n")

carro2.exibirDetalhes()
dias2 = 15
preco2 = carro2.calcularPrecoAluguel(dias2)
print(f"Custo do aluguel para {dias2} dias: R$ {preco2:.2f}")
