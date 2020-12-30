from abc import abstractmethod


class Pedra:

    def __init__(self):

        self.cor = None
        self.coordenada_x = None
        self.coordenada_y = None
        self.name = None

    @abstractmethod
    def todos_movimentos(self, casas):
        pass
