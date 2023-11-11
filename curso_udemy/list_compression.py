''' List Comprehension
        Mais simples de se escrever
        Utilizado quando você precisa criar uma nova lista a partir de uma já existente 
        [expressão for item in items]
'''

frutas = ['Mamão', 'Banana', 'Maça']
def antiga():
    
    fruta2 = []
    for p in frutas:
        if 'M' in p:
            fruta2.append(p)
    print(fruta2)




#O uso desta lista além de economizar linhas, o que torna o código mais 'clean', define, de maneira clara,
# a variável que fará o looping, o próprio looping e, como não poderia faltar, a condição IF na mesma linha que a finaliza e dá pontos finais Coprehension
fru2 = [p for p in frutas if 'B' in p]

#gere 6 valore que obdeçam a um FOR que acrescente alguma uma porcentagem por rodagem
val = [x * 10 for x in range(6)]
print(val)