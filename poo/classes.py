# o metodo __init__ ele sempre vai ser inicializado no começo da sua classe

class Tv:
    def __init__(self, cor, ligado, tamanho, canal):
        self.cor = cor
        self.ligado = ligado
        self.tamanho = tamanho
        self.canal = canal

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

tv_sala = Tv('Preta', False, 55, 'Netflix')
tv_sala.ligado = True
tv_sala.mudar_canal("HBO Max")
