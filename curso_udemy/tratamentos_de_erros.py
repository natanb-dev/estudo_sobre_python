'''
    Tratamento de erros: try e except
        Excelente para testes
        Não realiza 'stop' no programa
        Mensagens customizadas de tratamento de erro onde, além de encontrar o erro, este não imperrar o programa, podendo, assim, pular para a próxima linha de código fora do try '''    


''' try:
    letra = ['a', 'b', 'c']
    print(letra[3])
except IndexError: #especificar o erro que será printado caso as linhas acimas sejam rodadas 
    
    print('O index não existe')
'''
try:
    val = int(input('Digite o valor do seu produto: '))
    print(val)
except ValueError:
    print('Favor digitar um valor em números inteiros.')
finally: #só usa-lo caso queira que a saída venha com ou sem erro por parte do usuário
    print('Código ok')

'''else:
    print('O usuário digitou o valor correto')
    resultado = val * 2
    print(resultado)
''' 