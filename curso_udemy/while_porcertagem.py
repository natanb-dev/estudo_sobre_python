#Tarefa: publicar um produto com comissão de 10% o valor inicial da mercadoria

valor = int(input('Digite o valor da venda em R$: '))

while valor >= 20:
    valor1 = (valor * 0.10) + valor
    print(f'O valor final do produto é {valor1}')
    break
