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

#Passo 5 - Criar comando SQL para consultar os dados
sql = "SELECT * FROM funcionario"

#Passo 6- Executar o comando sql
consulta.execute(sql)

#Passo 7 - Eixbir dados do banco 
resultado = consulta.fetchall() # fetchall() irá trazer todos os registros que existem no banco de dados 

print(resultado)

print("-"*50)
for itens in resultado:
    print(f"Código: {itens[0]}, Nome: {itens[1]}")

#Passo 8 - Finalizar conexão 
conexao.close()