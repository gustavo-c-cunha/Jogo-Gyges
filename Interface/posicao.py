from sqlalchemy import false, null


class Posicao():
    
    def __init__(self, coord, vitoria):

        self.coordenadas = coord
        self.ocupada = false
        self.pecaPosicao = null
        self.casaVitoria = vitoria

    def posicionarPeca(self, peca):
        self.pecaPosicao = peca
        pass

    def resetarPosicao(self):
        self.ocupada = false
        self.pecaPosicao = null

    def posicaoSelecionada(self):
        return self

    def moverPeca(self, posicao):
        self.ocupada = false
        posicao.posicionarPeca(self.pecaPosicao)
        self.pecaPosicao = null