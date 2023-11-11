import sqlite3

def criar_tabela():
    # Conecta ao banco de dados SQLite e cria a tabela se não existir
    conexao = sqlite3.connect('notas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            ra INTEGER PRIMARY KEY,
            nome TEXT,
            av1 REAL,
            av2 REAL,
            av3 REAL,
            avd REAL,
            avds REAL
        )
    ''')
    conexao.commit()
    conexao.close()

def salvar_notas_banco(ra, nome, av1, av2, av3, avd, avds):
    # Salva as notas no banco de dados SQLite
    conexao = sqlite3.connect('notas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO alunos (ra, nome, av1, av2, av3, avd, avds)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (ra, nome, av1, av2, av3, avd, avds))
    conexao.commit()
    conexao.close()

def obter_ultimas_notas_arquivo():
    # Obtém as últimas notas salvas no arquivo TXT
    try:
        with open('ultimas_notas.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            return list(map(float, linhas))
    except FileNotFoundError:
        return None

def salvar_ultimas_notas_arquivo(av1, av2, av3, avd, avds):
    # Salva as últimas notas no arquivo TXT
    with open('ultimas_notas.txt', 'w') as arquivo:
        arquivo.write(f'{av1}\n{av2}\n{av3}\n{avd}\n{avds}')

def calcular_media_final(av1, av2, av3, avd, avds):
    # Calcula a Média Final (MF) conforme as regras especificadas
    notas = [av1, av2, av3]
    avd_avds = [avd, avds]

    # Pega as duas maiores notas entre AV1, AV2 e AV3
    duas_maiores_provas = sorted(notas)[-2:]

    # Pega a maior nota entre AVD e AVDS
    maior_avd_avds = max(avd_avds)

    # Calcula a Média Final
    media_final = (sum(duas_maiores_provas) + maior_avd_avds) / 3

    return media_final

def verificar_aprovacao(media_final):
    # Verifica se o aluno está aprovado ou reprovado
    if media_final >= 6 and all(nota >= 4 for nota in [av1, av2, av3, avd, avds]):
        return "Aprovado"
    else:
        return "Reprovado"

def iniciar_programa():
    while True:
        print("\nMenu:")
        print("[1] Iniciar/Refazer")
        print("[0] Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            ra = int(input("Digite o RA do aluno: "))
            nome = input("Digite o nome do aluno: ")

            # Obtém as últimas notas digitadas
            ultimas_notas = obter_ultimas_notas_arquivo()

            if ultimas_notas:
                av1, av2, av3, avd, avds = ultimas_notas
            else:
                av1 = float(input("Digite a nota da AV1: "))
                av2 = float(input("Digite a nota da AV2: "))
                av3 = float(input("Digite a nota da AV3: "))
                avd = float(input("Digite a nota da AVD: "))
                avds = float(input("Digite a nota da AVDS: "))

                # Salva as últimas notas digitadas
                salvar_ultimas_notas_arquivo(av1, av2, av3, avd, avds)

            # Calcula a Média Final
            media_final = calcular_media_final(av1, av2, av3, avd, avds)

            # Verifica a aprovação
            resultado = verificar_aprovacao(media_final)

            print(f"\nMédia Final: {media_final:.2f}")
            print(f"Resultado: {resultado}")

            # Salva as notas no banco de dados
            salvar_notas_banco(ra, nome, av1, av2, av3, avd, avds)

        elif opcao == '0':
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    # Cria a tabela no banco de dados
    criar_tabela()
    # Inicia o programa
    iniciar_programa()
