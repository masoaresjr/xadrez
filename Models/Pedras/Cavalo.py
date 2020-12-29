from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Cavalo(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Cavalo'
        self.Cor = cor
        self.Lado = lado

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 0
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 7

        if lado == Models.Propriedades.Lado.Rei:
            self.coordenada_x = 6
        elif lado == Models.Propriedades.Lado.Rainha:
            self.coordenada_x = 1

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self):
        casas_possiveis = []

        movimentos_x = [-1, 1]
        movimentos_y = [2, -2]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= y + self.coordenada_y <= 7 and 0 <= x + self.coordenada_x <= 7:
                    movimento_possivel = [x + self.coordenada_x, y + self.coordenada_y]
                    casas_possiveis.append(movimento_possivel)

        movimentos_x = [-2, 2]
        movimentos_y = [1, -1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.coordenada_x <= 7 and 0 <= y + self.coordenada_y <= 7:
                    movimento_possivel = [x + self.coordenada_x, y + self.coordenada_y]
                    casas_possiveis.append(movimento_possivel)

        return casas_possiveis
