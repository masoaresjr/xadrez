from Models.Pedras.Pedra import Pedra
import Models.Propriedades
from itertools import chain


class Rainha(Pedra):

    def __init__(self, cor):

        super().__init__()
        self.name = 'Rainha'
        self.cor = cor
        self.coordenada_x = 3

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 0
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 7

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self, casas, fim_da_rodada):
        casas_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_diagonais(x, y, casas, fim_da_rodada))

        movimentos_direcao_unica.append(self.movimentos_verticais_horizontais(True, casas, fim_da_rodada))
        movimentos_direcao_unica .append(self.movimentos_verticais_horizontais(False, casas, fim_da_rodada))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                casas_possiveis.append(movimento)

        return casas_possiveis

    def movimentos_verticais_horizontais(self, eixo_x, casas, fim_de_rodada):
        casas_possiveis = []

        if eixo_x:
            coordenada = self.__getattribute__("coordenada_x")
        else:
            coordenada = self.__getattribute__("coordenada_y")

        contador = 1
        while coordenada + contador <= 7:

            if eixo_x:
                casa_destino = casas[self.coordenada_x + contador][self.coordenada_y]
            else:
                casa_destino = casas[self.coordenada_x][self.coordenada_y + contador]

            if fim_de_rodada is False:
                if casa_destino.pedra is not None:
                    if casa_destino.pedra.cor != self.cor:
                        casas_possiveis.append(casa_destino)
                    break

            casas_possiveis.append(casa_destino)
            contador += 1

        contador = 1
        while coordenada - contador >= 0:

            if eixo_x:
                casa_destino = casas[self.coordenada_x - contador][self.coordenada_y]
            else:
                casa_destino = casas[self.coordenada_x][self.coordenada_y - contador]

            if fim_de_rodada is False:
                if casa_destino.pedra is not None:
                    if casa_destino.pedra.cor != self.cor:
                        casas_possiveis.append(casa_destino)
                    break

            casas_possiveis.append(casa_destino)
            contador += 1

        return casas_possiveis

    def movimentos_diagonais(self, contador_x, contador_y, casas, fim_de_rodada):
        casas_possiveis = []

        while 0 <= contador_x + self.coordenada_x <= 7 and 0 <= contador_y + self.coordenada_y <= 7:
            casa_destino = casas[contador_x + self.coordenada_x][contador_y + self.coordenada_y]

            if fim_de_rodada is False:
                if casa_destino.pedra is not None:
                    if casa_destino.pedra.cor != self.cor:
                        casas_possiveis.append(casa_destino)
                    break
            casas_possiveis.append(casa_destino)

            if contador_x > 0:
                contador_x += 1
            else:
                contador_x -= 1

            if contador_y > 0:
                contador_y += 1
            else:
                contador_y -= 1

        return casas_possiveis

    def atualizar_possiveis_destinos(self, tabuleiro):
        for linhas in tabuleiro:
            for casa in linhas:
                if self in casa.possivel_destino_de:
                    casa.possivel_destino_de.remove(self)

        casas_destino = self.todos_movimentos(tabuleiro, True)

        for casa_destino in casas_destino:
            casa_destino.possivel_destino_de.append(self)


