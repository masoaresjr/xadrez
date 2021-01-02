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

    def todos_possiveis_destinos(self, casas, atualizar_proximos_destinos):
        casas_possiveis = []

        movimentos_x = [-1, 0, 1]
        movimentos_y = [-1, 0, 1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.coordenada_x <= 7 and 0 <= y + self.coordenada_y <= 7 and (x != 0 or y != 0):
                    casa_destino = casas[x + self.coordenada_x][y + self.coordenada_y]

                    if atualizar_proximos_destinos is True:
                        casas_possiveis.append(casa_destino)
                    else:
                        if casa_destino.pedra is not None:
                            if casa_destino.pedra.cor != self.cor:
                                casas_possiveis.append(casa_destino)
                        else:
                            casas_possiveis.append(casa_destino)

        return casas_possiveis

    def atualizar_possiveis_destinos(self, tabuleiro):
        for linhas in tabuleiro:
            for casa in linhas:
                if self in casa.possivel_destino_de:
                    casa.possivel_destino_de.remove(self)
                    self.possiveis_destinos.remove(casa)

        casas_destino = self.todos_possiveis_destinos(tabuleiro, False)

        for casa_destino in casas_destino:
            casa_destino.possivel_destino_de.append(self)
            self.possiveis_destinos.append(casa_destino)

    def mover(self, tabuleiro):
        pass

