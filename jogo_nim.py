def computador_escolhe_jogada(pecas, jogadas):
    if pecas == jogadas + 1:
        print('Voce começa')
    return pecas


def usuario_escolhe_jogada(pecas, jogadas):
    return pecas


def main():
    print('Bem-vindo ao jogo do NIM! Escolha:')
    escolha = int(input('1 - para jogar uma partida isolada''\n''2 - para jogar um campeonato''\n'':'))
    if escolha == 1:
        partida()
    else:
        campeonato()


def partida():
    pecas = int(input('Quantas peças? '))
    jogadas = int(input('Limite de peças por jogada? '))
    computador_escolhe_jogada(pecas, jogadas)
    usuario_escolhe_jogada(pecas, jogadas)


def campeonato():
    i = 0
    while i < 3:
        partida()
        i = i + 1


main()
