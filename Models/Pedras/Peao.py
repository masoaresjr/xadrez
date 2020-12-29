from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Peao(Pedra):

    def __init__(self, cor, coordenada_x):

        super().__init__()
        self.primeiro_movimento = True
        self.name = 'Peão'
        self.Cor = cor
        self.coordenada_x = coordenada_x

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 1
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 6

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self):
        casas_possiveis = []

        if self.Cor == Models.Propriedades.Cor.Branca:
            movimento_y = [1]
            if self.primeiro_movimento:
                movimento_y.append(2)
        else:
            movimento_y = [-1]
            if self.primeiro_movimento:
                movimento_y.append(-2)

        for casa in movimento_y:
            movimento_possivel = [self.coordenada_x, self.coordenada_y + casa]
            casas_possiveis.append(movimento_possivel)

        return casas_possiveis


