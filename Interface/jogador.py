class Jogador():
    
    def __init__(self, lado):
        self.movimentos = 0
        self.casasPercorridas = []
        self.estaJogando = False
        self.lado = lado
    
    def getJogador(self):
        return self

    def resetarJogador(self):
        self.movimentos = 0
        self.casasPercorridas = []
        self.estaJogando = False