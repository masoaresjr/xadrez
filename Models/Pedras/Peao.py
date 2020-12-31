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

    def todos_movimentos(self, tabuleiro, fim_da_rodada):
        casas_possiveis = []

        movimento_y = [1]
        if self.primeiro_movimento:
            movimento_y.append(2)

        for casa in movimento_y:
            if self.cor == Models.Propriedades.Cor.Branca:
                casa_destino = tabuleiro[self.coordenada_x][self.coordenada_y + casa]
            else:
                casa_destino = tabuleiro[self.coordenada_x][self.coordenada_y - casa]
            if fim_da_rodada is False:
                if casa_destino.pedra is None:
                    casas_possiveis.append(casa_destino)
                else:
                    break
            else:
                casas_possiveis.append(casa_destino)

        pode_comer = self.pode_comer(tabuleiro, fim_da_rodada)

        for casas in pode_comer:
            casas_possiveis.append(casas)

        return casas_possiveis

    def pode_comer(self, tabuleiro, fim_da_rodada):
        pode_comer = []
        diagonais = []

        if 0 <= self.coordenada_x + 1 <= 7:
            diagonais.append(tabuleiro[self.coordenada_x + 1][self.coordenada_y + 1])
        if 0 <= self.coordenada_x - 1 <= 7:
            diagonais.append(tabuleiro[self.coordenada_x - 1][self.coordenada_y + 1])

        for diagonal in diagonais:
            if fim_da_rodada is False:
                if diagonal.pedra is not None and diagonal.pedra.cor != self.cor:
                    pode_comer.append(diagonal)
            else:
                pode_comer.append(diagonal)

        return pode_comer

    def atualizar_possiveis_destinos(self, tabuleiro):
        for linhas in tabuleiro:
            for casa in linhas:
                if self in casa.possivel_destino_de:
                    casa.possivel_destino_de.remove(self)

        casas_destino = self.todos_movimentos(tabuleiro, True)

        for casa_destino in casas_destino:
            casa_destino.possivel_destino_de.append(self)
            self.destinos_possiveis.append(casa_destino)
