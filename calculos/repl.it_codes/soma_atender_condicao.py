''' 
Crie um programa que leia vários números inteiros pelo teclado.
O programa só irá parar quando o usuário digitar 999 - que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles
'''
 
n1 = soma = cont = 0

while True:

    n1 = int(input('Digite o valor: (digite 999 para parar): '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'\n\n\nForam digitados {cont} vezes e o resultado da soma foi {soma} ')
