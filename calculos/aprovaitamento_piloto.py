'''
Comando: Crie um programa que gerencie o aproveitamento de um piloto de fórmula 1.
O programa deverá ler o nome do atleta e quantas pistas ele correu. Tendo o programa
armazenado estes dados, o próprio fará uma leitura das posições finais em cada race week. 
No final, tudo isso deverá ser guardado num dicionário, incluindo a melhor e a pior posição em cada race week.
'''
def champion_f1(): 
   #utilizar de dicionários 
    dados_piloto = {} 

    print("===" * 30)
    nome_piloto = input("\n\nDigite o nome do piloto = ")
    total_pistas = int(input("\nQuantas pistas o piloto correu = "))

    #armazenando as posições em cada race week
    dados_piloto["posicoes"] = []

    #loop para ler as posições em cada race week
    for semana in range(1, total_pistas + 1):
        posicao = int(input(f"digite a posição final na race week {semana}: "))
        dados_piloto["posicoes"].append(posicao)

    #adicionado o nome do piloto no dicionário
    dados_piloto["nome"] = nome_piloto
    
    #encontrar a melhor e a pior posição durante uma race week
    dados_piloto["melhor_posição"] = min(dados_piloto["posicoes"])
    dados_piloto["pior_posição"] = max(dados_piloto["posicoes"])

    # Calcula a média das posições
    media_posicoes = sum(dados_piloto["posicoes"]) / total_pistas

    # Calcula a porcentagem de vezes que o piloto ficou entre as três primeiras posições
    vezes_no_top3 = sum(1 for posicao in dados_piloto["posicoes"] if posicao <= 3)
    porcentagem_top3 = (vezes_no_top3 / total_pistas) * 100
    #exibindo os dados do piloto
    print("===" * 15)
    print("\n-Dados do piloto-")
    print("===" * 15)
    print(f"\n- Nome do piloto: {dados_piloto['nome']}")
    print(f"\n- Melhor posição: {dados_piloto['melhor_posição']}")
    print(f"\n- Pior posição: {dados_piloto['pior_posição']}")
    print(f"\n- Média de Posições: {media_posicoes:.2f}")
    print(f"\n- Porcentagem de vezes no Top 3: {porcentagem_top3:.2f}%")
    
    print(f"\n- Posições durante as race week: {dados_piloto['posicoes']}")

    # Retorna o dicionário com os dados do piloto
    return dados_piloto

projeto = champion_f1()
 