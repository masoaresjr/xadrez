class Tabuleiro:

    def __init__(self):
        self.casas = []

    def pegar_rei(self, cor):
        casa_do_rei = None

        for linha in self.casas:
            for casa in linha:
                if casa.pedra is not None:
                    if casa.pedra.name == "Rei":
                        if casa.pedra.cor == cor:
                            casa_do_rei = casa

        return casa_do_rei
