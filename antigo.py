#encoding: UTF8
from threading import Thread
from tkinter import *
# from teste import *

def funcao(master=None):
    fontePadrao = ("Arial", "10")
    # primeiroContainer = Frame(master)
    # primeiroContainer.pack()

    # .titulo = Label(.primeiroContainer, text="Dados do usuário")
    # .titulo["font"] = ("Arial", "10", "bold")
    # .titulo.pack()

    tela1 = Text(master, height=5, width=15)
    tela1.pack(side="left")

    nomeLabel = Label(master, font=fontePadrao)
    nomeLabel["width"] = 15
    nomeLabel["height"] = 5
    nomeLabel.config(wraplength=100)
    nomeLabel.pack()

    def teste(event):
        # print(tela1.get(1.0, END))
        if nomeLabel.cget("text") != tela1.get(1.0, END):
            nomeLabel.config(text = tela1.get(1.0, END))

    tela1.bind("<KeyRelease>",teste)


class Th(Thread):
    def  __init__ (self):
        Thread.__init__(self)

    def run(self):
        root = Tk()
        funcao(root)
        root.mainloop()

a = Th()
a.start()
b = Th()
b.start()
