# o metodo __init__ ele sempre vai ser inicializado no começo da sua classe

class Tv:
    def __init__(self):
        self.cor = "preta"
        self.ligado = False
        self.tamanho = 55

tv_sala = Tv()
tv_sala.ligado = True