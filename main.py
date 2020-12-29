from Models.Pedra import *
from Models.Casa import Casa
from itertools import chain


def montar_tabuleiro():
    pedras = criar_pedras()

    casas = posicionar_pedras(pedras, criar_casas())

    for index in range(8):
        linha = ""
        for i in casas:
            coluna = " | "
            pedra = i[index].pedra
            if pedra is not None:
                coluna += pedra.name
            else:
                coluna += "   "
            linha += coluna
        print(linha)

    print(casas[0][0].pedra.name)
    print(casas[0][0].pedra.todos_movimentos())
    casas[3][3].pedra = casas[0][0].pedra
    casas[3][3].pedra.coordenada_x = 3
    casas[3][3].pedra.coordenada_y = 3
    casas[3][3].pedra.primeiro_movimento = False
    print(casas[3][3].pedra.todos_movimentos())


def criar_pedras():
    peoes = criar_peoes()
    torres = criar_torres()
    cavalos = criar_cavalos()
    bispos = criar_bispos()
    reis_e_rainhas = criar_realeza()

    pedra = list(chain(peoes, torres, cavalos, bispos, reis_e_rainhas))

    return pedra


def criar_peoes():
    peoes = []

    for coordenada_x in range(8):
        peao_branco = Peao(Cor.Branca, coordenada_x)
        peao_preto = Peao(Cor.Preta, coordenada_x)
        peoes.extend([peao_branco, peao_preto])

    return peoes


# Melhorar!!! Fazer um método que crie torres, cavalos e bispos sem repetição
def criar_torres():
    torres = []

    torre_branca_rei = Torre(Cor.Branca, Lado.Rei)
    torre_branca_rainha = Torre(Cor.Branca, Lado.Rainha)

    torre_preta_rei = Torre(Cor.Preta, Lado.Rei)
    torre_preta_rainha = Torre(Cor.Preta, Lado.Rainha)

    torres.extend([torre_branca_rei, torre_branca_rainha, torre_preta_rei, torre_preta_rainha])

    return torres


def criar_cavalos():
    cavalos = []

    cavalo_branco_rei = Cavalo(Cor.Branca, Lado.Rei)
    cavalo_branco_rainha = Cavalo(Cor.Branca, Lado.Rainha)

    cavalo_preto_rei = Cavalo(Cor.Preta, Lado.Rei)
    cavalo_preto_rainha = Cavalo(Cor.Preta, Lado.Rainha)

    cavalos.extend([cavalo_branco_rei, cavalo_branco_rainha, cavalo_preto_rei, cavalo_preto_rainha])

    return cavalos


def criar_bispos():
    bispos = []

    bispo_branco_rei = Bispo(Cor.Branca, Lado.Rei)
    bispo_branco_rainha = Bispo(Cor.Branca, Lado.Rainha)

    bispo_preto_rei = Bispo(Cor.Preta, Lado.Rei)
    bispo_preto_rainha = Bispo(Cor.Preta, Lado.Rainha)

    bispos.extend([bispo_branco_rei, bispo_branco_rainha, bispo_preto_rei, bispo_preto_rainha])

    return bispos


def criar_realeza():
    realeza = []

    rei_branco = Rei(Cor.Branca)
    rei_preto = Rei(Cor.Preta)

    rainha_branca = Rainha(Cor.Branca)
    rainha_preta = Rainha(Cor.Preta)

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
