# o metodo __init__ ele sempre vai ser inicializado no começo da sua classe
from datetime import datetime
import pytz

class Tv:
    cor = 'preta'

    @staticmethod
    def _data_hora(self):
        fuso_horario = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_horario)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self,  ligado, tamanho, canal):
        self.ligado = ligado
        self.tamanho = tamanho
        self.canal = canal

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def _mostrar_preco(self): # metodo privado
        print(2000)

tv_sala = Tv( False, 55, 'Netflix')
tv_sala.ligado = True
tv_sala.mudar_canal("HBO Max")
