import tkinter as tk

janela = tk.Tk()

def tela():
    janela.title("Provavelmente vai ser uma calculadora")
    janela.configure(background='purple')
    janela.geometry("400x320")
    janela.resizable(True, True)
    janela.maxsize(width=860, height=640)
    janela.minsize(width=200, height=160)
tela()


texto = tk.Label(janela, text="arigato")
texto.pack()


def botaor():
    texto['text'] = "aaaaaahhhnnnn"







        


tk.Button(janela, text="me aperte", command=botaor).pack()


janela.mainloop()
