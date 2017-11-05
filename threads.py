#encoding: UTF8
from threading import Thread
from Tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master, height=300, width=300)
        self.segundoContainer.pack()

        # self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        # self.titulo["font"] = ("Arial", "10", "bold")
        # self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, font=self.fontePadrao)
        self.nomeLabel.pack(side=RIGHT)

        self.tela1 = Text(self.segundoContainer, height=10, width=10)
        self.tela1["width"] = 30
        self.tela1.pack(side=RIGHT)

class Th(Thread):
    def  __init__ (self, num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        root = Tk()
        Application(root)
        root.mainloop()

a = Th(1)
a.start()
b = Th(2)
b.start()
