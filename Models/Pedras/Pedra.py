from abc import abstractmethod


class Pedra:

    def __init__(self):

        self.cor = None
        self.coordenada_x = None
        self.coordenada_y = None
        self.name = None
        self.primeiro_movimento = None

    @abstractmethod
    def todos_movimentos(self, tabuleiro, fim_da_rodada):
        pass

    @abstractmethod
    def atualizar_possiveis_destinos(self, tabuleiro):
        pass
