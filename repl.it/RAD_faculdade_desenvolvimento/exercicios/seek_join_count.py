frase1 = input(str("Digite a primeira frase: "))
frase2 = input(str("Digite a segunda frase: "))

#Armazenando as variaveis no objeto arquivo
arquivo = open ("Teste.txt", "w")
arquivo.write(frase1 + '\n')
arquivo.write(frase2)
arquivo.close()

print("----------------------------------------")

#Abrindo o arquivo em modo leitura sem espaçamento
with open ("Teste.txt", "r") as arquivo:
  
  for frase in arquivo:    
    frase_limpa = frase.strip()
    print(repr(frase_limpa))
    
  #Ponteiro seek
  arquivo.seek(0, 2)
  conteudo = arquivo.readline()
  unico_conteudo = conteudo.strip()
  print("----------------------------------------")
  print(repr(unico_conteudo))

#Acrescentando a palavra python no arquivo
arquivo = open("Teste.txt","a")
arquivo.write('\n'+ unico_conteudo)
arquivo.close()

#contador 
with open ("Teste.txt", "r") as arquivo:
  texto = arquivo.read()
  contador = texto.count("python")
  print("Quantas palavras python existe no arquivo? ", contador)
  
meu_texto = [frase1, frase2]
texto = ' ' .join(meu_texto)

with open ("Teste.txt", "r") as arquivo_reab:
  print(repr(texto))