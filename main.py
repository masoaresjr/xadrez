from Models.Casa import Casa
from Models.Pedras.Peao import Peao
from Models.Pedras.Torre import Torre
from Models.Pedras.Cavalo import Cavalo
from Models.Pedras.Bispo import Bispo
from Models.Pedras.Rei import Rei
from Models.Pedras.Rainha import Rainha
import Models.Lixeira
import Models.Propriedades
from itertools import chain


def montar_tabuleiro():
    pedras = criar_pedras()
    tabuleiro = posicionar_pedras(pedras, criar_casas())
    lixeiras = [Models.Lixeira.Lixeira(Models.Propriedades.Cor.Branca), Models.Lixeira.Lixeira(Models.Propriedades.Cor.Preta)]

    for index in range(8):
        linha = ""
        for i in tabuleiro:
            coluna = " | "
            pedra = i[index].pedra
            if pedra is not None:
                coluna += pedra.name
            else:
                coluna += "   "
            linha += coluna
        print(linha)


def criar_pedras():
    peoes = criar_peoes()
    torres = criar_torres()
    cavalos = criar_cavalos()
    bispos = criar_bispos()
    realeza = criar_realeza()

    pedra = list(chain(peoes, torres, cavalos, bispos, realeza))

    return pedra


def criar_peoes():
    peoes = []

    for coordenada_x in range(8):
        peao_branco = Peao(Models.Propriedades.Cor.Branca, coordenada_x)
        peao_preto = Peao(Models.Propriedades.Cor.Preta, coordenada_x)
        peoes.extend([peao_branco, peao_preto])

    return peoes


# Melhorar!!! Fazer um método que crie torres, cavalos e bispos sem repetição
def criar_torres():
    torres = []

    torre_branca_rei = Torre(Models.Propriedades.Cor.Branca, Models.Propriedades.Lado.Rei)
    torre_branca_rainha = Torre(Models.Propriedades.Cor.Branca, Models.Propriedades.Lado.Rainha)

    torre_preta_rei = Torre(Models.Propriedades.Cor.Preta, Models.Propriedades.Lado.Rei)
    torre_preta_rainha = Torre(Models.Propriedades.Cor.Preta, Models.Propriedades.Lado.Rainha)

    torres.extend([torre_branca_rei, torre_branca_rainha, torre_preta_rei, torre_preta_rainha])

    return torres


def criar_cavalos():
    cavalos = []

    cavalo_branco_rei = Cavalo(Models.Propriedades.Cor.Branca, Models.Propriedades.Lado.Rei)
    cavalo_branco_rainha = Cavalo(Models.Propriedades.Cor.Branca, Models.Propriedades.Lado.Rainha)

    cavalo_preto_rei = Cavalo(Models.Propriedades.Cor.Preta, Models.Propriedades.Lado.Rei)
    cavalo_preto_rainha = Cavalo(Models.Propriedades.Cor.Preta, Models.Propriedades.Lado.Rainha)

    cavalos.extend([cavalo_branco_rei, cavalo_branco_rainha, cavalo_preto_rei, cavalo_preto_rainha])

    return cavalos


def criar_bispos():
    bispos = []

    bispo_branco_rei = Bispo(Models.Propriedades.Cor.Branca, Models.Propriedades.Lado.Rei)
    bispo_branco_rainha = Bispo(Models.Propriedades.Cor.Branca, Models.Propriedades.Lado.Rainha)

    bispo_preto_rei = Bispo(Models.Propriedades.Cor.Preta, Models.Propriedades.Lado.Rei)
    bispo_preto_rainha = Bispo(Models.Propriedades.Cor.Preta, Models.Propriedades.Lado.Rainha)

    bispos.extend([bispo_branco_rei, bispo_branco_rainha, bispo_preto_rei, bispo_preto_rainha])

    return bispos


def criar_realeza():
    realeza = []

    rei_branco = Rei(Models.Propriedades.Cor.Branca)
    rei_preto = Rei(Models.Propriedades.Cor.Preta)

    rainha_branca = Rainha(Models.Propriedades.Cor.Branca)
    rainha_preta = Rainha(Models.Propriedades.Cor.Preta)

    realeza.extend([rei_branco, rei_preto, rainha_branca, rainha_preta])

    return realeza


def criar_casas():
    casas = []

    for coordenada_x in range(8):
        nova_linha = []
        for coordenada_y in range(8):
            nova_linha.append(Casa(coordenada_x, coordenada_y))
        casas.append(nova_linha)

    return casas


def posicionar_pedras(pedras, casas):
    for pedra in pedras:
        casa = (casas[pedra.coordenada_x])[pedra.coordenada_y]
        casa.pedra = pedra

    return casas


montar_tabuleiro()
