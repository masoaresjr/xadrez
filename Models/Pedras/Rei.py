from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Rei(Pedra):

    def __init__(self, cor):

        super().__init__()
        self.name = 'Rei'
        self.cor = cor
        self.coordenada_x = 4

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 0
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 7

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self, casas):
        casas_possiveis = []

        movimentos_x = [-1, 0, 1]
        movimentos_y = [-1, 0, 1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.coordenada_x <= 7 and 0 <= y + self.coordenada_y <= 7 and (x != 0 or y != 0):
                    movimento_possivel = [x + self.coordenada_x, y + self.coordenada_y]
                    casas_possiveis.append(movimento_possivel)

        return casas_possiveis


