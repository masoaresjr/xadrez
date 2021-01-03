from Models.Pedras.Pedra import Pedra
from Models.Tabuleiro import Tabuleiro
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

    def todos_possiveis_destinos(self, tabuleiro, atualizar_proximos_destinos):
        casas_possiveis = []

        contador_x = [1, 0, -1]
        contador_y = [1, 0, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                if (x == 0 and y != 0) or (x != 0 and y == 0):  # Movimento só pode ser Horizontal OU Vertical
                    movimentos_direcao_unica.append(
                        self.movimento_direcao_unica(tabuleiro, atualizar_proximos_destinos, x, y)
                    )

        for direcao in movimentos_direcao_unica:
            for casa in direcao:
                casas_possiveis.append(casa)

        return casas_possiveis

    def atualizar_possiveis_destinos(self, tabuleiro):
        for linhas in tabuleiro.casas:
            for casa in linhas:
                if self in casa.possivel_destino_de:
                    casa.possivel_destino_de.remove(self)
                    self.possiveis_destinos.remove(casa)

        casas_destino = self.todos_possiveis_destinos(tabuleiro, True)

        for casa_destino in casas_destino:
            casa_destino.possivel_destino_de.append(self)
            self.possiveis_destinos.append(casa_destino)

    def mover(self, tabuleiro):
        pass

    def movimento_direcao_unica(self, tabuleiro, atualizar_proximos_destinos, contador_x, contador_y):
        casas_possiveis = []
        casas_destino = []

        if contador_y == 0:  # Movimento em X
            while 0 <= self.coordenada_x + contador_x <= 7:
                casas_destino.append(tabuleiro.casas[self.coordenada_x + contador_x][self.coordenada_y])
                if contador_x > 0:
                    contador_x += 1
                else:
                    contador_x -= 1

        elif contador_x == 0:  # Movimento em Y
            while 0 <= self.coordenada_y + contador_y <= 7:
                casas_destino.append(tabuleiro.casas[self.coordenada_x][self.coordenada_y + contador_y])
                if contador_y > 0:
                    contador_y += 1
                else:
                    contador_y -= 1

        for casa in casas_destino:
            if atualizar_proximos_destinos is True:
                casas_possiveis.append(casa)
            else:
                if casa.pedra is not None:
                    if casa.pedra.cor != self.cor:
                        casas_possiveis.append(casa)
                    break
                else:
                    casas_possiveis.append(casa)

        return casas_possiveis
