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

    def movimentos_direcao_unica(self, contador_x, contador_y, casas):
        casas_possiveis = []

        while 0 <= contador_x + self.coordenada_x <= 7 and 0 <= contador_y + self.coordenada_y <= 7:
            casa_destino = casas[contador_x + self.coordenada_x][contador_y + self.coordenada_y]

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

    def todos_movimentos(self, casas, fim_da_rodada):
        casas_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_direcao_unica(x, y, casas))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                casas_possiveis.append(movimento)

        return casas_possiveis

    def atualizar_possiveis_destinos(self, casas):
        pass
