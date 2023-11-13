import sqlite3 as conector
conexao = conector.connect("bancoIII.db")
cursor = conexao.cursor()

comando1 = "CREATE TABLE Aluno (cpf INTEGER NOT NULL, nome TEXT NOT NULL, endereço TEXT NOT NULL, PRIMARY KEY (cpf));"

comando2 = "CREATE TABLE Historico (ra INTEREGER NOT NULL, disciplina TEXT NOT NULL, professor TEXT NOT NULL, nota REAL NOT NULL, PRIMARY KEY (ra), FOREIGN KEY (ra) REFERENCES Aluno(cpf));"

comandoINSERT = "INSERT INTO Aluno (cpf, nome, endereço) VALUES (520264928, 'Natan Barbosa', 'Rua promotor Gabriel Netuzzi Perez');"

comandoINSERT_I = "INSERT INTO Aluno (cpf, nome, endereço) VALUES (520264978, 'Paul', 'Grajau');"

comandoINSERT_II = "INSERT INTO Historico (ra, disciplina, professor, nota) VALUES (202009002846, 'Matamática', 'Godoi', 5);"

comandoINSERT4 = "INSERT INTO Historico (ra, disciplina, professor, nota) VALUES (201905123456, 'ARA0095', 'Flávio', 9);"

comandodelete = ("DELETE FROM Historico WHERE ra = 201905123456 ");


cursor.execute(comando1)
cursor.execute(comando2)
cursor.execute(comandoINSERT)
cursor.execute(comandoINSERT_I)
cursor.execute(comandoINSERT_II)
cursor.execute(comandoINSERT4)
cursor.execute(comandodelete)
cursor.execute
conexao.commit()
cursor.close()
conexao.close()