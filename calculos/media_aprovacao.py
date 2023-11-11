'''
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- média abaixo de 5.0: reprovado
- média entre 5.0 e 6,9: recuperação
- média 7.0 ou superior: aprovado

'''
def media():
    print("==" * 15)
    print("\n Calculadora de média\n")
    nota1 = float(input("n1 =  "))
    nota2 = float(input("n2 = "))
    print("==" * 15)
    media = (nota1 + nota2) / 2

    if media < 5.0:
        print(f"Reprovado | sua nota foi {media}")
        print("==" * 15)
    elif media <= 5.9:
        print(f"Recuperação | sua nota foi {media}")
        print("==" * 15)
    else:
        print("Aprovado")
        print("==" * 15)

if __name__ == "__main__": media()    
