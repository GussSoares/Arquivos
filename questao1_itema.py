# -*- coding: utf-8 -*-
from multiprocessing import *
from tkinter import *
import threading, os, time

# def close():
#    os.popen("pkill python")


def refreshWrite(write, text_box):  # escrita

    while True:
       write.send(text_box.get(1.0, END))  # captura o texto escrito


def refreshRead(read, nomeLabel):                          # leitura

    while True:
       text = read.recv()                  # cria-se uma variavel auxiliar para armazear a msg escrita
       if text != nomeLabel.cget("text"):
           nomeLabel.config(text=text)     # seta o label para a msg escrita


def son(name,read,write):  # processo pai
    print("Process Filho Id: " + str(os.getpid()))
    def interface(master=None):                     # criacao das janelas
        fontePadrao = ("Arial", "10")               # fonte padrao
        label = Label(master, text="Enter text")    # label de indicação
        label.pack(side="top")                      # posicao do label
        text_box = Text(master, height=5, width=50)# caixa de texto que recebera a escrita
        text_box.pack(side="top")                   # posicao da caixa de texto

        nomeLabel = Label(master, font=fontePadrao) # criacao do label q recebera a msg escrita na caixa de texto
        label = Label(master, text="Output")
        label.pack(side="top")
        nomeLabel["height"] = 5
        nomeLabel["width"] = 50
        nomeLabel.config(wraplength=350)            # quebra de linha
        nomeLabel.pack()
        # button = Button(master, text="Close", command=close)
        # button.pack()

        time.sleep(.1)
        thread1 = threading.Thread(target=refreshWrite, args=(write, text_box,)) # thread de escrita
        thread2 = threading.Thread(target=refreshRead, args=(read, nomeLabel,))  # thread de leitura
        thread1.start()                             # inicia a thread
        thread2.start()                             # inicia a thread

    root = Tk()
    interface(root)
    root.title(name)
    root.mainloop()                                 # inicializa a interface


def father():
    print("Process Pai Id: " + str(os.getpid()))
    time.sleep(.1)
    read1, write1 = Pipe()                          # cria os pipes
    read2, write2 = Pipe()                          # cria os pipes

    # p1 = Process(target=son, args=("SON_1", read1, write2))
    # p2 = Process(target=son, args=("SON_2", read2, write1))
    # p1.start()
    # p2.start()

    p1 = os.fork()                                  # cria os forks
    if p1 == 0:                                      # se > 0, é filho
        son("SON_1", read1, write2)                 # cria processo filho1
                                           # senão, é pai
    p2 = os.fork()                              # cria pai
    if p2 == 0:                                  # se > 0, é filho
        son("SON_2", read2, write1)             # cria processo filho2

if __name__ == '__main__':
    father()
