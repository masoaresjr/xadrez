from Models.Casa import Casa
from Models.Pedras.Peao import Peao
from Models.Pedras.Torre import Torre
from Models.Pedras.Cavalo import Cavalo
from Models.Pedras.Bispo import Bispo
from Models.Pedras.Rei import Rei
from Models.Pedras.Rainha import Rainha
from Models.Propriedades import Cor
from Models.Propriedades import Lado
from itertools import chain


class Tabuleiro:

    def __init__(self):
        self.casas = []
        self.popular_tabuleiro()
        self.atualizar_todos_possiveis_destinos()

    def pegar_rei(self, cor):
        casa_do_rei = None

        for linha in self.casas:
            for casa in linha:
                if casa.pedra is not None:
                    if casa.pedra.name == "Rei":
                        if casa.pedra.cor == cor:
                            casa_do_rei = casa
        return casa_do_rei
    
    def escolher_casa(self, coordenada_x, coordenada_y):
        return self.casas[coordenada_x][coordenada_y]

    def popular_tabuleiro(self):
        self.criar_casas()
        pedras = self.criar_pedras()

        self.posicionar_pedras(pedras, self)

    def criar_casas(self):
        for coordenada_x in range(8):
            nova_linha = []
            for coordenada_y in range(8):
                nova_linha.append(Casa(coordenada_x, coordenada_y))
            self.casas.append(nova_linha)
            
    def criar_pedras(self):
        peoes = self.criar_peoes()
        torres = self.criar_torres()
        cavalos = self.criar_cavalos()
        bispos = self.criar_bispos()
        realeza = self.criar_realeza()

        return list(chain(peoes, torres, cavalos, bispos, realeza))

    @staticmethod
    def criar_peoes():
        peoes = []

        for coordenada_x in range(8):
            peao_branco = Peao(Cor.Branca, coordenada_x)
            peao_preto = Peao(Cor.Preta, coordenada_x)
            peoes.extend([peao_branco, peao_preto])

        return peoes

    # Melhorar!!! Fazer um método que crie torres, cavalos e bispos sem repetição
    @staticmethod
    def criar_torres():
        torres = []

        torre_branca_rei = Torre(Cor.Branca, Lado.Rei)
        torre_branca_rainha = Torre(Cor.Branca, Lado.Rainha)

        torre_preta_rei = Torre(Cor.Preta, Lado.Rei)
        torre_preta_rainha = Torre(Cor.Preta, Lado.Rainha)

        torres.extend([torre_branca_rei, torre_branca_rainha, torre_preta_rei, torre_preta_rainha])

        return torres

    @staticmethod
    def criar_cavalos():
        cavalos = []

        cavalo_branco_rei = Cavalo(Cor.Branca, Lado.Rei)
        cavalo_branco_rainha = Cavalo(Cor.Branca, Lado.Rainha)

        cavalo_preto_rei = Cavalo(Cor.Preta, Lado.Rei)
        cavalo_preto_rainha = Cavalo(Cor.Preta, Lado.Rainha)

        cavalos.extend([cavalo_branco_rei, cavalo_branco_rainha, cavalo_preto_rei, cavalo_preto_rainha])

        return cavalos

    @staticmethod
    def criar_bispos():
        bispos = []

        bispo_branco_rei = Bispo(Cor.Branca, Lado.Rei)
        bispo_branco_rainha = Bispo(Cor.Branca, Lado.Rainha)

        bispo_preto_rei = Bispo(Cor.Preta, Lado.Rei)
        bispo_preto_rainha = Bispo(Cor.Preta, Lado.Rainha)

        bispos.extend([bispo_branco_rei, bispo_branco_rainha, bispo_preto_rei, bispo_preto_rainha])

        return bispos

    @staticmethod
    def criar_realeza():
        realeza = []

        rei_branco = Rei(Cor.Branca)
        rei_preto = Rei(Cor.Preta)

        rainha_branca = Rainha(Cor.Branca)
        rainha_preta = Rainha(Cor.Preta)

        realeza.extend([rei_branco, rei_preto, rainha_branca, rainha_preta])

        return realeza

    @staticmethod
    def posicionar_pedras(pedras, tabuleiro):
        for pedra in pedras:
            casa = (tabuleiro.casas[pedra.coordenada_x])[pedra.coordenada_y]
            casa.pedra = pedra

        return tabuleiro

    def atualizar_todos_possiveis_destinos(self):
        for linha in self.casas:
            for casa in linha:
                if casa.pedra is not None:
                    casa.pedra.atualizar_possiveis_destinos(self)
