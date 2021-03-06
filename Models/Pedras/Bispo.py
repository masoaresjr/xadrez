from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Bispo(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Bispo'
        self.cor = cor
        self.Lado = lado

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 0
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 7

        if lado == Models.Propriedades.Lado.Rei:
            self.coordenada_x = 5
        elif lado == Models.Propriedades.Lado.Rainha:
            self.coordenada_x = 2

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_possiveis_destinos(self, tabuleiro, atualizar_proximos_destinos):
        casas_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_direcao_unica(x, y, tabuleiro, atualizar_proximos_destinos))

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

        casas_destino = self.todos_possiveis_destinos(tabuleiro, True, False)

        for casa_destino in casas_destino:
            casa_destino.possivel_destino_de.append(self)
            self.possiveis_destinos.append(casa_destino)

    def mover(self, tabuleiro):
        pass

    def movimentos_direcao_unica(self, contador_x, contador_y, tabuleiro, atualizar_proximos_destinos):
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
