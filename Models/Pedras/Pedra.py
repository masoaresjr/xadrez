from abc import abstractmethod


class Pedra:

    def __init__(self):

        self.cor = None
        self.coordenada_x = None
        self.coordenada_y = None
        self.name = None
        self.primeiro_movimento = None
        self.possiveis_destinos = []

    @abstractmethod
    def todos_possiveis_destinos(self, tabuleiro):
        # Usado para retornar os possíveis movimentos para uma eventual próxima rodada.
        # Outras pedras no tabuleiro não interferem no resultado desse método,
        #  isso porque na eventual próxima rodada o tabuleiro vai ter sido alterado
        # Também tende a ser usado para validar quais pedras podem ameaçar o rei adversário
        pass

    @abstractmethod
    def possiveis_destinos_reais(self, tabuleiro):
        # Usado para mostrar os possíveis movimentos para a rodada atual
        # Usa a propriedade atualizada pelo método atualizar_possiveis_destinos e
        #   valida possíveis bloqueios por outras pedras
        # Usado no começo da rodada
        pass

    @abstractmethod
    def atualizar_possiveis_destinos(self, tabuleiro):
        # Método responsável por atualizar a propriedade possiveis_destinos
        #   que será usada pelo método possiveis_destinos_reais
        # Usado no fim da rodada
        pass

    @abstractmethod
    def mover(self, tabuleiro):
        pass


