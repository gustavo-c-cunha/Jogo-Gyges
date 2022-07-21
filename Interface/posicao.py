from sqlalchemy import false, null


class Posicao():
    
    def __init__(self, coord, vitoria):
        self.coordenadas = coord
        self.ocupada = False
        self.pecaPosicao = None
        self.casaVitoria = vitoria

    def posicionarPeca(self, peca):
        self.pecaPosicao = peca

    def resetarPosicao(self):
        self.ocupada = False
        self.pecaPosicao = None

    def posicaoSelecionada(self):
        return self

    def moverPeca(self, posicao):
        self.ocupada = False
        posicao.posicionarPeca(self.pecaPosicao)
        self.pecaPosicao = None