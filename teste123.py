from multiprocessing import *
from tkinter import *
import time, sys
from threading import Thread

buffer1 = ["", "", "", "", "", ""]
buffer2 = ["", "", "", "", "", ""]
v1 = [buffer1, 0, 0]
v2 = [buffer2, 0, 0]

def _full(i, f):
    if f==i-1:
        return True
    return False

def _empty(i, f):
    if i == f-1:
        return True
    return False

def interface(master, v1, v2):                     # criacao das janelas
    fontePadrao = ("Arial", "10")               # fonte padrao
    label = Label(master, text="Enter text")    # label de indicação
    label.pack(side="top")                      # posicao do label
    text_box = Text(master, height=10, width=30)# caixa de texto que recebera a escrita
    text_box.pack(side="top")                   # posicao da caixa de texto

    def refreshWrite():
                                 # escrita
        while True:
            if _full(v1[1], v1[2]) is True:
                continue
            v1[2]+=1
            # write.send(text_box.get(1.0, END))  # captura o texto escrito
            v1[0][0] = text_box.get(1.0, END)
            time.sleep(.1000)                     # delay de 10ms

    def refreshRead():                          # leitura
        while True:
            if _empty(v2[1], v2[2]) is True:
                continue
            v2[1]+=1
            text = v2[0][0]                 # cria-se uma variavel auxiliar para armazear a msg escrita
            if text != nomeLabel.cget("text"):
                nomeLabel.config(text=text)     # seta o label para a msg escrita
            time.sleep(.1000)                         #delay de 10ms


    nomeLabel = Label(master, font=fontePadrao) # criacao do label q recebera a msg escrita na caixa de texto
    nomeLabel["width"] = 30
    nomeLabel["height"] = 10
    nomeLabel.config(wraplength=100)            # quebra de linha
    nomeLabel.pack()

    thread1 = Thread(target=refreshWrite) # thread de escrita
    thread2 = Thread(target=refreshRead)  # thread de leitura
    thread1.start()                             # inicia a thread
    thread2.start()                             # inicia a thread



root = Tk()
# root.withdraw()
w1 = Toplevel()
w2 = Toplevel()

interface(w1, v1, v2)
interface(w2, v2, v1)
root.mainloop()
