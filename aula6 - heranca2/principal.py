from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Getúlio", 65)
aluno1 = Aluno("Keila", 16, "2 ano do ensino médio")
professor1 = Professor("Fernando", 32, "Biologia")

pessoa1.info()

aluno1.info()
aluno1.estudar()

professor1.info()
professor1.ensinar()


