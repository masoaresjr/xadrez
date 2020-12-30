from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Peao(Pedra):

    def __init__(self, cor, coordenada_x):

        super().__init__()
        self.primeiro_movimento = True
        self.name = 'Peão'
        self.cor = cor
        self.coordenada_x = coordenada_x

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 1
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 6

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self, casas):
        casas_possiveis = []

        movimento_y = [1]
        if self.primeiro_movimento:
            movimento_y.append(2)

        for casa in movimento_y:
            if self.cor == Models.Propriedades.Cor.Branca:
                casa_destino = casas[self.coordenada_x][self.coordenada_y + casa]
            else:
                casa_destino = casas[self.coordenada_x][self.coordenada_y - casa]

            if casa_destino.pedra is None:
                casas_possiveis.append(casa_destino)
            else:
                break

        pode_comer = self.pode_comer(casas)

        for casas in pode_comer:
            casas_possiveis.append(casas)

        return casas_possiveis

    def pode_comer(self, casas):
        pode_comer = []
        diagonais = [casas[self.coordenada_x - 1][self.coordenada_y + 1], casas[self.coordenada_x + 1][self.coordenada_y + 1]]

        for diagonal in diagonais:
            if diagonal.pedra is not None and diagonal.pedra.cor != self.cor:
                pode_comer.append(diagonal)

        return pode_comer
