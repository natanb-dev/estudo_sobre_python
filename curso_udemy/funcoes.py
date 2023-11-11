#Você pode muito bem criar uma função para um pedaço de código que resolva um problema, para que, em efeito, possa simplificar e tornar mais legível o seu código com um todo.
''' 
def calculo_nascimento():
    import datetime

    print('****Não insira o numeral zero ao especificar o mês')
    print('==' * 30)
    print('====' * 30 + '\nCalculadora de idade iniciada')
    nome = input("\n\nComo você se chama? ")
    ano = eval(input(f"Nasceu em qual ano, {nome}? "))
    mes = eval(input(f"Nasceu em qual mês, {nome}? "))
    dia = eval(input(f"Nasceu em qual dia, {nome}? "))
    ano_atual = eval(input("Ano atual? "))
    mes_atual = eval(input("Mês atual? "))
    dia_atual = eval(input("Dia atual? "))
    dataNasc = datetime.date(ano, mes, dia)
    dataAtual = datetime.date(ano_atual, mes_atual, dia_atual)

    #diferença retorna em timedelta
    diferenca = (dataAtual - dataNasc)
    #Cálculos e Resultados
    rslt = (diferenca.days / 365.25)
    #ano_atual-ano

    if (dia == dia_atual and mes == mes_atual):
        print(
            f'\n\nComo o(a) {nome} nasceu em {dia}/{mes}/{ano}, este tem a idade exata de {rslt} anos! '
        )
        print(
            'Ou, especificando de uma maneira melhor, ele(a) tem {:.1f} anos'.
            format(rslt))
    else:
        ((dia > dia_atual and mes == mes_atual) or mes < mes_atual)
        print(
            f'\n\nComo o(a) {nome} nasceu em {dia}/{mes}/{ano}, este tem a idade exata de {rslt} anos! '
        )
        print(
            'Ou, especificando de uma maneira melhor, ele(a) tem {:.1f} anos'.
            format(rslt))


calculo_nascimento()

'''
def fun_media():
    nome = str(input('Digite o seu nome: '))
    n1 = 15
    n2 = 30
    media = (n1 + n2) / 2
    print(f'Olá, {nome}! A soma dos números {n1} e {n2} resulta na média de {media}')
    if media < 30:
        print('Nota insuficiente')
    else:
        print(f'\nBoa, {nome}')

def amostrar():
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    res = 2022 - idade
    if res > 18:
        print(f'Você, {nome}, é sim maior de idade')
    elif res > 60:
        print(f'Você, {nome}, é uma pessoa idosa')
    else:
        print('Você é criança ainda')

amostrar()



#Passando, através da própria função, argumentos que fazem com que o código ali embutido possa ser personalizado


#Passando, através da própria função, argumentos que fazem com que o código ali embutido possa ser personalizado



