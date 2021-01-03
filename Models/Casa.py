class Casa:

    def __init__(self, coordenada_x, coordenada_y, pedra=None):
        self.pedra = pedra
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.possivel_destino_de = []

    def mover(self, casa_destino, tabuleiro, lixeiras=None):

        if casa_destino.pedra is not None:

            for casa in tabuleiro:
                if casa_destino.pedra in casa.possivel_destino_de:
                    casa.possivel_destino_de.remove(casa_destino.pedra)

            for lixeira in lixeiras:
                if lixeira.cor == casa_destino.pedra.cor:
                    lixeira.pedras.append(casa_destino.pedra)

        if self.pedra.primeiro_movimento:
            self.pedra.primeiro_movimento = False

        casa_destino.pedra = self.pedra
        casa_destino.pedra.coordenada_x = casa_destino.coordenada_x
        casa_destino.pedra.coordenada_y = casa_destino.coordenada_y
        self.pedra = None
