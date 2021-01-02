from Models.Pedras.Pedra import Pedra
import Models.Propriedades


class Peao(Pedra):

    def __init__(self, cor, coordenada_x):

        super().__init__()
        self.primeiro_posicionamento = True
        self.primeiro_movimento = True
        self.name = 'Peão'
        self.cor = cor
        self.coordenada_x = coordenada_x

        if cor == Models.Propriedades.Cor.Branca:
            self.coordenada_y = 1
        elif cor == Models.Propriedades.Cor.Preta:
            self.coordenada_y = 6

        self.casa_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_possiveis_destinos(self, tabuleiro):
        casas_possiveis = []

        movimento_y = [1]
        if self.primeiro_movimento:
            movimento_y.append(2)

        for casa in movimento_y:
            if self.cor == Models.Propriedades.Cor.Branca:
                casa_destino = tabuleiro[self.coordenada_x][self.coordenada_y + casa]
            else:
                casa_destino = tabuleiro[self.coordenada_x][self.coordenada_y - casa]

            casas_possiveis.append(casa_destino)

        pode_comer = self.pode_comer(tabuleiro)

        for casas in pode_comer:
            casas_possiveis.append(casas)

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
        casas_possiveis = []

        for casa in self.possiveis_destinos:

            # Se for diagonal, só move se existir uma pedra do adversário
            if casa.coordenada_x == self.coordenada_x + 1 or casa.coordenada_x == self.coordenada_x - 1:
                if casa.pedra is not None:
                    if casa.pedra.cor != self.cor:
                        casas_possiveis.append(casa)
                        continue
                    continue
                continue

            if casa.pedra is None:
                casas_possiveis.append(casa)

        return casas_possiveis

    def mover(self, tabuleiro):
        pass

    def pode_comer(self, tabuleiro):
        pode_comer = []

        if self.cor == Models.Propriedades.Cor.Branca:
            movimento_y = 1
        else:
            movimento_y = -1

        if 0 <= self.coordenada_x + 1 <= 7:
            pode_comer.append(tabuleiro[self.coordenada_x + 1][self.coordenada_y + movimento_y])
        if 0 <= self.coordenada_x - 1 <= 7:
            pode_comer.append(tabuleiro[self.coordenada_x - 1][self.coordenada_y + movimento_y])

        return pode_comer
