class Tabuleiro():
    def __init__(self):
        self.casas = None
        self.jogoEmAndamento = False
        self.jogadorDaVez = None
        self.jogoFinalizado = None
        self.pecaSelecionada = None

    def verificarPartida(self):
        # retorna um boolean
        pass

    def limparTabuleiro(self):
        # não tem retorno
        pass

    def getProximoJogador(self):
        # retorna um jogador
        pass

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
        pass

    def validarDestinoR(self, linha, coluna):
        # retorna boolean
        pass

    def verificarColuna(self, linha):
        # retorna boolean
        pass