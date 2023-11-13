with open('banco.txt', 'w') as pasta:
  
    nota1 = float(input('Digite o primeiro número: '))
    nota2 = float(input('\nDigite o segundo número: '))
    nota3 = float(input('\nDigite o terceiro número: '))
    somar = (nota1 + nota2 + nota3)
    multiplicar = (nota1 * nota2 * nota3)

    print('\nEstes foram os três números digitados:\n1°:{:.2f}\n2°:{:.2f}\n3°:{:.2f}\n \nA soma dos números digitados é {:.1f}. A multiplicação, destes mesmos números, equivale a {:.1f}'.format(nota1, nota2, nota3, somar, multiplicar))

    pasta.writelines('\nNOTA1: {:.1f}'.format(nota1))

    pasta.writelines('\nNOTA2: {:.1f}'.format(nota2))

    pasta.writelines('\nNOTA3: {:.1f}'.format(nota3))

    pasta.writelines('\nSoma: {:.1f}'.format(somar))

    pasta.writelines('\nMultiplicação: {:.1f}'.format(multiplicar))

    pasta.close()

    opc = 0

    while opc != 2:

      print("\nDigite [1] PARA EXECUTAR")
      print("\nDigite [2] PARA SAIR ")

      opc = int(input("\n---Digite a opção: "))

      if opc == 1:
        with open('banco.txt', 'w') as past:
        
            nota1 = float(input('\nDigite o primeiro número: '))
            nota2 = float(input('\nDigite o segundo número: '))
            nota3 = float(input('\nDigite o terceiro número: '))
            somar = (nota1 + nota2 + nota3)
            multiplicar = (nota1 * nota2 * nota3)

            print('Estes foram os três números digitados:\n1°:{:.2f}\n2°:{:.1f}\n3°:{:.2f}\n A soma dos números digitados é {:.1f}.\n A multiplicação, destes mesmos números, equivale a {:.1f}'.format(nota1, nota2, nota3, somar, multiplicar))

            past.writelines('\nNOTA1: {:.1f}'.format(nota1))

            past.writelines('\nNOTA2: {:.1f}'.format(nota2))

            past.writelines('\nNOTA3: {:.1f}'.format(nota3))

            past.writelines('\nSoma: {:.1f}'.format(somar))

            past.writelines('\nMultiplicação: {:.1f}'.format(multiplicar))

            past.close()

      elif opc == 2:

        print("\nPrograma finalizado. Agradecemos a utilização ")
            


        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')