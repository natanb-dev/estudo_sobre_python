# Enunciado da questão restruturado pelas IA

## Bard:
**Reconstrução do enunciado**

O enunciado do projeto pode ser reconstruído da seguinte forma para ficar mais claro e com os detalhes definidos mais claros:

**Objetivo do projeto**

O objetivo do projeto é desenvolver um programa em Python que calcule a média final de 3 alunos, considerando as notas das seguintes avaliações: AV1, AV2, AV3, AVD e AVDS.

**Requisitos funcionais**

* O programa deve solicitar as seguintes informações para cada aluno: RA, nome, notas das 5 avaliações.
* O programa deve calcular a média final pegando as 2 maiores notas entre AV1, AV2 e AV3 e a maior nota entre AVD e AVDS.
* O programa deve confirmar a aprovação ou reprovação do aluno, com base na seguinte regra:
    * MF >= 6 e todas as 3 notas consideradas >= 4: aprovado
    * MF < 6 ou alguma nota considerada < 4: reprovado
* O programa deve salvar as notas de todos os alunos em um banco de dados.
* O programa deve ser capaz de recuperar as notas do banco de dados para iterações com o programa.
* O programa deve salvar as últimas notas digitadas em um arquivo TXT.

**Requisitos não funcionais**

* O programa deve ser implementado em Python.
* O programa deve ser eficiente, utilizando algoritmos e estruturas de dados apropriadas.
* O programa deve ser fácil de usar, com uma interface clara e intuitiva.

**Detalhes adicionais**

* Para calcular as 2 maiores notas entre AV1, AV2 e AV3, o programa pode utilizar a seguinte lógica:

```python
maiores_notas = []
for nota in notas:
    if nota not in maiores_notas:
        maiores_notas.append(nota)
        if len(maiores_notas) == 2:
            break
```

* Para calcular a maior nota entre AVD e AVDS, o programa pode utilizar a seguinte lógica:

```python
maior_nota = notas[0]
for nota in notas[1:]:
    if nota > maior_nota:
        maior_nota = nota
```

* Para salvar as notas no banco de dados, o programa pode utilizar a seguinte instrução:

```python
with sqlite3.connect("notas.db") as conexao:
    cursor = conexao.cursor()
    cursor.executemany("INSERT INTO notas VALUES (?, ?, ?, ?, ?, ?)", notas)
    conexao.commit()
```

* Para recuperar as notas do banco de dados, o programa pode utilizar a seguinte instrução:

```python
notas = recuperar_notas()
```

* Para salvar as últimas notas em um arquivo TXT, o programa pode utilizar a seguinte instrução:

```python
with open("notas.txt", "w") as arquivo:
    for nota in notas:
        arquivo.write(str(nota) + "\n")
```

## Chatgpt:

Vamos reformular o enunciado para torná-lo mais claro e detalhado:

### Projeto de Controle de Notas de Alunos

#### Descrição Geral:

Desenvolva um programa em Python que permita o registro e controle das notas de alunos, realizando o cálculo da Média Final (MF) com base em critérios específicos. O programa deve oferecer funcionalidades como entrada de dados, cálculos, armazenamento em banco de dados e manipulação de notas.

#### Funcionalidades:

1. **Entrada de Dados:**
   - Solicitar o Registro Acadêmico (RA) e nome de 3 alunos.
   - Para cada aluno, solicitar as notas de 5 avaliações: AV1, AV2, AV3, AVD e AVDS, utilizando a função `input()` para receber as informações do usuário.

2. **Cálculo da Média Final (MF):**
   - Calcular a Média Final (MF) para cada aluno considerando as duas maiores notas entre AV1, AV2 e AV3, e a maior entre AVD e AVDS.
   - A fórmula para a MF é: `(AV1 + AV2 + AV3) / 3`, onde AV1, AV2 e AV3 são as duas maiores notas entre as três, e `(AVD + AVDS) / 2` para a avaliação dissertativa.

3. **Verificação de Aprovação:**
   - Verificar se a MF é maior ou igual a 6.
   - Se MF for maior ou igual a 6 e todas as notas (AV1, AV2, AV3, AVD e AVDS) forem maiores ou iguais a 4, exibir a mensagem "Aprovado".
   - Caso contrário, exibir a mensagem "Reprovado".

4. **Armazenamento em Banco de Dados:**
   - Utilizar um banco de dados SQLite para armazenar as notas dos alunos. Criar uma tabela para armazenar RA, nome e as notas das avaliações.

5. **Menu de Opções:**
   - Implementar um menu com as seguintes opções:
     - [1] Iniciar/Refazer: Permite o usuário inserir ou refazer as notas dos alunos.
     - [0] Sair: Encerra o programa.

6. **Salvamento das Últimas Notas em Arquivo TXT:**
   - Salvar as últimas notas digitadas em um arquivo TXT.
   - Garantir que o arquivo armazene apenas as notas mais recentes, descartando entradas anteriores.

#### Observações:

- Utilizar estruturas de controle (como if-else) para determinar as maiores notas.
- As notas devem ser salvas no banco de dados SQLite para permitir persistência e recuperação de dados entre execuções do programa.
- Implementar mecanismos para lidar com exceções e entradas inválidas.
- Garantir a modularidade do código, criando funções para diferentes etapas do processo.

Esta descrição detalhada fornece uma visão clara do projeto, destacando cada funcionalidade e a lógica por trás delas. Isso facilita a implementação do código, a compreensão do projeto e a manutenção futura.




