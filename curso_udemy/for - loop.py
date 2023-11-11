#Com Strings
palavra = 'google'

for c in 'google':
    print(f'{c} contém na palavra Google ' )

#Ciclos de repetição
'''
compra_confirmada = False
mens = 'Pagamento feito com sucesso'

for c in range(3):
    
    if compra_confirmada:
        print(f'\n{mens}. \n\nPróximo passo ')
        break
    else:
        print('Houve algum erro inesperado')
        break
'''

#Números
'''
for c in range(1, 20, 2):
    print(f'{c} ==number')
'''

#FOR loop nested (loop dentro de outro loop)
'''
for c in range(1, 6):
    print('Produto ' + str(c))
    for c2 in range(4):
        print(c, c2)
'''

#espaçando a frase numa mesma linha

word = 'Fantástico'

for c in word:
    print(f'  {c}', end='')
