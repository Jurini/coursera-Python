def campeonato():
    usuario = 0
    computador = 0

    rodada = 1

    for i in range(1, 4):

        print(" ")
        print("****** Rodada", i, "******")
        print(" ")

        vencedor = partida()

        if (vencedor == 1):
            usuario += 1
        else:
            computador += 1

            print("Placar final: Você", usuario, "X", computador, "Computador")


def usuario_escolhe_jogada(n, m):
    print("Sua vez!")

    jogada = 0

    while jogada == 0:
        jogada = int(input("Quantas peças irá tirar?: "))

        if jogada > n or jogada < 1 or jogada > m:
            jogada = 0

    return jogada


def computador_escolhe_jogada(n, m):
    print("Vez do computador")

    if n <= m:
        return n

    else:
        quantia = n % (m + 1)

        if quantia > 0:
            return quantia

        return m


def partida():
    n = int(input("Quantas peças?: "))
    m = int(input("Qual o limite de peças por jogada?: "))

    is_computer_turn = False

    if n % (m + 1) == 0:
        is_computer_turn = False
        print("Você começa")
    elif n % (m + 1) != 0:
        is_computer_turn = True
        print("Computador começa")

    while n > 0:

        if (is_computer_turn):
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador tirou", jogada, "peças")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            is_computer_turn = True
            print("Você tirou", jogada, "peças")

        n = n - jogada

        print("Restam apenas", n, "peça(s) no tabuleiro")

    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("Computador ganhou!")
        return 0


tipo_jogo = 0

print("Bem Vindo ao Jogo NIN! Escolha: ")
print(" ")
print("1 = Para jogar uma partida")
print("2 = Para jogar um campeonato")

while tipo_jogo == 0:

    tipo_jogo = int(input("Sua opçao: "))

    if tipo_jogo == 1:
        print("Você escolheu uma partida!")
        partida()
        break
    elif tipo_jogo == 2:
        print("Você escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opção inválida")
        tipo_jogo = 0