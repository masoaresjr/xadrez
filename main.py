from Models.Jogo.Partida import Partida

partida = Partida("Um", "Dois")

for index in range(8):
    linha = ""
    for i in partida.tabuleiro.casas:
        coluna = " | "
        pedra = i[index].pedra
        if pedra is not None:
            coluna += pedra.name
        else:
            coluna += "   "
        linha += coluna
    print(linha)
