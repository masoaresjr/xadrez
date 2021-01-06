from Models.Tabuleiro import Tabuleiro
from Models.Jogo.Jogador import Jogador
from Models.Propriedades import Cor


class Partida:

    def __init__(self, nome_jogador_um, nome_jogador_dois):
        self.tabuleiro = Tabuleiro()
        self.jogadores = []
        self.rodadas = []
        self.criar_jogadores(nome_jogador_um, nome_jogador_dois)

    def criar_jogadores(self, nome_jogador_um, nome_jogador_dois):
        self.jogadores.append(Jogador(nome_jogador_um, Cor.Branca))
        self.jogadores.append(Jogador(nome_jogador_dois, Cor.Preta))
