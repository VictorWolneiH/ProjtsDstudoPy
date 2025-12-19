import tkinter as tk
import subprocess

def laucnherP():
    subprocess.Popen([
        "/usr/bin/python3",
        "/home/Sh0tinh4/Documentos/MeusProjetos/teste/grafico.py"
    ])

janela = tk.Tk()
janela.title("Launcher Pessoal")
janela.geometry("120x60")
janela.resizable(False, False)

botao = tk.Button(janela, text="rodar",
command=laucnherP)
botao.pack(expand=True)

janela.mainloop()