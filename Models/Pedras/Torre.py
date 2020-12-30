from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Torre(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Torre'
        self.Cor = cor
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

        contador_x = 0

        while contador_x <= 7:
            if contador_x != self.coordenada_x:
                movimento_possivel = [contador_x, self.coordenada_x]
                casas_posiveis.append(movimento_possivel)
            contador_x += 1

        contador_y = 0

        while contador_y <= 7:
            if contador_y != self.coordenada_y:
                movimento_possivel = [self.coordenada_y, contador_y]
                casas_posiveis.append(movimento_possivel)
            contador_y += 1

        return casas_posiveis
