#          ==== ARGUMENTOS =====

#Passando, através da própria função, argumentos que fazem com que o código ali embutido possa ser personalizado

def boas_vindas(nome, quant):
    print(f'Olá, {nome}')
    
    print(f'Temos {quant} laptops em estoque')

#boas_vindas('Irineu', 8)

# Utilizando um número maior de argumentos onde, através do percorrimento do ciclo FOR Loop, foi possível realizar uma operação matemática junto aos números fora inseridos fora da função

#Atenção=tenha cuidado com o return
''' 
def soma(*num):
    res = 0
    for c in num: 
        res += c
    return res
    
z = soma(2, 3, 4, 6)
print(z)




def mult(*mul):
    res = 1
    for c in mul:
        res *= c
    return res
        
#x = mult(4, 6, 2)
#print(x)

#somando um asterístico a mais torna-se possível passar diversos paramêtros 
def agencia(**carro):
    return carro
    
print(agencia(linha='Gol', cor='Branca', motor=2.0, placa=1234))
print(agencia(linha='Honda', cor='Preto', motor=1.0))
print(agencia(linha='Mercedes', cor='Vermelho', motor=1.5, placa='85943'))
'''