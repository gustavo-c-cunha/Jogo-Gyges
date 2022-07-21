class Peca():

    def __init__(self, tipo):
        self.tipo = tipo
        self.casasMovimento = tipo

    def incrementarMovimento(self, movimentos):
        self.casasMovimento = movimentos

    def resetarPeca(self):
        self.casasMovimento = self.tipo
    
    def getTipo(self):
        return self.tipo

    def getCasasMovimento(self):
        return self.casasMovimento