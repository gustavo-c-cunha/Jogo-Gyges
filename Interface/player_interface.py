from tkinter import *
from tabuleiro import Tabuleiro
from pprint import pprint
class PlayerInterface:
    def __init__(self):

        self.main_window = Tk()
        self.board = Tabuleiro()
        self.fill_main_window()
        self.main_window.mainloop()

    def fill_main_window(self):
       
        # Título, ícone, dimensionamento e fundo da janela
        self.main_window.title("Jogo Gyges")
        self.main_window.iconbitmap("images/Gyges32.ico")
        self.main_window.geometry("1280x720")
        self.main_window.resizable(False, False)
        self.main_window["bg"]="#291A3B" #4D2C61

        # Criação de 4 frames e organização da janela em um grid de 2 linhas e 5 colunas,
        # sendo que table_frame ocupa a linha inferior e message_frame, a superior e
        # padding apenas é utilizado para centralizar as outras colunas
        self.paddingL = Label(self.main_window, bg="#291A3B")
        self.paddingL.grid(row=1, column=0, padx=(225,0))
        self.paddingR = Label(self.main_window, bg="#291A3B")
        self.paddingR.grid(row=1, column=4, padx=(0,225))

        self.table_frame_left = Frame(self.main_window, padx=0, pady=10, bg="#291A3B")
        self.table_frame_left.grid(row=1 , column=1)
        self.table_frame_center = Frame(self.main_window, padx=0, pady=10, bg="#291A3B")
        self.table_frame_center.grid(row=1 , column=2)
        self.table_frame_right = Frame(self.main_window, padx=0, pady=10, bg="#291A3B")
        self.table_frame_right.grid(row=1 , column=3)

        self.message_frame = Frame(self.main_window, padx=0, pady=10, bg="#291A3B")
        self.message_frame.grid(row=0 , column=2)

        # Definição das imagens do tabuleiro
        self.empty_space = PhotoImage(file="images/white_square.png")
        self.peca1 = PhotoImage(file="images/piece1.png")
        self.peca2 = PhotoImage(file="images/piece2.png")
        self.peca3 = PhotoImage(file="images/piece3.png")
        self.logo = PhotoImage(file="images/Gyges64.png")

        # Preenchimento de table_frame com 38 imagens iguais, organizadas em 6 linhas e 8 colunas, com coluna 0 e 7 diferentes
        self.board_view=[]
        for y in range(8):
            a_column = [] # column
            if y == 0:
                aLabel = Label(self.table_frame_left, bd = 0, image=self.empty_space)
                aLabel.grid(row=0 , column=y)
                aLabel.bind("<Button-1>", lambda event, a_line=0, a_column=y: self.click(event, a_line, a_column))
                a_column.append(aLabel)
            elif y == 7:
                aLabel = Label(self.table_frame_right, bd = 0, image=self.empty_space)
                aLabel.grid(row=0 , column=y)
                aLabel.bind("<Button-1>", lambda event, a_line=0, a_column=y: self.click(event, a_line, a_column))
                a_column.append(aLabel)
            else:
                for x in range(6):
                    aLabel = Label(self.table_frame_center, bd = 0, image=self.empty_space)
                    aLabel.grid(row=x , column=y)
                    aLabel.bind("<Button-1>", lambda event, a_line=x, a_column=y: self.click(event, a_line, a_column))
                    a_column.append(aLabel)
            self.board_view.append(a_column)

        # Preenchimento de message_frame com 1 imagem com logo (label) e 1 label com texto,
        # organizadas em 1 linha e 2 colunas
        self.logo_label = Label(self.message_frame, bd = 0, image=self.logo)
        self.logo_label.grid(row=0, column=0)
        self.message_label = Label(self.message_frame, bg="#291A3B", text=' Gyges', font="arial 30", fg="white")
        self.message_label.grid(row=0, column=1)

        # Definição do menu de jogo
        self.menubar = Menu(self.main_window)
        self.menubar.option_add('*tearOff', FALSE)
        self.main_window['menu'] = self.menubar
        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label='Menu')
        self.menu_file.add_command(label='Iniciar jogo', command=self.iniciarPartida)
        self.menu_file.add_command(label='Restaurar estado inicial', command=self.restaurarEstadoInicial)

    def iniciarPartida(self):
        control = self.board.verificarPartida()
        if control == True:
            print('partida em andamento')
        else:
            self.board.setJogoEmAndamento(True)
            self.atualizarInterface()
    def restaurarEstadoInicial(self):
        self.board.limparTabuleiro()
        self.atualizarInterface()

    def atualizarInterface(self):
        casas = self.board.getCasas()
        for coluna in range(8):
            for linha in range(6):
                peca = casas[linha][coluna].getPecaPosicao()
                if peca == None:
                    break
                if coluna == 0 or coluna == 7:
                    if (peca.getTipo()==1):
                        self.board_view[coluna][linha].configure(image=self.peca1)
                        self.board_view[coluna][linha].image = self.peca1
                    elif (peca.getTipo()==2):
                        self.board_view[coluna][linha].configure(image=self.peca2)
                        self.board_view[coluna][linha].image = self.peca2
                    else:
                        self.board_view[coluna][linha].configure(image=self.peca3)
                        self.board_view[coluna][linha].image = self.peca3
                    break
                else:
                    if (peca.getTipo()==1):
                        self.board_view[coluna][linha].configure(image=self.peca1)
                        self.board_view[coluna][linha].image = self.peca1
                    elif (peca.getTipo()==2):
                        self.board_view[coluna][linha].configure(image=self.peca2)
                        self.board_view[coluna][linha].image = self.peca2
                    else:
                        self.board_view[coluna][linha].configure(image=self.peca3)
                        self.board_view[coluna][linha].image = self.peca3

    def click(self, event, line, column):
        print('CLICK', line, column)