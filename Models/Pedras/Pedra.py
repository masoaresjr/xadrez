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
    def todos_possiveis_destinos(self, tabuleiro, atualizar_proximos_destinos, verificar_possivel_cheque):
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

    def rei_em_cheque(self, tabuleiro, casa_atual_do_rei, casa_destino):
        rei_em_cheque = False

        coordenada_x_atual = self.coordenada_x
        coordenada_y_atual = self.coordenada_y

        pedra_atual_no_destino = casa_destino.pedra
        self.mover_temporariamente(tabuleiro, casa_destino)

        for pedra in casa_atual_do_rei.possivel_destino_de:

            # Se a pedra for aliada, ou se for comida, não existe cheque:
            if pedra.cor != casa_atual_do_rei.pedra.cor and pedra != pedra_atual_no_destino:

                todos_possiveis_destinos = pedra.todos_possiveis_destinos(tabuleiro, False, True)

                if casa_atual_do_rei in todos_possiveis_destinos:
                    rei_em_cheque = True
                    break

        self.voltar_ao_estado_original(tabuleiro, coordenada_x_atual, coordenada_y_atual
                                       , casa_destino, pedra_atual_no_destino)

        return rei_em_cheque

    def mover_temporariamente(self, tabuleiro, casa_destino):
        casa_atual = self.pegar_casa(tabuleiro)
        casa_atual.pedra = None
        casa_destino.pedra = self

    def voltar_ao_estado_original(self, tabuleiro, coordenada_x, coordenada_y, casa_destino, pedra_atual_no_destino):
        tabuleiro.casas[coordenada_x][coordenada_y].pedra = self
        casa_destino.pedra = pedra_atual_no_destino

    def pegar_casa(self, tabuleiro):
        for linha in tabuleiro.casas:
            for casa in linha:
                if casa.pedra == self:
                    return casa


