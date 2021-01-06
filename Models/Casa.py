class Casa:

    def __init__(self, coordenada_x, coordenada_y, pedra=None):
        self.pedra = pedra
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.possivel_destino_de = []

    def realizar_jogada(self, casa_destino, tabuleiro, lixeiras=None):

        if casa_destino.pedra is not None:

            self.comer_pedra(tabuleiro, casa_destino.pedra, lixeiras)

        if self.pedra.primeiro_movimento:
            self.pedra.primeiro_movimento = False

        self.mover_pedra(casa_destino)

    def mover_pedra(self, casa_destino):
        casa_destino.pedra = self.pedra
        casa_destino.pedra.coordenada_x = casa_destino.coordenada_x
        casa_destino.pedra.coordenada_y = casa_destino.coordenada_y
        self.pedra = None

    @staticmethod
    def comer_pedra(tabuleiro, pedra, lixeiras):
        for casa in tabuleiro:
            if pedra in casa.possivel_destino_de:
                casa.possivel_destino_de.remove(pedra)

        for lixeira in lixeiras:
            if lixeira.cor == pedra.cor:
                lixeira.pedras.append(pedra)

