import sqlite3 as conector

banko = input ("\nInsira o seu endereço: ")

conexao = conector.connect("bancoV.db")
cursor = conexao.cursor()

comando1 = "CREATE TABLE Cliente (id INTEGER NOT NULL, cpf INTEGER NOT NULL, nome TEXT NOT NULL, PRIMARY KEY (cpf));"

comando2 = "CREATE TABLE Pedido (id INTEGER NOT NULL,pedido INTEGER NOT NULL, alimento TEXT NOT NULL, endereco TEXT NOT NULL, PRIMARY KEY (pedido), FOREIGN KEY(alimento) REFERENCES Cliente (cpf));"

COMANDOinsert = "INSERT INTO Cliente (id, cpf, nome)VALUES (1, '52026492825', 'Natan barbosa')"

COMANDOinsertI = "INSERT INTO Pedido (id, alimento, endereco) VALUES (2, 'Arroz', 'AV. Paulista')"

comandoupdate = ("UPDATE Pedido SET endereco = ? WHERE id = 2")

cursor.execute(comando1)
cursor.execute(comando2)
cursor.execute(COMANDOinsert)
cursor.execute(COMANDOinsertI)
cursor.execute(comandoupdate,(banko,))
cursor.execute
conexao.commit()
cursor.close()
conexao.close()