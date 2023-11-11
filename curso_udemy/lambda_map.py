''' 
Lambda Function
        È uma funcão (pequena) sem nome
        Função utilizada dentro de outras funções 
        Código mais 'Clean'
        Pode ter vários argumentos mas somente uma expressão 
'''
#fonte de uma lista com várias funções já contruídas:
#https://docs.python.org/3/library/functions.html

#Tornando o return útil
#def somar(x):
    #return x+5

#Fazendo a mesma saída acima só que utilizando a função Lambda 
somar = lambda x,y: x+y+10

print(somar(5, 5))

def somar(x):
    opc = lambda x: x+10
    return opc(x) *4


#print(somar(5))


'''Map Function
    Utilizado em listas
    Aplica uma função a um Iterable por item (list, tuple, dicionários, etc...) como se fosse um FOR
    '''

list1 = [2, 6, 4]

list2 = map(lambda x: x*2, list1)

#print(list(map(lambda x: x*2, list1)))

lambda x: x*4, list1

list5 = [5, 4]
print(list(map(lambda x: x*4, list5)))


''' Filter function
        Muito utilizado em listas [];
        Aplica-la a uma função que tenha iterable filtrando os itens (list, tuple, dict, etc...)
        Seu uso faz efeito quanto a funcionalidade a mais, dada pela função, que, em vez de retornar um valor booleano,
        como o próprio MAP faria, a função filter retorna especificamente número posto pela saída
    '''
valores = [13,12,19,25,40]

print(list(filter(lambda x: x > 20, valores)))