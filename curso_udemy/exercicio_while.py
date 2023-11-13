def data_nasci():
    opc = 0
    nome = str(input('Nome= '))
    idade = int(input('Idade= '))
    cont = 2023 - idade

    while (opc != 2):

        
        print(
            '-----' *40
        )
        print(f'\n Olá, {nome}! Você nasceu no ano de {cont} \nCaso vc queirar saber o seu atual momento de vida, siga as instruções abaixo para tal')
        print('====' * 30 +
              '\nDigite para continuarmos {1} ou para sairmos {2}')
        opc = int(input('\nDigite a opção: '))

        if opc == 1:
            print('=====' * 30 + '\n\nVocê é bem corajoso(a)')

            if cont >= 18:
                print('-----' * 30 +
                      f'\nVocê já pode ser preso, seu merda, {nome}')
            elif cont >= 60:
                print('-----' * 30 + f'\nSe aposente, {nome}')
            elif cont <= 17:
                print('------' * 30 +
                      f'Você nem poderia estar usando este programa, {nome}')

        elif opc == 2:
            print('Programa terminado')
            break


data_nasci()
