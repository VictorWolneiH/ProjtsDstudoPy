import tkinter as tk

janela = tk.Tk()


class Application():
    def __init__(self):
        self.janela = janela
        self.tela()
        janela.mainloop()

    def tela(self):
        self. janela.title("Provavelmente uma calculadora")
        self.janela.configure(background='purple')
        self.janela.geometry("400x320")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=860, height=640)
        self.janela.minsize(width=200, height=160)




Application()