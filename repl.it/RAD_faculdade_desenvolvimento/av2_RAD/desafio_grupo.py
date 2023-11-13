import os 
import sqlite3 as conector
conexao = conector.connect("SQL_BANCO_ALUNOS.db")
cursor = conexao.cursor()

comandoAPAGA = "DROP TABLE Notas"
cursor.execute(comandoAPAGA)

FOLHA_SQL = "CREATE TABLE Notas (RA INTEGER NOT NULL, NOME TEXT NOT NULL, MaiorNota1 REAL NOT NULL, MaiorNota2 REAL NOT NULL, MaiorNota3 REAL NOT NULL, MEDIA REAL NOT NULL, PRIMARY KEY (RA));"
cursor.execute(FOLHA_SQL)

conexao.commit()
cursor.close()
conexao.close()

print('.....::::: A Calculadora de Médias foi iniciada :::::.....')

print('\n..........................................................')

RESP=int(1)
while (RESP==1):
  ESCREVER = open('TXT_BANCO_ALUNOS.txt', 'w')
  ESCREVER.writelines("")
  ESCREVER.close()
  RESP1=int(0)
  while (RESP1<=2):
    
    MaiorNota1=0
    MaiorNota2=0
    MaiorNota3=0
    MEDIA=0

    RA = int(input("\nDigite seu RA: "))
    NOME = str(input('\nDigite seu nome: '))
    AV1=float(input("\nNota AV1 = "))
    AV2=float(input("\nNota AV2 = "))
    AV3=float(input("\nNota AV3 = "))
    AVD=float(input("\nNota AVD = "))
    AVDs=float(input("\nNota AVDs = "))

    if ((AV1>=AV3) and (AV2>=AV3)):
      MaiorNota1=AV1
      MaiorNota2=AV2

    if ((AV2>=AV1) and (AV3>=AV1)): 
      MaiorNota1=AV2
      MaiorNota2=AV3

    if ((AV1>=AV2) and (AV3>=AV2)):
      MaiorNota1=AV1
      MaiorNota2=AV3

    if ((AVD>=AVDs)):
      MaiorNota3=AVD+0

    if ((AVD<AVDs)):
     MaiorNota3=AVDs+0

    if (MaiorNota1<=MaiorNota2):
      Variavel_transferencia=MaiorNota1+0
      MaiorNota1=MaiorNota2+0
      MaiorNota2=Variavel_transferencia+0
     
    MEDIA=((MaiorNota1+MaiorNota2+MaiorNota3)/3)


    if ((MEDIA>=6) and ((MaiorNota1>=4) and (MaiorNota2>=4) and (MaiorNota3>=4))):
      print('\n'+NOME,'você foi aprovado:\n1a Maior Nota Presencial = {:.2f}\n2a Maior Nota Presencial = {:.2f}\nMaior nota digital = {:.2f}\nMedia final = {:.2f}'.format(MaiorNota1, MaiorNota2, MaiorNota3, MEDIA))

    if ((MEDIA>=6) and ((MaiorNota1<4) or (MaiorNota2<4) or (MaiorNota3<4))):
      print('\n'+NOME,' você foi reprovado por ter alguma nota menor que 4:\n1a Maior Nota Presencial= {:.2f}\n2a Maior Nota Presencial = {:.2f}\nMaior nota digital = {:.2f}\nMedia final = {:.2f}'.format(MaiorNota1, MaiorNota2, MaiorNota3, MEDIA))

    if (MEDIA<6):
      print('\n'+NOME,' você foi reprovado por ter a media menor que 6:\n1a Maior Nota Presencial = {:.2f}\n2a Maior Nota Presencial = {:.2f}\nMaior nota digital = {:.2f}\nMedia final = {:.2f}'.format(MaiorNota1, MaiorNota2, MaiorNota3, MEDIA))

    print('\n..........................................................')

    LER = open('TXT_BANCO_ALUNOS.txt', 'r')
    BACKUP = LER.readlines()
    LER.close()

    ESCREVER = open('TXT_BANCO_ALUNOS.txt', 'w')
    ESCREVER.writelines(BACKUP)
    ESCREVER.writelines('Nome: '+NOME)
    ESCREVER.writelines('\nRA: '+str(RA))  
    ESCREVER.writelines('\n1a Maior Nota Presencial: {:.2f}'.format(MaiorNota1))
    ESCREVER.writelines('\n2a Maior Nota Presencial: {:.2f}'.format(MaiorNota2))
    ESCREVER.writelines('\nMaior Nota Digital: {:.2f}'.format(MaiorNota3))
    ESCREVER.writelines('\nMédia: {:.2f}\n\n'.format(MEDIA))
    ESCREVER.close()

    import sqlite3 as conector
    conexao = conector.connect("SQL_BANCO_ALUNOS.db")
    cursor = conexao.cursor()

    comandoINSERE1 = "INSERT INTO Notas (RA, NOME, MaiorNota1, MaiorNota2, MaiorNota3, MEDIA) VALUES (?,?,?,?,?,?);"
    cursor.execute(comandoINSERE1,(RA, NOME, '{:.2f}'.format(MaiorNota1), '{:.2f}'.format(MaiorNota2), '{:.2f}'.format(MaiorNota3), '{:.2f}'.format(MEDIA)))

    conexao.commit()
    cursor.close()
    conexao.close()

    RESP1=RESP1+1

  RESP=int(input("\nDeseja refazer a média?\nDigite 1 para SIM e 2 para NÃO:\n"))

print('\n.....:::::A Calculadora de Médias foi finalizada:::::.....')

os.system("pause")
