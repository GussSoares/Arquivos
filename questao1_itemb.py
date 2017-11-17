# -*- coding: utf-8 -*-
from tkinter import *
import time, os
from threading import Thread, Semaphore

buffer1 = [""]                          # buffer1
buffer2 = [""]                          # buffer2

def close():
    os.popen("pkill python")


def refreshWrite(semaphore, buffer1, text_box):
    while True:
        semaphore.acquire()
        buffer1[0] = text_box.get(1.0, END)                 # recebe o texto escrito
        semaphore.release()
        time.sleep(.1)


def refreshRead(semaphore, buffer2, nomeLabel):
    while True:
        text = buffer2[0]                                   # cria-se uma variavel auxiliar para armazear a msg escrita
        semaphore.acquire()
        if text != nomeLabel.cget("text"):
            nomeLabel.config(text=text)                     # seta o label para a msg escrita

        semaphore.release()
        time.sleep(.1)


def interface(master,buffer1,buffer2,semaphore):            # criacao das janelas
    fontePadrao = ("Arial", "10")                           # fonte padrao
    label = Label(master, text="Enter text")                # label de indicação
    label.pack(side="top")                                  # posicao do label
    text_box = Text(master, height=5, width=50)             # caixa de texto que recebera a escrita
    text_box.pack(side="top")                               # posicao da caixa de texto

    nomeLabel = Label(master, font=fontePadrao)             # criacao do label q recebera a msg escrita na caixa de texto
    label = Label(master, text="Output")
    label.pack(side="top")
    nomeLabel["height"] = 5
    nomeLabel["width"] = 50
    nomeLabel.config(wraplength=350)                        # quebra de linha
    nomeLabel.pack()
    time.sleep(.1)
    button = Button(master, text="Close", command=close)
    button.pack()

    thread1 = Thread(target=refreshWrite, args=(semaphore, buffer1, text_box,))                      # thread de escrita
    thread2 = Thread(target=refreshRead, args=(semaphore, buffer2, nomeLabel,))                      # thread de leitura
    thread1.start()
    thread2.start()


def main():
    root = Tk()
    w1 = Toplevel()  # cria multiplas janelas

    smf1 = Semaphore()
    interface(root, buffer1, buffer2, smf1)
    interface(w1, buffer2, buffer1, smf1)
    root.mainloop()

if __name__ == '__main__':
    main()