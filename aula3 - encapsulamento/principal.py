from contaBancaria import Conta

minhaConta = Conta(123, "Silvano Salles", 1000, 500)

minhaConta.detalhes()

print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.setLimite(259) #alterando o valor do limite 

minhaConta.__limite = 2000

print(f"O limite atual é {minhaConta.getLimite()}")

minhaConta.depositar(100)
minhaConta.detalhes()

minhaConta.sacar(500)
minhaConta.detalhes()

