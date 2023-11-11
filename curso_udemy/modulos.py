from func import find_index
#from itens.cad import cada

#No advento de várias funções num mesmo código, é preferível utilizar as
#packages para uma organização e gestão melhor do código do que no main ou aglutinado em um
#mesmo file.
lista = ['a', 'b', 'c', 'd', 'e']

b = find_index(lista, 'u')
print(b)