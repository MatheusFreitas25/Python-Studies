def display(linha1, linha2, linha3):
    print(linha1)
    print(linha2)
    print(linha3)


def verificaseganhou(linha, linhaAux, linhaAux2):

    if linha == linha1:
        if linha[0] == linha[1] == linha[2] or linha[0] == linhaAux[0] == linhaAux2[0] or linha[0] == linhaAux[1] == linhaAux2[2]:
            print("GANHOU O JOGO")

    elif linha == linha2:
        if linha[0] == linhaAux[0] == linhaAux2[0] or linha[0] == linha[1] == linha[2]:
             print("GANHOU O JOGO")

    elif linha == linha3:
        if linha[0] == linhaAux2[0] == linhaAux[0] or linha[0] == linha[1] == linha[2] or linha[0] == linhaAux2[1] == linhaAux[2]:
             print("GANHOU O JOGO")


i = 0
linha1 = ['', '', '']
linha2 = ['', '', '']
linha3 = ['', '', '']
numerosValidos = [1,2,3]
simbolosValidos = ['X', 'O']

while i <= 9:

    simbolo = input("Digite X ou O: ")
    while simbolo not in simbolosValidos:
        simbolo = input("Digite X ou O: ")

    linha = int(input("Digite a linha: "))
    while linha not in numerosValidos:
        linha = int(input("Digite a linha: "))

    posicao = int(input("Digite a posicao 1, 2 ou 3: "))
    while posicao not in numerosValidos:
        posicao = int(input("Digite a posicao 1, 2 ou 3: "))

    if linha == 1:
        linha1[int(posicao - 1)] = simbolo
        verificaseganhou(linha1, linha2, linha3)
    elif linha == 2:
        linha2[int(posicao - 1)] = simbolo
        verificaseganhou(linha2, linha1, linha3)
    elif linha == 3:
        linha3[int(posicao - 1)] = simbolo
        verificaseganhou(linha3, linha1, linha2)
    display(linha1, linha2, linha3)
    i = i + 1
