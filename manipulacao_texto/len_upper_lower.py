''' 
Aqui neste programa se encontram as maneiras simples de manipular uma string

Entre estes, estão como tornar maiusculas, minusculas e contar o total de letras de uma variável
'''

nome = str(input('Digite o seu nome: ')).strip()
print('\nAnalisando o seu nome... ')
#upper
print('\\nSeu nome em maísculas é {}'.format(nome.upper()))
#lower
print('\nSeu nome em minúsculo é {}'.format(nome.lower()))
#len
print('\nSeu nome tem ao todo {} letra(s)'.format(len(nome) - nome.count(' ')))
