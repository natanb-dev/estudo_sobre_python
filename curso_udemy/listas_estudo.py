#Listas
    #Armazena mais de uma informação numa mesma variável
    #Mantém a sequência dos dados numa variável

#BIBLIOTECA=https://docs.python.org/3/tutorial/datastructures.html

estados = ['São Paulo', 'Paraná', 'Minas Gerais']

capitais = ['São Paulo', 'Curitiba', 'Belo Horizonte', 'Cuiabá', 'Campo Grande', 'Porto Velho', 'Boa Vista', 'Teresina', 'Macéio', 'Aracajú', 'Natal', 'Belém', 'São Luis', 'Recife', 'Fortaleza', 'Salvador']


#Associar os itens a variáveis
#iten1, iten2, iten3 = capitais

#lista com sublista
'''pólis = [['Massachucets', 'Ilinóis'], 'New York']

print(pólis[1])
'''
#caso queira alterar algum item
estados[2] = 'Espírito Santo'
capitais[2] = 'Vitória'

#                  =============                    =================

#Adicionar ao final da lista
#estados.append('Maranhão')

#Específicar o index da inserção do item
#estados.insert(4, 'Amapá')

#Retirar um item da lista
#estados.pop()

#Classificar os itens em ordem alfabética
#estados.sort()

#print('\n' + estados[2] + ' tem por capital ' + capitais[2])

#Queira adicionar uma lista a outra *torna-se preciso printar o nome desta variável que, no caso em questão, seria 'add'
add = estados + capitais


#==================        ======================

#Looping dentro de uma lista

val = ['Recife', 'Fortaleza', 'Salvador', 'Natal']

for c in val:
    print(f'{c} é um estado do nordeste brasileiro')