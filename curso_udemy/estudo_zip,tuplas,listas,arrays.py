#Criando uma lista onde cada elemento toma-se vez com um index
'''
var = list('NATAN')
print(var)


#agregando/associando duas listas com o zip 
color = ['Paraná', 'Santa Catarina', 'Rio Grande do Sul']
num = ['PR', 'SC', 'RS']

dupla = zip(color, num)

print(list(dupla))

 
#input em uma lista

#-Objetivo: Criar uma lista de estados brasileiros a partir do input
#fornecido pelo usuário

states_usuario = input('Digite o nome dos estados separados por vírgula:')

states_lista = states_usuario.split(', ')

print('As informações da lista são, respectivamente ', states_lista)


 
    (Tuplas)
    
        --Armazenas mais de uma informação numa mesma variável
        --Mantém a sequência dos dados de uma variável
        --As inserções não podem serem alteradas (immutable)
        

'''
colors_list = ('yellow', 'red', 'blue')

from array import array

    #(Arrays)
        
        #--Ao ter uma lista com diversos itens, torna-se preciso 
        #--converter esta para um Array
        #--Além do primeiro argumento, usa-se muito array quando prefere-se
        #--aumento de performance
        
        

''' 
#letra = 'n,a,t,a,n'
letra = input('Nome= ')
l = ['n', 'a', 't']
num = [10, 29, 80, 65]
for c in letra:
    
    var = str(print(f',{c}', end=''))
    break
split_letra = letra.split(' ')

l = array('u', ['n', 'a', 't'])
num = array('i', [10, 29, 80, 65])
print('\n\n')

print(l, num)
'''
