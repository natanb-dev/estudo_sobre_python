#trabalhando com strings básicas no python

nome = str(input('Insira o seu nome: '))
idade = int(input(f'\nInsira a sua idade, {nome}: '))
city = 'São Paulo'
real = 2022 - idade

print(f'\n\n---Boa tarde, {nome}! Você nasceu no ano de {real} e, hoje, tem a idade'
      + ' de {idade} anos? Seria o seu local de nascimento {city}?')
