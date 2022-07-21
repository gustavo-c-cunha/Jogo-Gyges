from posicao import Posicao
from peca import Peca
from jogador import Jogador
from random import randrange
class Tabuleiro():
    def __init__(self):
        self.casas = [[None for x in range(8)] for y in range(6)]
        self.jogoEmAndamento = False
        self.jogadorDaVez = None
        self.jogoFinalizado = None
        self.pecaSelecionada = None
        self.jogadores = [Jogador(0), Jogador(1)]

    def setJogoEmAndamento(self, estado):
        self.jogoEmAndamento = estado
    
    def getCasas(self):
        return self.casas

    def verificarPartida(self):
        # retorna um boolean
        if not(self.jogoEmAndamento):
            for coluna in range(8):
                for linha in range(6):
                    if coluna == 0 or coluna == 7:
                        self.casas[linha][coluna] = Posicao((linha,coluna), True)
                        break
                    else:
                        self.casas[linha][coluna] = Posicao((linha,coluna),False)
                        if coluna == 1 or coluna == 6:
                            if linha == 0 or linha == 5:
                                peca = Peca(3)
                            elif linha == 1 or linha == 4:
                                peca = Peca(2)
                            else:
                                peca = Peca(1)
                            self.casas[linha][coluna].posicionarPeca(peca)
            self.jogadorDaVez = self.jogadores[self.definirJogadorInicial()]
        return self.jogoEmAndamento

    def limparTabuleiro(self):
        # não tem retorno
        self.jogadores[0].resetarJogador()
        self.jogadores[1].resetarJogador()
        for coluna in range(8):
            for linha in range(6):
                if coluna == 0 or coluna == 7:
                    self.casas[linha][coluna].resetarPosicao()
                    break
                else:
                    self.casas[linha][coluna].resetarPosicao()
        self.setJogoEmAndamento(False)

    def getProximoJogador(self):
        # retorna um jogador
        lado = self.jogadorDaVez.getJogador()
        if lado == 0:
            self.jogadorDaVez = self.jogadores[1]
        else:
            self.jogadorDaVez = self.jogadores[0]
        return self.jogadorDaVez

    def verificarDestino(self, linha, coluna):
        # retorna boolean
        pass

    def selecionarPeca(self, linha, coluna):
        # não tem retorno 
        pass

    def selecionarDestino(self, linha, coluna):
        # não tem retorno
        pass

    def verificarCasaVitoria(self):
        # retorna boolean
        pass

    def verificarPeca(self, posicao):
        # retorna boolean
        pass

    def verificarCasaVazia(self, posicao):
        # retorna boolean
        pass

    def definirJogadorInicial(self):
        # retorna um inteiro
        numero = randrange(10)
        resultado = numero%2
        return resultado

    def validarDestinoR(self, linha, coluna):
        # retorna boolean
        pass

    def verificarColuna(self, linha):
        # retorna boolean
        pass