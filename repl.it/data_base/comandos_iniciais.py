import sqlite3 as conector
conexao = conector.connect("bancoII.db")
cursor = conexao.cursor()

comando1 = "CREATE TABLE Pessoa (cpf INTEGER NOT NULL, nome TEXT NOT NULL, nascimento DATE NOT NULL, oculos BOLLEAN NOT NULL, PRIMARY KEY (cpf));"

comando2 = "CREATE TABLE Marca (id INTEGER NOT NULL, nome TEXT NOT NULL, sigla CHARACTER(2) NOT NULL, PRIMARY KEY(id));"

comando3 = "CREATE TABLE Veiculo (placa CHARACTER(7) NOT NULL, ano INTEGER NOT NULL, cor TEXT NOT NULL, proprietario INTERGER NOT NULL, marca INTEGER NOT NULL, PRIMARY KEY (placa), FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf), FOREIGN KEY (marca) REFERENCES Marca (id));"

comandoINSERE = "INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (123456789, 'Aluno', '31-05-2021', 1);"

cursor.execute(comando1)
cursor.execute(comando2)
cursor.execute(comando3)
cursor.execute(comandoINSERE)
cursor.execute
conexao.commit()
cursor.close()
conexao.close()