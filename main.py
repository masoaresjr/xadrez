from Models.Peça import *
from Models.Casa import Posição
from itertools import chain


def montar_tabuleiro():
    peças = criar_peças()

    casas = posicionar_peças(peças, criar_posicoes())

    for index in range(8):
        linha = ""
        for i in casas:
            coluna = " | "
            peça = i[index].peça
            if peça is not None:
                coluna += peça.name
            else:
                coluna += "   "
            linha += coluna
        print(linha)

    print(casas[0][0].peça.name)
    print(casas[0][0].peça.todos_movimentos())
    casas[3][3].peça = casas[0][0].peça
    casas[3][3].peça.posicao_x = 3
    casas[3][3].peça.posicao_y = 3
    casas[3][3].peça.primeiro_movimento = False
    print(casas[3][3].peça.todos_movimentos())


def criar_peças():
    peoes = criar_peoes()
    torres = criar_torres()
    cavalos = criar_cavalos()
    bispos = criar_bispos()
    reis_e_rainhas = criar_realeza()

    peças = list(chain(peoes, torres, cavalos, bispos, reis_e_rainhas))

    return peças


def criar_peoes():
    peoes = []

    for posicao_x in range(8):
        peao_branco = Peao(Cor.Branca, posicao_x)
        peao_preto = Peao(Cor.Preta, posicao_x)
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


def criar_posicoes():
    posicoes = []

    for coordenada_x in range(8):
        nova_linha = []
        for coordenada_y in range(8):
            nova_linha.append(Posição(coordenada_x, coordenada_y))
        posicoes.append(nova_linha)

    return posicoes


def posicionar_peças(peças, posicoes):
    for peça in peças:
        posicao_a_usar = (posicoes[peça.posicao_x])[peça.posicao_y]
        posicao_a_usar.peça = peça

    return posicoes


montar_tabuleiro()
