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
    def todos_possiveis_destinos(self, tabuleiro, atualizar_proximos_destinos):
        # Usado para retornar os possíveis movimentos
        # atualizar_proximos_destinos == False: Início da Rodada
        # atualizar_proximos_destinos == True: Fim da Rodada
        # Caso atualizar_proximos_destinos seja True, ira desconsiderar possiveis bloqueios por outras pedras,
        #   e também não valida se o movimento pode deixar o rei aliado em cheque, pois não estará sendo usado
        #   para indicar os atuais movimentos da pedra escolhida, mas sim mostrar quais possiveis destinos que a
        #   pedra pode ter em uma eventual próxima rodada.
        pass

    @abstractmethod
    def atualizar_possiveis_destinos(self, tabuleiro):
        # Método responsável por atualizar a propriedade possiveis_destinos
        # O motivo de gravar todos os possiveis destinos, mesmo que existam pedras no meio do caminho, é justamente pra
        #   validar se caso essa pedra, que está entre a origem e o destino da pedra escolhida, se mover para uma outra
        #   posição deixará o próprio rei em cheque. Isso será possível de validar pois ao gravar todos os possíveis
        #   movimentos de outras pedras, já saberemos quais delas estão mirando pro rei,
        #   tendo, ou não, outras pedras no caminho
        # Também será usado para impedir que o rei se mova diretamente para uma casa na mira de uma pedra adversária.
        # Usado no fim da rodada
        pass

    @abstractmethod
    def mover(self, tabuleiro):
        pass


