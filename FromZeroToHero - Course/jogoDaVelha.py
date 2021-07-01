def display(linha1, linha2, linha3):
    print(linha1)
    print(linha2)
    print(linha3)


def verificaseganhou(linha, posicao, linhaAux, linhaAux2, simbolo):

    if linha == linha1 and posicao == 1 or linha == linha1 and posicao == 3 or linha == linha3 and posicao == 1 or linha == linha3 and posicao == 3 or linha == linha2 and posicao == 2:
        if linha == linha1 and posicao == 1:
            if linha[posicao-1] == linhaAux[posicao] == linhaAux2[posicao+1]:
                print(f"{simbolo} Ganhou o jogo")
                exit()
        elif linha == linha1 and posicao == 3:
            if linha[posicao-1] == linhaAux[posicao-2] == linhaAux2[posicao-3]:
                print(f"{simbolo} Ganhou o jogo")
                exit()
        elif linha == linha3 and posicao == 1:
            if linha[posicao-1] == linhaAux[posicao+1] == linhaAux2[posicao]:
                print(f"{simbolo} Ganhou o jogo")
                exit()
        elif linha == linha3 and posicao == 3:
            if linha[posicao-1] == linhaAux[posicao-3] == linhaAux2[posicao-2]:
                print(f"{simbolo} Ganhou o jogo")
                exit()
        elif linha == linha2 and posicao == 2:
            if linha[posicao-1] == linhaAux[posicao-2] == linhaAux2[posicao]:
                print(f"{simbolo} Ganhou o jogo")
                exit()
            elif linha[posicao-1] == linhaAux[posicao] == linhaAux2[posicao-2]:
                print(f"{simbolo} Ganhou o jogo")
                exit()

    if posicao == 1:
        if linha[posicao-1] == linhaAux[posicao-1] == linhaAux2[posicao-1]:
            print(f"{simbolo} Ganhou o jogo")
            exit()
        elif linha[posicao-1] == linha[posicao] == linha[posicao+1]:
            print(f"{simbolo} Ganhou o jogo")
            exit()

    if posicao == 2:
        if linha[posicao-1] == linhaAux[posicao-1] == linhaAux2[posicao-1]:
            print(f"{simbolo} Ganhou o jogo")
            exit()
        elif linha[posicao-1] == linha[posicao-2] == linha[posicao]:
            print(f"{simbolo} Ganhou o jogo")
            exit()

    if posicao == 3:
        if linha[posicao-1] == linhaAux[posicao-1] == linhaAux2[posicao-1]:
            print(f"{simbolo} Ganhou o jogo")
            exit()
        elif linha[posicao-1] == linha[posicao-2] == linha[posicao-3]:
            print(f"{simbolo} Ganhou o jogo")
            exit()


i = 1
linha1 = ['', '', '']
linha2 = ['', '', '']
linha3 = ['', '', '']
numerosValidos = [1, 2, 3]
simbolosValidos = ['x', 'o']

print("x inicia a partida")
while i <= 9:

    if i%2!=0:
        simbolo = simbolosValidos[0]
    else:
        simbolo = simbolosValidos[1]

    linha = int(input("Digite a linha 1, 2 ou 3: "))
    while linha not in numerosValidos:
        linha = int(input("Digite a linha 1, 2 ou 3: "))

    posicao = int(input("Digite a posicao 1, 2 ou 3: "))
    while posicao not in numerosValidos:
        posicao = int(input("Digite a posicao 1, 2 ou 3: "))

    if linha == 1:
        linha1[int(posicao - 1)] = simbolo
        display(linha1, linha2, linha3)
        verificaseganhou(linha1, posicao, linha2, linha3, simbolo)

    elif linha == 2:
        linha2[int(posicao - 1)] = simbolo
        display(linha1, linha2, linha3)
        verificaseganhou(linha2, posicao, linha1, linha3, simbolo)

    elif linha == 3:
        linha3[int(posicao - 1)] = simbolo
        display(linha1, linha2, linha3)
        verificaseganhou(linha3, posicao, linha1, linha2, simbolo)

    i = i + 1
