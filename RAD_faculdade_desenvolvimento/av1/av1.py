'''
Desenvolva um código em Python para cadastrar carros de moradores de um prédio, registrando o nome, número do apartamento e placa do veículo em um arquivo TXT (por exemplo, Fulano de Tal, Apto XXX, Placa ABC1234).

Objetivos específicos:

1. Solicitar o nome do morador.
2. Solicitar o número do apartamento.
3. Solicitar a placa do veículo.
4. Solicitar uma letra minúscula como entrada.
5. Implementar um menu de opções com as seguintes escolhas:
   - [1] Cadastrar outro morador
   - [2] Sair
6. Em cada iteração, gravar os dados (nome, número do apartamento e placa) em um arquivo TXT sem perder as informações já registradas.
7. Na cada iteração, imprimir a frase: "Morador [NOME] mora no apto [APTO] possui veículo de placa [PLACA]", usando os dados da iteração atual.
8. Imprimir todo o conteúdo do banco de dados a cada iteração para confirmar a presença dos dados.
9. Contar e imprimir quantas vezes a letra solicitada no item 4 apareceu no banco de dados em cada iteração.
10. Bônus: Utilizar o método `with` ao manipular o arquivo para um acréscimo de 5% na nota do código.
11. Atenção: Não gravar o arquivo se a letra minúscula for 'F'
'''
def cadastrar_morador():
    nome = input("Digite o nome do morador: ")
    apto = input("Digite o número do apartamento: ")
    placa = input("Digite a placa do veículo: ")
    return nome, apto, placa

def imprimir_dados(nome, apto, placa, letra):
    print(f"Morador {nome} mora no apto {apto} possui veículo de placa {placa}.")
    print(f"Letra '{letra}' apareceu {placa.lower().count(letra)} vezes no banco de dados.")

def gravar_no_arquivo(nome, apto, placa, letra):
    with open("banco_dados.txt", "a") as arquivo:
        arquivo.write(f"{nome}, Apto {apto}, Placa {placa}\n")

def imprimir_banco_de_dados():
    with open("banco_dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print("Banco de Dados:")
        print(conteudo)

def main():
    letra = input("Digite uma letra minúscula: ")

    nome, apto, placa = cadastrar_morador()
    gravar_no_arquivo(nome, apto, placa, letra)
    imprimir_dados(nome, apto, placa, letra)
    imprimir_banco_de_dados()

    while True:
        opcao = input("\n[1] Cadastrar outro morador\n[2] Sair\nEscolha uma opção: ")

        if opcao == "1":
            nome, apto, placa = cadastrar_morador()
            gravar_no_arquivo(nome, apto, placa, letra)
            imprimir_dados(nome, apto, placa, letra)
            imprimir_banco_de_dados()
        elif opcao == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
