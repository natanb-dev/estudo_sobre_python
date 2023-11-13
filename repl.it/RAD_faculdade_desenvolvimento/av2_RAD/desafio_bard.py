import sqlite3

# Função para calcular a média final
def calcular_media_final(notas):
    maiores_notas = []
    for nota in notas:
        if nota not in maiores_notas:
            maiores_notas.append(nota)
            if len(maiores_notas) == 3:
                break
    return sum(maiores_notas) / 3

# Função para imprimir o resultado
def imprimir_resultado(ra, nome, mf, aprovado):
    print("RA:", ra)
    print("Nome:", nome)
    print("Média final:", mf)
    if aprovado:
        print("Aprovado")
    else:
        print("Reprovado")

# Função para salvar as notas no banco de dados
def salvar_notas(notas):
    with sqlite3.connect("notas.db") as conexao:
        cursor = conexao.cursor()
        cursor.executemany("INSERT INTO notas VALUES (?, ?, ?, ?, ?, ?)", notas)
        conexao.commit()

# Função para recuperar as notas do banco de dados
def recuperar_notas():
    with sqlite3.connect("notas.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM notas")
        notas = cursor.fetchall()
    return notas

# Função para salvar as últimas notas em um arquivo TXT
def salvar_notas_txt(notas):
    with open("notas.txt", "w") as arquivo:
        for nota in notas:
            arquivo.write(str(nota) + "\n")

# Função principal
def main():
    notas = []
    while True:
        # Opções do menu
        print("1 - Iniciar/refazer")
        print("0 - Sair")
        opcao = int(input("Opção: "))

        # Iniciar/refazer
        if opcao == 1:
            notas = []
            for i in range(3):
                ra = input("RA: ")
                nome = input("Nome: ")
                notas.append([ra, nome, float(input("AV1: ")), float(input("AV2: ")), float(input("AV3: ")), float(input("AVD: ")), float(input("AVDS: "))])

            # Calcular a média final e imprimir o resultado
            mf = calcular_media_final(notas[i][2:])
            aprovado = mf >= 6 and notas[i][2:].count(4) >= 3
            imprimir_resultado(notas[i][0], notas[i][1], mf, aprovado)

            # Salvar as notas no banco de dados
            salvar_notas(notas)

            # Salvar as últimas notas em um arquivo TXT
            salvar_notas_txt(notas)

        # Sair
        elif opcao == 0:
            break

if __name__ == "__main__":
    main()
