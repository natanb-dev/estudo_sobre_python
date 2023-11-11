from datetime import datetime
'''
Python object-oriented programming


#Classes
    Utilizadas para criar objetos (instances)
    Objetos são parte dentro de uma class (instacias)
    Classes são utilizadas para agrupar dados e funções
    podendo reutilizá-las
    #Class: frutas
    #Objects: Abacaxi, Maça...
'''


class Func:
    #pass #este comando torna a classe vazia
    def __init__(self, nome, sobrenome, nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = nascimento

    def nome_com(self):
        return self.nome + ' ' + self.sobrenome

    def idade(self):
        ano = datetime.now().year
        self.nascimento = str(ano - self.nascimento)
        return self.nascimento
        '''cont = int(2022 - self.nascimento)
        return cont '''


#Criando objeto
usu_1 = Func('Helena', "Carla", 2001)
usu_2 = Func('CArka', "FErreira", 1995)

#print(usu_1.nome, usu_1.sobrenome)
#print(usu_1.nome + ' ' +usu_1.sobrenome)

#print(usu_1.nome_com())
print(Func.nome_com(usu_1) + '; idade: ' + Func.idade(usu_1))
