''' Dicionários
            Utilizam index no formato de Keys e Values
            Aceitam string, integer, float, boolean'''

#Já dentro dos {}, temos, respectivamente, chaves e, após os dois pontos, temos os valores que as compõem
aluno = dict()

aluno = {'Nome': 'Ana', 'Idade': '23', 'Nota_final': '7', 'Aprovação': True}
#print(f'As informações são == {aluno}')

while True:

    aluno = {'Nome': 'Ana', 'Idade': '23', 'Nota_final': '7', 'Aprovação': True}
    aluno['Sexo'] = str(input('Digite o sexo: ')).upper()
    
    if aluno['Sexo'] in 'MF':
        break
    print('Erro!!!!')

    print(aluno)
    break
#Caso queira puxar somente uma informação, basta especificar a chave dentro dos []

#print('O nome da tal garota é: ' + aluno['Nome'])


#Com o get é possível retornar um valor específico, assim como print anterior, porém, já que este é uma nova função, o GET também printa na tela o que for específicado após a vírgula caso a chave não esteja contida no dicionário. Siga os exemplos abaixo.

#print('\n' + aluno.get('Nome', 'Nothing'))
#print('\n' + aluno.get('endereco', 'Nothing'))

#Adicionando e atualizando valores dentro de um Dicionário
#Caso queira atualizar, basta digitar a chave específica e o valor atualizado; agora, caso queira adicionar uma nova chave, bastar digitar a nova chave

aluno['Nome'] = 'josé'
#aluno.update({'nome': 'Jose', 'Idade': '43'})

#Deletando itens de uma lista

#del aluno['Aprovação']

#Looping dentro de um dicionário

# Vizualizando os valores em tuplas
#for c in aluno.items():

#Vizualizando os valores fora das tuplas
#for keys, values in aluno.items():
    #print(keys, values)

#Prints específicos como, por exemplo, de apenas chaves ou valores:

#print(aluno.keys())
#print(aluno.values())