''' 
Desenvolver um código-fonte que solicite dois inputs tipo string e daí vc digitará no prompt "desenvolvimento rápido de aplicações pyhton", dará um ENTER, e gravará em outra input "python na quinta", e que abra um arquivo banco2.txt no modo write,  e esse programa deve ter como saída:
#a) gravar as duas frases do enunciado no banco2.txt
#b) imprimir no prompt e uma de cada vez, as duas frases do enunciado sem os espaços vazios entre as palavras
#c) imprimir a primeira frase com o ponteiro a partir de "aplicações python" e gravar essa informação no banco2.txt
#d) contar quantas vezes a palavra "python" aparece no banco2.txt (count)
#e) imprimir as duas frases juntas no prompt fazendo uma concatenação (join)
'''

# Solicitar dois inputs tipo string
frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")

# Gravar as duas frases no banco2.txt
with open("banco2.txt", "w") as arquivo:
    arquivo.write(frase1 + "\n" + frase2)

# Imprimir as duas frases sem espaços vazios entre as palavras
print("Frase 1 sem espaços:", "".join(frase1.split()))
print("Frase 2 sem espaços:", "".join(frase2.split()))

# Imprimir a primeira frase a partir de "aplicações python"
indice_aplicacoes_python = frase1.find("aplicações python")
if indice_aplicacoes_python != -1:
    print("Frase 1 a partir de 'aplicações python':", frase1[indice_aplicacoes_python:])

# Contar quantas vezes a palavra "python" aparece no banco2.txt
with open("banco2.txt", "r") as arquivo:
    conteudo = arquivo.read()
    count_python = conteudo.lower().count("python")
    print("Quantidade de vezes que 'python' aparece no banco2.txt:", count_python)

# Imprimir as duas frases juntas fazendo uma concatenação
frases_concatenadas = frase1 + " " + frase2
print("Frases concatenadas:", frases_concatenadas)

