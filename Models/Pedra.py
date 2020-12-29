from abc import abstractmethod
import enum


class Pedra:

    def __init__(self):

        self.Cor = None
        self.coordenada_x = None
        self.coordenada_y = None
        self.name = None

    @abstractmethod
    def todos_movimentos(self):
        pass

    @abstractmethod
    def mover(self, casa_origem, casa_destino):
        pass


class Peao(Pedra):

    def __init__(self, cor, coordenada_x):

        super().__init__()
        self.primeiro_movimento = True
        self.name = 'Peao'
        self.Cor = cor
        self.coordenada_x = coordenada_x

        if cor == Cor.Branca:
            self.coordenada_y = 1
        elif cor == Cor.Preta:
            self.coordenada_y = 6

        self.posicao_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self):
        casas_possiveis = []

        if self.Cor == Cor.Branca:
            movimento_y = [1]
            if self.primeiro_movimento:
                movimento_y.append(2)
        else:
            movimento_y = [-1]
            if self.primeiro_movimento:
                movimento_y.append(-2)

        for casa in movimento_y:
            movimento_possivel = [self.coordenada_x, self.coordenada_y + casa]
            casas_possiveis.append(movimento_possivel)

        return casas_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Torre(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Torre'
        self.Cor = cor
        self.Lado = lado

        if cor == Cor.Branca:
            self.coordenada_y = 0
        elif cor == Cor.Preta:
            self.coordenada_y = 7

        if lado == Lado.Rei:
            self.coordenada_x = 7
        elif lado == Lado.Rainha:
            self.coordenada_x = 0

        self.posicao_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self):
        casas_posiveis = []

        contador_x = 0

        while contador_x <= 7:
            if contador_x != self.coordenada_x:
                movimento_possivel = [contador_x, self.coordenada_x]
                casas_posiveis.append(movimento_possivel)
            contador_x += 1

        contador_y = 0

        while contador_y <= 7:
            if contador_y != self.coordenada_y:
                movimento_possivel = [self.coordenada_y, contador_y]
                casas_posiveis.append(movimento_possivel)
            contador_y += 1

        return casas_posiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Cavalo(Pedra):

    def test(self):
        print("Cavalo")

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Cavalo'
        self.Cor = cor
        self.Lado = lado

        if cor == Cor.Branca:
            self.coordenada_y = 0
        elif cor == Cor.Preta:
            self.coordenada_y = 7

        if lado == Lado.Rei:
            self.coordenada_x = 6
        elif lado == Lado.Rainha:
            self.coordenada_x = 1

        self.posicao_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self):
        casas_possiveis = []

        movimentos_x = [-1, 1]
        movimentos_y = [2, -2]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= y + self.coordenada_y <= 7 and 0 <= x + self.coordenada_x <= 7:
                    movimento_possivel = [x + self.coordenada_x, y + self.coordenada_y]
                    casas_possiveis.append(movimento_possivel)

        movimentos_x = [-2, 2]
        movimentos_y = [1, -1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.coordenada_x <= 7 and 0 <= y + self.coordenada_y <= 7:
                    movimento_possivel = [x + self.coordenada_x, y + self.coordenada_y]
                    casas_possiveis.append(movimento_possivel)

        return casas_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Bispo(Pedra):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Bispo'
        self.Cor = cor
        self.Lado = lado

        if cor == Cor.Branca:
            self.coordenada_y = 0
        elif cor == Cor.Preta:
            self.coordenada_y = 7

        if lado == Lado.Rei:
            self.coordenada_x = 5
        elif lado == Lado.Rainha:
            self.coordenada_x = 2

        self.posicao_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def movimentos_direcao_unica(self, contador_x, contador_y):
        todos_movimentos = []

        while 0 <= contador_x + self.coordenada_x <= 7 and 0 <= contador_y + self.coordenada_y <= 7:
            movimento_possivel = [contador_x + self.coordenada_x, contador_y + self.coordenada_y]
            todos_movimentos.append(movimento_possivel)

            if contador_x > 0:
                contador_x += 1
            else:
                contador_x -= 1

            if contador_y > 0:
                contador_y += 1
            else:
                contador_y -= 1

        return todos_movimentos

    def todos_movimentos(self):
        casas_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_direcao_unica(x, y))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                casas_possiveis.append(movimento)

        return casas_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Rei(Pedra):

    def __init__(self, cor):

        super().__init__()
        self.name = 'Rei'
        self.Cor = cor
        self.coordenada_x = 4

        if cor == Cor.Branca:
            self.coordenada_y = 0
        elif cor == Cor.Preta:
            self.coordenada_y = 7

        self.posicao_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def todos_movimentos(self):
        casas_possiveis = []

        movimentos_x = [-1, 0, 1]
        movimentos_y = [-1, 0, 1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.coordenada_x <= 7 and 0 <= y + self.coordenada_y <= 7 and (x != 0 or y != 0):
                    movimento_possivel = [x + self.coordenada_x, y + self.coordenada_y]
                    casas_possiveis.append(movimento_possivel)

        return casas_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Rainha(Pedra):

    def __init__(self, cor):

        super().__init__()
        self.name = 'Rainha'
        self.Cor = cor
        self.coordenada_x = 3

        if cor == Cor.Branca:
            self.coordenada_y = 0
        elif cor == Cor.Preta:
            self.coordenada_y = 7

        self.posicao_inicial_tabuleiro = [self.coordenada_x, self.coordenada_y]

    def movimentos_direcao_unica(self, contador_x, contador_y):
        todos_movimentos = []

        while 0 <= contador_x + self.coordenada_x <= 7 and 0 <= contador_y + self.coordenada_y <= 7:
            movimento_possivel = [contador_x + self.coordenada_x, contador_y + self.coordenada_y]
            todos_movimentos.append(movimento_possivel)

            if contador_x > 0:
                contador_x += 1
            else:
                contador_x -= 1

            if contador_y > 0:
                contador_y += 1
            else:
                contador_y -= 1

        return todos_movimentos

    def todos_movimentos(self):
        casas_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_direcao_unica(x, y))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                casas_possiveis.append(movimento)

        contador_x = 0

        while contador_x <= 7:
            if contador_x != self.coordenada_x:
                movimento_possivel = [contador_x, self.coordenada_y]
                casas_possiveis.append(movimento_possivel)
            contador_x += 1

        contador_y = 0

        while contador_y <= 7:
            if contador_y != self.coordenada_y:
                movimento_possivel = [self.coordenada_x, contador_y]
                casas_possiveis.append(movimento_possivel)
            contador_y += 1

        return casas_possiveis

    def mover(self, casa_origem , casa_destino):
        print("movido")


class Cor(enum.Enum):
    Branca = 0
    Preta = 1


class Lado(enum.Enum):
    Rei = 0
    Rainha = 1
