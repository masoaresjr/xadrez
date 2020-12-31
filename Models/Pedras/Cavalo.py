from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Cavalo(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Cavalo'
        self.cor = cor
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

    def todos_movimentos(self, casas, fim_da_rodada):
        casas_possiveis = []

        casas_destino = [self.movimentos([-1, 1], [2, -2], casas), self.movimentos([-2, 2], [1, -1], casas)]

        for lista_de_casas in casas_destino:
            for casas in lista_de_casas:
                casas_possiveis.append(casas)

        return casas_possiveis

    def movimentos(self, coordenadas_x, coordenadas_y, casas):
        casas_possiveis = []

        for x in coordenadas_x:
            for y in coordenadas_y:
                if 0 <= x + self.coordenada_x <= 7 and 0 <= y + self.coordenada_y <= 7:
                    casa_destino = casas[x + self.coordenada_x][y + self.coordenada_y]
                    if casa_destino.pedra is not None:
                        if casa_destino.pedra.cor != self.cor:
                            casas_possiveis.append(casa_destino)
                        continue
                    casas_possiveis.append(casa_destino)
        return casas_possiveis

    def atualizar_possiveis_destinos(self, casas):
        pass