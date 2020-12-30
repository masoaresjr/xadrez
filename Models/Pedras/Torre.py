from Models.Pedras.Pedra import Pedra
import Models.Propriedades


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

    def todos_movimentos(self, casas):
        casas_posiveis = []

        contador_x = 1
        while self.coordenada_x + contador_x <= 7:
            casa_destino = casas[self.coordenada_x + contador_x][self.coordenada_y]
            if casa_destino.pedra is not None:
                if casa_destino.pedra.cor != self.cor:
                    casas_posiveis.append(casa_destino)
                break
            casas_posiveis.append(casa_destino)
            contador_x += 1

        contador_x = 1
        while self.coordenada_x - contador_x >= 0:
            casa_destino = casas[self.coordenada_x - contador_x][self.coordenada_y]
            if casa_destino.pedra is not None:
                if casa_destino.pedra.cor != self.cor:
                    casas_posiveis.append(casa_destino)
                break
            casas_posiveis.append(casa_destino)
            contador_x += 1

        contador_y = 1
        while self.coordenada_y + contador_y <= 7:
            casa_destino = casas[self.coordenada_x][self.coordenada_y + contador_y]
            if casa_destino.pedra is not None:
                if casa_destino.pedra.cor != self.cor:
                    casas_posiveis.append(casa_destino)
                break
            casas_posiveis.append(casa_destino)
            contador_y += 1

        contador_y = 1
        while self.coordenada_y - contador_y >= 0:
            casa_destino = casas[self.coordenada_x][self.coordenada_y - contador_y]
            if casa_destino.pedra is not None:
                if casa_destino.pedra.cor != self.cor:
                    casas_posiveis.append(casa_destino)
                break
            casas_posiveis.append(casa_destino)
            contador_y += 1

        return casas_posiveis

