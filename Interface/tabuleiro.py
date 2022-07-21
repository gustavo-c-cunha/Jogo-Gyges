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
        self.posicaoMExtra = None
        self.jogadores = [Jogador(0), Jogador(1)]
        self.estadoMovimento = 0

    def setJogoEmAndamento(self, estado):
        self.jogoEmAndamento = estado
    
    def getCasas(self):
        return self.casas

    def getEstado(self):
        return self.estadoMovimento

    def setEstado(self, estado):
        self.estadoMovimento = estado

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
        self.setEstado(0)

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
        if self.estadoMovimento == 1:
            iInicial = self.pecaSelecionada.getCoordenadas()[0]
            jInicial = self.pecaSelecionada.getCoordenadas()[1]
        else:
            iInicial = self.posicaoMExtra[0]
            jInicial = self.posicaoMExtra[1]
        soma = abs(iInicial-linha) + abs(jInicial-coluna)
        n = self.pecaSelecionada.getPecaPosicao().getCasasMovimento()
        if n == soma:
            return True
        else:
            return False

    def selecionarPeca(self, linha, coluna):
        # não tem retorno 
        if self.casas[linha][coluna].getOcupada() == False:
            print("casa vazia")
        elif self.verificarPeca(self.casas[linha][coluna]):
            self.pecaSelecionada = self.casas[linha][coluna]
            self.setEstado(1)
        else:
            print("casa falhou na verificacao")

    def selecionarDestino(self, linha, coluna):
        # não tem retorno
        if self.verificarDestino(linha, coluna):
            print("destino valido")
            if self.verificarCasaVitoria():
                return str(self.jogadorDaVez.getJogador())
            else:
                if self.verificarCasaVazia(self.casas[linha][coluna]):
                    self.pecaSelecionada.getPecaPosicao().resetarPeca()
                    self.pecaSelecionada.moverPeca(self.casas[linha][coluna])
                    self.getProximoJogador()
                    self.setEstado(0)
                else:
                    self.posicaoMExtra = (linha, coluna)
                    self.pecaSelecionada.getPecaPosicao().incrementarMovimento(self.casas[linha][coluna].getPecaPosicao().getTipo())
                    self.setEstado(2)
        else:
            if self.estadoMovimento == 2:
                if self.validarDestinoR(linha, coluna):
                    if self.verificarColuna(coluna):
                        self.pecaSelecionada.getPecaPosicao().resetarPeca()
                        self.casas[self.posicaoMExtra[0]][self.posicaoMExtra[1]].moverPeca(self.casas[linha][coluna])
                        self.pecaSelecionada.moverPeca(self.casas[self.posicaoMExtra[0]][self.posicaoMExtra[1]])
                        self.getProximoJogador()
                        print(self.jogadorDaVez.getJogador())
                        print("reposicionado")
                        self.setEstado(0)
                    else:
                        print("coluna invalida")
                else:
                    print("destino invalido")
            else:
                print("destino invalido")


    def verificarCasaVitoria(self):
        # retorna boolean
        if self.casas[0][0].getPecaPosicao() != None:
            return True
        elif self.casas[0][7].getPecaPosicao() != None:
            return True
        else:
            return False

    def verificarPeca(self, posicao):
        # retorna boolean
        if self.jogadorDaVez.getJogador() == 0:
            inicio = 1
            fim = posicao.getCoordenadas()[1]
            if inicio == fim:
                return True
        else:
            inicio = posicao.getCoordenadas()[1]
            fim = 6
            if inicio == fim:
                return True
        for i in range(inicio, fim):
            for j in range(6):
                casa = self.casas[j][i].getOcupada()
                if casa:
                    if (self.jogadorDaVez.getJogador() == 0 and i == fim) or (self.jogadorDaVez.getJogador() == 1 and i == fim):
                        print("caso extranho")
                        pass
                    else:
                        return False
        return True

    def verificarCasaVazia(self, posicao):
        # retorna boolean
        return not(posicao.getOcupada())

    def definirJogadorInicial(self):
        # retorna um inteiro
        numero = randrange(10)
        resultado = numero%2
        return resultado

    def validarDestinoR(self, linha, coluna):
        destino = self.casas[linha][coluna]
        ocupada = destino.getOcupada()
        if ocupada:
            return False
        else:
            return True

    def verificarColuna(self, coluna):
        # retorna boolean
        if self.jogadorDaVez.getJogador() == 1:
            inicio = 1
            fim = coluna
        else:
            inicio = coluna
            fim = 7
        for i in range(inicio, fim):
            for j in range(6):
                casa = self.casas[j][i].getOcupada()
                if casa:
                    return True
        return False