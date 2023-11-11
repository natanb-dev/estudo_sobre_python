import sqlite3 as conector

CPF = float(input("\nInsira seu cpf: "))
NOME = str(input("\nInsira seu Nome: "))
PEDIDO = int(input("\nNúmero do seu pedido: "))
ALIMENTO = str(input("\nInsira seu alimento: "))
ENDERECO = str(input("\nInsira seu endereço: "))


conexao = conector.connect("bancazo.db")
cursor = conexao.cursor()

comando1 = "CREATE TABLE Cliente (cpf INTEGER NOT NULL, nome TEXT NOT NULL, PRIMARY KEY (cpf));"
comando2 = "CREATE TABLE Pedido (pedido INTEGER NOT NULL, alimento TEXT NOT NULL, endereco TEXT NOT NULL, PRIMARY KEY (Pedido), FOREIGN KEY(alimento) REFERENCES Cliente (cpf));"

comandoinsert = "INSERT INTO Cliente (cpf, nome) VALUES (?,?)"

comandoinsertI = "INSERT INTO Pedido (pedido, alimento, endereco) VALUES (?,?,?)"


cursor.execute(comando1)
cursor.execute(comando2)
cursor.execute(comandoinsert,(CPF, NOME))
cursor.execute(comandoinsertI,(PEDIDO, ALIMENTO, ENDERECO))
cursor.execute
conexao.commit()
cursor.close()
conexao.close()