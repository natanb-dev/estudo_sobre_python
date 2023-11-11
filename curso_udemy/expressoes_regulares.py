import re

# 1. Buscar uma correspondência no início da string
pattern = re.compile(r'^\d+')
result = pattern.match('123abc')
print(result.group())  # Saída: 123

# 2. Buscar todas as correspondências na string
pattern = re.compile(r'\d+')
result = pattern.findall('A123B456C789')
print(result)  # Saída: ['123', '456', '789']

# 3. Substituir correspondências na string
pattern = re.compile(r'\d+')
result = pattern.sub('X', 'A123B456C789')
print(result)  # Saída: AXBXCX

# 4. Dividir a string com base em um padrão
pattern = re.compile(r'\s+')
result = pattern.split('Palavras Separadas Por Espacos')
print(result)  # Saída: ['Palavras', 'Separadas', 'Por', 'Espacos']

# 5. Encontrar todas as correspondências com grupos
pattern = re.compile(r'(\w+)-(\d+)')
result = pattern.findall('Item-123, Produto-456, Coisa-789')
print(result)  # Saída: [('Item', '123'), ('Produto', '456'), ('Coisa', '789')]

# 6. Verificar se uma string começa com um padrão
pattern = re.compile(r'^\d+')
result = pattern.match('123abc')
if result:
    print("A string começa com um número.")
else:
    print("A string não começa com um número.")

# 7. Ignorar maiúsculas/minúsculas durante a correspondência
pattern = re.compile(r'python', re.IGNORECASE)
result = pattern.match('Python é poderoso')
print(result.group())  # Saída: Python

# 8. Verificar se uma string termina com um padrão
pattern = re.compile(r'\d+$')
result = pattern.search('abc123')
if result:
    print("A string termina com um número.")
else:
    print("A string não termina com um número.")
