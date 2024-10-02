from funcionario import Funcionario

funcionario1 = Funcionario("Gerente", 3000)
print("Seu cargo atual é: ",funcionario1.getCargo())

#tentando mudar o valor do atributo 
funcionario1.cargo = "Supervisor" #acessando o atributo direto 
funcionario1.setCargo("Engenheiro")  #acessando o método para mudar
print("Seu cargo atual é: ",funcionario1.getCargo())

#exibindo o salário 
print("O seu salário atual é" , funcionario1.salario)

funcionario1.salario = -100
print("O seu salário atual é ", funcionario1.salario)
