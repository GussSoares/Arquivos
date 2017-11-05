#encoding: UTF8
from threading import Thread
from Tkinter import *

# class Application:
#     def __init__(self, master=None):
#         self.fontePadrao = ("Arial", "10")
#         self.primeiroContainer = Frame(master, height=300, width=300)
#         self.primeiroContainer.pack()
#
#         self.segundoContainer = Frame(master)
#         self.segundoContainer.pack()
#
#         # self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
#         # self.titulo["font"] = ("Arial", "10", "bold")
#         # self.titulo.pack()
#
#         self.nomeLabel = Label(self.segundoContainer, font=self.fontePadrao)
#         self.nomeLabel.pack()
#
#         self.tela1 = Text(self.primeiroContainer, height=5, width=10)
#         self.tela1.pack(side=LEFT)
#
# class Th(Thread):
#     def  __init__ (self, num):
#         Thread.__init__(self)
#         self.num = num
#
#     def run(self):
# root = Tk()
# Application(root)
# root.mainloop()
#
# a = Th(1)
# a.start()
# b = Th(2)
# b.start()


root = Tk()
root.title('how to get text from textbox')


#**********************************
mystring = StringVar()

####define the function that the signup button will do
def getvalue():
   Label(root, text=mystring.get()).grid(row=3, column=1)
#*************************************

Label(root, text="Text to get").grid(row=0, sticky=W)  #label
Entry(root, textvariable = mystring).grid(row=0, column=1, sticky=E) #entry textbox

WSignUp = Button(root, text="print text", command=getvalue).grid(row=3, column=0, sticky=W) #button

root.mainloop()
