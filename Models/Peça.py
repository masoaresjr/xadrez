from abc import abstractmethod
import enum


class Peça:

    def __init__(self):

        self.Cor = None
        self.posicao_x = None
        self.posicao_y = None
        self.name = None

    @abstractmethod
    def todos_movimentos(self):
        pass

    @abstractmethod
    def mover(self, casa_origem, casa_destino):
        pass


class Peao(Peça):

    def __init__(self, cor, posicao_x):

        super().__init__()
        self.primeiro_movimento = True
        self.name = 'Peao'
        self.Cor = cor
        self.posicao_x = posicao_x

        if cor == Cor.Branca:
            self.posicao_y = 1
        elif cor == Cor.Preta:
            self.posicao_y = 6

        self.posicao_inicial_tabuleiro = [self.posicao_x, self.posicao_y]

    def todos_movimentos(self):
        posicoes_possiveis = []

        if self.Cor == Cor.Branca:
            movimento_y = [1]
            if self.primeiro_movimento:
                movimento_y.append(2)
        else:
            movimento_y = [-1]
            if self.primeiro_movimento:
                movimento_y.append(-2)

        for casa in movimento_y:
            movimento_possivel = [self.posicao_x, self.posicao_y + casa]
            posicoes_possiveis.append(movimento_possivel)

        return posicoes_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Torre(Peça):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Torre'
        self.Cor = cor
        self.Lado = lado

        if cor == Cor.Branca:
            self.posicao_y = 0
        elif cor == Cor.Preta:
            self.posicao_y = 7

        if lado == Lado.Rei:
            self.posicao_x = 7
        elif lado == Lado.Rainha:
            self.posicao_x = 0

        self.posicao_inicial_tabuleiro = [self.posicao_x, self.posicao_y]

    def todos_movimentos(self):
        posicoes_possiveis = []

        contador_x = 0

        while contador_x <= 7:
            if contador_x != self.posicao_x:
                movimento_possivel = [contador_x, self.posicao_x]
                posicoes_possiveis.append(movimento_possivel)
            contador_x += 1

        contador_y = 0

        while contador_y <= 7:
            if contador_y != self.posicao_y:
                movimento_possivel = [self.posicao_y, contador_y]
                posicoes_possiveis.append(movimento_possivel)
            contador_y += 1

        return posicoes_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Cavalo(Peça):

    def test(self):
        print("Cavalo")

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Cavalo'
        self.Cor = cor
        self.Lado = lado

        if cor == Cor.Branca:
            self.posicao_y = 0
        elif cor == Cor.Preta:
            self.posicao_y = 7

        if lado == Lado.Rei:
            self.posicao_x = 6
        elif lado == Lado.Rainha:
            self.posicao_x = 1

        self.posicao_inicial_tabuleiro = [self.posicao_x, self.posicao_y]

    def todos_movimentos(self):
        posicoes_possiveis = []

        movimentos_x = [-1, 1]
        movimentos_y = [2, -2]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= y + self.posicao_y <= 7 and 0 <= x + self.posicao_x <= 7:
                    movimento_possivel = [x + self.posicao_x, y + self.posicao_y]
                    posicoes_possiveis.append(movimento_possivel)

        movimentos_x = [-2, 2]
        movimentos_y = [1, -1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.posicao_x <= 7 and 0 <= y + self.posicao_y <= 7:
                    movimento_possivel = [x + self.posicao_x, y + self.posicao_y]
                    posicoes_possiveis.append(movimento_possivel)

        return posicoes_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Bispo(Peça):

    def __init__(self, cor, lado):

        super().__init__()
        self.name = 'Bispo'
        self.Cor = cor
        self.Lado = lado

        if cor == Cor.Branca:
            self.posicao_y = 0
        elif cor == Cor.Preta:
            self.posicao_y = 7

        if lado == Lado.Rei:
            self.posicao_x = 5
        elif lado == Lado.Rainha:
            self.posicao_x = 2

        self.posicao_inicial_tabuleiro = [self.posicao_x, self.posicao_y]

    def movimentos_direcao_unica(self, contador_x, contador_y):
        todos_movimentos = []

        while 0 <= contador_x + self.posicao_x <= 7 and 0 <= contador_y + self.posicao_y <= 7:
            movimento_possivel = [contador_x + self.posicao_x, contador_y + self.posicao_y]
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
        posicoes_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_direcao_unica(x, y))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                posicoes_possiveis.append(movimento)

        return posicoes_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Rei(Peça):

    def __init__(self, cor):

        super().__init__()
        self.name = 'Rei'
        self.Cor = cor
        self.posicao_x = 4

        if cor == Cor.Branca:
            self.posicao_y = 0
        elif cor == Cor.Preta:
            self.posicao_y = 7

        self.posicao_inicial_tabuleiro = [self.posicao_x, self.posicao_y]

    def todos_movimentos(self):
        posicoes_possiveis = []

        movimentos_x = [-1, 0, 1]
        movimentos_y = [-1, 0, 1]

        for x in movimentos_x:
            for y in movimentos_y:
                if 0 <= x + self.posicao_x <= 7 and 0 <= y + self.posicao_y <= 7 and (x != 0 or y != 0):
                    movimento_possivel = [x + self.posicao_x, y + self.posicao_y]
                    posicoes_possiveis.append(movimento_possivel)

        return posicoes_possiveis

    def mover(self, casa_origem, casa_destino):
        print("movido")


class Rainha(Peça):

    def __init__(self, cor):

        super().__init__()
        self.name = 'Rainha'
        self.Cor = cor
        self.posicao_x = 3

        if cor == Cor.Branca:
            self.posicao_y = 0
        elif cor == Cor.Preta:
            self.posicao_y = 7

        self.posicao_inicial_tabuleiro = [self.posicao_x, self.posicao_y]

    def movimentos_direcao_unica(self, contador_x, contador_y):
        todos_movimentos = []

        while 0 <= contador_x + self.posicao_x <= 7 and 0 <= contador_y + self.posicao_y <= 7:
            movimento_possivel = [contador_x + self.posicao_x, contador_y + self.posicao_y]
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
        posicoes_possiveis = []

        contador_x = [1, -1]
        contador_y = [1, -1]

        movimentos_direcao_unica = []
        for x in contador_x:
            for y in contador_y:
                movimentos_direcao_unica.append(self.movimentos_direcao_unica(x, y))

        for direcao in movimentos_direcao_unica:
            for movimento in direcao:
                posicoes_possiveis.append(movimento)

        contador_x = 0

        while contador_x <= 7:
            if contador_x != self.posicao_x:
                movimento_possivel = [contador_x, self.posicao_y]
                posicoes_possiveis.append(movimento_possivel)
            contador_x += 1

        contador_y = 0

        while contador_y <= 7:
            if contador_y != self.posicao_y:
                movimento_possivel = [self.posicao_x, contador_y]
                posicoes_possiveis.append(movimento_possivel)
            contador_y += 1

        return posicoes_possiveis

    def mover(self, casa_origem , casa_destino):
        print("movido")


class Cor(enum.Enum):
    Branca = 0
    Preta = 1


class Lado(enum.Enum):
    Rei = 0
    Rainha = 1
