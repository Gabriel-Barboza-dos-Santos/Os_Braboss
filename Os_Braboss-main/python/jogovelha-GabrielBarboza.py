def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def verificar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if linha.count(linha[0]) == len(linha) and linha[0] != " ":
            return True

    for coluna in range(len(tabuleiro[0])):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return True

    return False

def jogo_da_velha():
    tabuleiro = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]

    jogador = "X"
    jogadas = 0

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Informe a linha (0-2): "))
        coluna = int(input("Informe a coluna (0-2): "))

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            jogadas += 1

            if verificar_vencedor(tabuleiro):
                print("O mais Bebado", jogador, "venceu!")
                break
            elif jogadas == 9:
                print("Seis é mula!")
                break
            else:
                jogador = "O" if jogador == "X" else "X"
        else:
            print("Essa ja foi cabeçao tente outra")

jogo_da_velha()