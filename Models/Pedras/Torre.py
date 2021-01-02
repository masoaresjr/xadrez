from Models.Pedras.Pedra import Pedra
import Models.Propriedades
from itertools import chain


class Torre(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Torre'
        self.cor = cor
        self.Lado = lado

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 0
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 7

        if lado == Models.Propriedades.Lado.Rei:
            self.coordenada_x = 7
        elif lado == Models.Propriedades.Lado.Rainha:
            self.coordenada_x = 0

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_possiveis_destinos(self, tabuleiro):

        movimentos_eixo_x = self.movimento_direcao_unica(True, tabuleiro)
        movimentos_eixo_y = self.movimento_direcao_unica(False, tabuleiro)

        casas_possiveis = list(chain(movimentos_eixo_x, movimentos_eixo_y))

        return casas_possiveis

    def atualizar_possiveis_destinos(self, tabuleiro):
        for linhas in tabuleiro:
            for casa in linhas:
                if self in casa.possivel_destino_de:
                    casa.possivel_destino_de.remove(self)
                    self.possiveis_destinos.remove(casa)

        casas_destino = self.todos_possiveis_destinos(tabuleiro)

        for casa_destino in casas_destino:
            casa_destino.possivel_destino_de.append(self)
            self.possiveis_destinos.append(casa_destino)

    def possiveis_destinos_reais(self, tabuleiro):
        pass

    def mover(self, tabuleiro):
        pass

    def movimento_direcao_unica(self, eixo_x, tabuleiro):
        casas_possiveis = []
        casas_destino = []

        if eixo_x:
            coordenada = self.__getattribute__("coordenada_x")
        else:
            coordenada = self.__getattribute__("coordenada_y")

        contador = 1
        while coordenada + contador <= 7:

            if eixo_x:
                casas_destino.append(tabuleiro[self.coordenada_x + contador][self.coordenada_y])
            else:
                casas_destino.append(tabuleiro[self.coordenada_x][self.coordenada_y + contador])

            contador += 1

        contador = 1
        while coordenada - contador >= 0:

            if eixo_x:
                casas_destino.append(tabuleiro[self.coordenada_x - contador][self.coordenada_y])
            else:
                casas_destino.append(tabuleiro[self.coordenada_x][self.coordenada_y - contador])

            contador += 1

        for casas in casas_destino:
            casas_possiveis.append(casas)

        return casas_possiveis
