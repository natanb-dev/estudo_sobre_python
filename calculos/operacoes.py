'''
Calculadora entre as operações: Soma, Subtração, Multiplicação, Media e Porcentagem

pontos:
     - o grande ponto deste app é que, realizando a operação, ele retorna para o looping

'''

def soma():
    print("===" * 15)
    num1 = float(input("n1: "))
    num2 = float(input("n2: "))
    resultado = num1 + num2
    print("===" * 15)
    print(f"\n>>>> A soma de {num1} e {num2} é: {resultado:.2f}")

def subtracao():
    print("===" * 15)
    num1 = float(input("n1: "))
    num2 = float(input("n2: "))
    print("===" * 15)
    resultado = num1 - num2
    print(f"A subtração de {num1} por {num2} é: {resultado:.2f}")

def multiplicacao():
    print("===" * 15)
    num1 = float(input("n1: "))
    num2 = float(input("n2: "))
    mult = (num1 * num2)
    print("===" * 15)
    print(f"A multiplicação entre {num1} e {num2} é: {mult:.2f}")

def media():
    print("===" * 15)
    num1 = float(input("n1: "))
    num2 = float(input("n2: "))
    media = (num1 + num2) / 2
    print("===" * 15)
    print(f"A média entre {num1} e {num2} é: {media:.2f}")

def porcentagem():
    print("===" * 15)
    valor_total = float(input("Digite o valor total: "))
    percentual = float(input("Digite a porcentagem a ser calculada: "))
    resultado = (percentual / 100) * valor_total
    print("===" * 15)
    print(f"{percentual:.2f}% de {valor_total:.2f} é: {resultado:.2f}")

def realizar_operacao():
    escolha = None

    while escolha != '9':
        
        print("\nSelecione a operação:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Media (/)")
        print("5. Porcentagem (%)")
        print("9. Sair")

        print("===" * 15)
        escolha = input("Digite o número da operação desejada: ")

        # Verifica a escolha do usuário e chama a função equivalente
        if escolha == "1":
            soma()
        elif escolha == "2":
            subtracao()
        elif escolha == "3":
            multiplicacao()
        elif escolha == "4":
            media()
        elif escolha == "5":
            porcentagem()
        elif escolha == '9':
            print("Programa encerrado. Agradeço a utilização")
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")

# Chamando o loop de escolha das funções
realizar_operacao()