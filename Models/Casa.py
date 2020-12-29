from Models import Peça


class Posição:

    def __init__(self, posiçãoX, posiçãoY, peça=None):
        self.peça = peça
        self.posiçãoX = posiçãoX
        self.posiçãoy = posiçãoY