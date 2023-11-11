'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado

mas e quanto a uma calculadora onde você ṕoderá decidir qual operação realizar?
'''
def media():
    print("==" * 15)
    print("\n Calculadora de média\n")
    nota1 = float(input("n1 =  "))
    nota2 = float(input("n2 = "))
    print("==" * 15)
    media = (nota1 + nota2) / 2

    if media < 5.0:
        print("Reprovado | sua nota foi {}".format(media))
        print("==" * 15)
    elif media <= 6.9:
        print("Recuperação | sua nota foi {}".format(media))
        print("==" * 15)
    else:
        print("Aprovado")
        print("==" * 15)

def soma():

    n1=float(input("n1: "))
    n2=float(input("n2: "))
    soma=n1+n2
    print("\nO resultado é {}".format(soma))

def subt():
    n1=float(input("n1= "))
    n2=float(input("n2= "))
    sub = (n1 - n2)
    print("o resultado da subtração é {}".format(sub))
''' 
def divi():
    n1=float(input("n1: "))
    n2=float(input("n2="))

#if __name__ == "__main__":
'''    

leia = media(), soma(), subt()
