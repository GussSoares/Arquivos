#encoding: UTF8
from threading import Thread
from tkinter import *
from questao2_queue import *

def rodar():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# def funcao(master=None):
#     fontePadrao = ("Arial", "10")
#     primeiroContainer = Frame(master)
#     primeiroContainer.pack()
#
#     # .titulo = Label(.primeiroContainer, text="Dados do usuário")
#     # .titulo["font"] = ("Arial", "10", "bold")
#     # .titulo.pack()
#
#     tela1 = Text(primeiroContainer, height=5, width=10)
#     tela1.pack(side=LEFT)
#
#     nomeLabel = Label(primeiroContainer, font=fontePadrao)
#     nomeLabel["width"] = 10
#     nomeLabel["height"] = 5
#     nomeLabel.pack()
#
#     def teste(event):
#         print(tela1.get(1.0, END))
#         if nomeLabel.cget("text") != tela1.get(1.0, END):
#             nomeLabel.config(text = tela1.get(1.0, END))
#
#     tela1.bind("<KeyRelease>",teste)
#
#
# class Th(Thread):
#     def  __init__ (self):
#         Thread.__init__(self)
#
#     def run(self):
#         root = Tk()
#         funcao(root)
#         root.mainloop()
