from abc import abstractmethod


class Pedra:

    def __init__(self):

        self.cor = None
        self.coordenada_x = None
        self.coordenada_y = None
        self.name = None
        self.primeiro_movimento = None
        self.destinos_possiveis = []

    # Possiveis destinos contém todas as casas que a pedra poderia se mover caso não houvessem outras pedras no caminho
    # Possiveis Destinos Reais contém somente as casas que a pedra conseguirá se mover na rodada atual

    @abstractmethod
    def possiveis_destinos(self, tabuleiro, fim_da_rodada):
        pass

    @abstractmethod
    def possiveis_destinos_reais(self, tabuleiro):
        pass

    @abstractmethod
    def atualizar_possiveis_destinos(self, tabuleiro):
        pass

    @abstractmethod
    def mover(self, tabuleiro):
        pass


