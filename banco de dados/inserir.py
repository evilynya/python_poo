import sqlite3 #Importando uma biblioteca de banco de dados 

#Estabelecendo conexão com o banco
conexao = sqlite3.connect("departamento.db") #Estamos criando um arquivo que irá guardar o nosso bando de dados 

#Passo 2 - Verificar se a tabela existe ou não 
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT, 
    cargo VARCHAR(100)
);
"""
#Passo 3 - Acessar o objeto da biblioteca sqlite3 para manipular o banco 
consulta = conexao.cursor() #O objeto cursos() é responsável por manipular dados do banco 

#Passo 4 - Executar o comando de criação da tabela 
consulta.execute(tabela)

#Passo 5 - Solicitar dados 
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe  o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

#Passo 6 - Criando comando SQL para inserir os dados 
sql = "INSERT INTO funcionario VALUES(?,?,?,?)" #Colocamos ? no lugar dos dados reais, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca sqlite3

#Passo 7 - Organizar os dados que irão substituir a ? no comando sql para inserir os dados 
campos = (None, nome, salario, cargo) #Criando uma tupla com os dados que serão trocados pela ?. Ao informar o valor "None", estamos dizendo que será atribuido o valor padrão de AUTOINCREMENT

#Passo 8- Utilizar o objeto cursor()
consulta.execute(sql, campos)

#Passo 9 - Gravar os dados no banco 
conexao.commit()

print(consulta.rowcount, "linhas inseridas com sucesso")

#Passo 10 - Finalizar conexão 
conexao.close()
