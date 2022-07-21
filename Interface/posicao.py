from sqlalchemy import false, null


class Posicao():
    
    def __init__(self, coord, vitoria):
        self.coordenadas = coord
        self.ocupada = False
        self.pecaPosicao = None
        self.casaVitoria = vitoria

    def posicionarPeca(self, peca):
        self.pecaPosicao = peca
        self.ocupada = True

    def resetarPosicao(self):
        self.ocupada = False
        self.pecaPosicao = None

    def posicaoSelecionada(self):
        return self

    def moverPeca(self, posicao):
        self.ocupada = False
        posicao.posicionarPeca(self.pecaPosicao)
        self.pecaPosicao = None

    def getPecaPosicao(self):
        return self.pecaPosicao

    def getCoordenadas(self):
        return self.coordenadas

    def getOcupada(self):
        return self.ocupada