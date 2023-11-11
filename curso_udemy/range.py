'''
v = list()
v = int(input('valor:'))
# print('\n')
    #print(p)
#for p in range(v, 101)


for p in range(v, 101):
    print('\n\n------------\n\n')
    print(p)
''' 

#Ou também pode-se associá-lo a uma lista e aplicar o looping 

num = [x*1 for x in range(101)]
print(num)