from Models.Pedras.Pedra import Pedra
import Models.Propriedades


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

    def todos_possiveis_destinos(self, tabuleiro, atualizar_proximos_destinos):
        casas_possiveis = []

        movimentos_direcao_unica = []
        contador_x = [1, -1]
        contador_y = [1, -1]

        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_diagonais(x, y, tabuleiro, atualizar_proximos_destinos))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                casas_possiveis.append(movimento)

        movimentos_direcao_unica = []
        contador_x = [1, 0, -1]
        contador_y = [1, 0, -1]

        for x in contador_x:
            for y in contador_y:
                if (x == 0 and y != 0) or (x != 0 and y == 0):  # Movimento só pode ser Horizontal OU Vertical
                    movimentos_direcao_unica.append(
                        self.movimentos_verticais_horizontais(tabuleiro, atualizar_proximos_destinos,
                                                              x, y
                                                              )
                    )

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                casas_possiveis.append(movimento)

        return casas_possiveis

    def atualizar_possiveis_destinos(self, tabuleiro):
        for linhas in tabuleiro.casas:
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

    def movimentos_verticais_horizontais(self, tabuleiro, atualizar_proximos_destinos, contador_x, contador_y):
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

    def movimentos_diagonais(self, contador_x, contador_y, tabuleiro, atualizar_proximos_destinos):
        casas_possiveis = []

        while 0 <= contador_x + self.coordenada_x <= 7 and 0 <= contador_y + self.coordenada_y <= 7:
            casa_destino = tabuleiro.casas[contador_x + self.coordenada_x][contador_y + self.coordenada_y]

            if atualizar_proximos_destinos is True:
                casas_possiveis.append(casa_destino)
            else:
                if casa_destino.pedra is None:
                    casas_possiveis.append(casa_destino)
                else:
                    if casa_destino.pedra.cor != self.cor:
                        casas_possiveis.append(casa_destino)
                    break

            if contador_x > 0:
                contador_x += 1
            else:
                contador_x -= 1

            if contador_y > 0:
                contador_y += 1
            else:
                contador_y -= 1

        return casas_possiveis
