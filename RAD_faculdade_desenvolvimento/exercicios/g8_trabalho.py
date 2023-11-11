nome = str(input('Digite seu nome: '))

av1 = float(input('\nPrimeira nota da avaliação: ')) 

av2 = float(input('\nSegunda nota da avaliação: '))

Media = (av1+av2)/2

print('\nSendo suas notas {:.2f} e {:.2f}, a média do\n aluno é {:.2f}.'.format(
    av1, av2, Media))

if Media > 5.99:
    print("\nSendo assim, o aluno está Aprovado")
elif Media <= 5.99:
    print("\nSendo assim, o aluno está Reprovado")
print('----------------------------------------------------------------------------------------')

write = open('Banco de Dados.txt', 'a+')
write.writelines(str(f'\nNOME={nome}'))
write.writelines(str(f'\nMÉDIA={Media}'))
write.close()


opc=0

while (opc != 3):

  print('\nLeia atentamente as opções abaixo e \nselecione qual lhe for necessário:')
  print("\nDigite [1] Refazer o Calculo ")
  print("\nDigite [2] Calcular a média de outro aluno ")
  print("\nDigite [3] Sair")
 
  opc = int(input("\nDigite a opção: "))
    
  if opc == 1: 
    print("_______________________________________")
    nome = str(input('Digite o seu nome: '))   
    av1 = float(input('\nPrimeira nota da avaliação: '))
    av2 = float(input('\nSegunda nota da avaliação: '))
    Media = (av1 + av2) / 2
    
    print('\n>>>Sendo suas notas {:.2f} e {:.2f}, a média do aluno é {:.2f}.'.format(av1, av2, Media))
    print("\n Consulte abaixo se você foi aprovado ou\n reprovado nesta disciplina ") 
    Write2 = open('Banco de Dados.txt', 'w')
    Write2.writelines(str(f'\n\nNOME{nome}'))
    Write2.writelines(str(f'\nMÉDIA={Media}'))
    Write2.close()
    
    if Media > 5.99:
        print("\nSendo assim, o aluno está >>Aprovado")
    elif Media <= 5.99:
        print("\nSendo assim, o aluno está>>Reprovado") 
    
    print('--------------------------------------------') 

  if opc == 2:
        print("_______________________________________")
        nome = str(input('Digite o seu nome: '))   
        av1 = float(input('\nPrimeira nota da avaliação: '))
        av2 = float(input('\nSegunda nota da avaliação: '))
        Media = (av1 + av2) / 2
        print('\n>>>Sendo suas notas {:.2f} e {:.2f}, a média do aluno é {:.2f}.'.format(av1, av2, Media))
        print("\n Consulte abaixo se você foi aprovado ou\n reprovado nesta disciplina ") 
        Write3 = open('Banco de Dados.txt', 'a+')
        Write3.writelines(str(f'\n\nNOME{nome}'))
        Write3.writelines(str(f'\nMÉDIA={Media}'))  
        Write3.close()
        
        if Media > 5.99:
            print("\nSendo assim, o aluno está >>Aprovado")
        elif Media <= 5.99:
            print("\nSendo assim, o aluno está>>Reprovado") 
              
        print('--------------------------------------------') 
        
  if opc == 3:
            print("\nPrograma finalizado. Agradecemos a\n utilização ")
  
  else:
      print("Opção inválida")

  print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')