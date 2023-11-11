#Crie um programa que leia none, sexo e idade de várias pessoas, guardando os dados de cada uma dessas em um dicionário junto a uma lista. No final, mostre os seguintes requisitos:
#Quantas pessoas foram cadastradas
#A média de idade das pessoas
#Uma lista que contenha somente mulheres
#Uma lista com idade acima da média

#chave: a estrutura abaixo é uma lista que têm vários dicionários
galera = list()
pessoa = dict()
soma = mer = 0
while True:
    pessoa.clear
    pessoa['nome'] = str(input('\n\nNome: ')).upper()

    while True:
        pessoa['sexo'] = str(input('\nSexo: [M/F] ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas a letra M ou F.')
    pessoa['idade'] = int(input('\nIdade: '))
    soma += pessoa[
        'idade']  #esta linha faz com que a idade, estando essa enbutida num dicionário, seja passada para a variável 'soma' que irá, ao longo da segunda etapa, calcular a média de idade das pessoas
    galera.append(pessoa.copy(
    ))  #esta linha está passando uma cópia do dicionário para uma lista
    while True:
        resp = str(input(
            "\nQuer continuar? Digite S caso sim ou N caso não: ")).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda somente S ou N')
    if resp == 'N':
        break

print('=====' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas')
#essa função len reune todas as vezes que o programa rodou
mer = (soma / len(galera))
print(f'B) A média de idade é de {mer:5.2f} anos.')
print('C) Lista das pessoas com idade acima da média')

for p in galera:
    if p['idade'] >= mer:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()

print('D) Quais foram as mulheres digitadas: ')

for p in galera:
    if p['sexo'] in 'F':
        print(f'\n{p["nome"]}')

print('=========' * 30 + '\n\n<< ENCERRADO >>')
