''' 
Generator expressions
        Uma forma mais rápida para listas, discionários e etc...
        Menos mómoria alocada
        Valores em bytes
        
        detalhes: A mudança se dá nas chaves da lista que, em vez de ser colchetes[],
        torna-se-ia parentêses().
        Para que isto funcione, torna-se expresso o uso do import da biblioteca logo abaixo
'''
from sys import getsizeof

num = [x*10 for x in range(10)]
print(type(num))
print(num)
print(getsizeof(num))

print('=' *20)
#exemplo  de fato
num2 = (y*10 for y in range(10))
print(type(num2))
print(getsizeof(num2))
