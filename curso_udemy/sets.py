'''
Set (listas sem duplicação)
        -Similar as listas   
        -Evita itens duplicados   
        -Não utiliza index'''

'''list1 = {10, 20, 30, 49, 69}
list2 = {10, 20, 30, 49}

num1 = set(list1)
num2 = set(list2)

print(num1|num2) #Union  
print(num1 - num2) #Difference
print(num1 ^ num2) #Symmetric Difference
print(num1 & num2)
#                          outra maneira
''' 

s1 = {15, 53}
s2 = {53, 45}


sy = s1.union(s2)

st = s1.difference(s2)

se = s1.intersection(s2) #junção daquilo que somente for igual 

s1.add(6)
s1.update([98, 7, 45])
s1.discard(6)
print(s1)
