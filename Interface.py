from tkinter import *
class Interface:

    def __init__ (self,titulo ='default',x = 800, y = 600 ):

         #gera a janela            
        self.janela = Tk()
        self.janela.iconbitmap('icones/agronomia_icone.ico')
        self.janela.title(f"{titulo}")
        self.janela.geometry(f"{x}x{y}")

        #mostra o rotulo de bem vindo
        label_bv = Label(
            self.janela,
            text='Bem vindo ao JupAuto',
            background='#e0e0e0',
            font='Arial 15',
            border=15,
            width=x,
            height=2,
            anchor=CENTER
        )
        
        label_bv.pack()

        #armazena uma referência ao objeto Botao
        self.botao = Botao(self.janela, 'Clique aqui', self.acao)

    def acao(self):
        from tkinter import filedialog
        self.abre_pasta = Tk()
        self.abre_pasta.withdraw()
        Interface.selecionar_pasta = filedialog.askdirectory()
        print(Interface.selecionar_pasta)
        
class Botao:

    def __init__(self,janela,texto,acao):
        
        botaos = Button(janela,
                        text=f'{texto}',
                        command=acao,
                        background='#d9d9d9',
                        font='Arial 10',
                        border=5)
        
        botaos.place(x=50,y=100)

        
janela = Interface()
janela.janela.mainloop()