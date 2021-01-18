from Models.Jogo.Partida import Partida

partida = Partida("Um", "Dois")


def mostrar_tabuleiro(partida_atual):
    for index in range(8):
        linha = ""
        for i in partida_atual.tabuleiro.casas:
            coluna = " | "
            pedra = i[index].pedra
            if pedra is not None:
                coluna += pedra.name
            else:
                coluna += "   "
            linha += coluna
        print(linha)
    print("--------------------------------")



mostrar_tabuleiro(partida)

casas = partida.tabuleiro.casas

casas[6][3].pedra = casas[2][7].pedra
casas[2][7].pedra = None
casas[6][3].pedra.coordenada_x = 6
casas[6][3].pedra.coordenada_y = 3
casas[6][3].pedra.atualizar_possiveis_destinos(partida.tabuleiro)

casas[4][1].pedra = None

casas[5][2].pedra = casas[5][1].pedra
casas[5][1].pedra = None
casas[5][2].pedra.coordenada_x = 5
casas[5][2].pedra.coordenada_y = 2
casas[5][2].pedra.atualizar_possiveis_destinos(partida.tabuleiro)

movimentos = casas[5][2].pedra.todos_possiveis_destinos(partida.tabuleiro, False, False)

print(movimentos)

mostrar_tabuleiro(partida)


