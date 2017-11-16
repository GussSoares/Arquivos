#encoding: UTF8
from tkinter import *
import time, os
from threading import Thread, Semaphore

buffer1 = [""]                          # buffer1
buffer2 = [""]                          # buffer2

def interface(master,buffer1,buffer2,semaphore):                              # criacao das janelas
    fontePadrao = ("Arial", "10")                           # fonte padrao
    label = Label(master, text="Enter text")                # label de indicação
    label.pack(side="top")                                  # posicao do label
    text_box = Text(master, height=5, width=50)             # caixa de texto que recebera a escrita
    text_box.pack(side="top")                               # posicao da caixa de texto


    def refreshWrite():
        while True:
            semaphore.acquire()
            buffer1[0] = text_box.get(1.0, END)               # recebe o texto escrito
            semaphore.release()
            time.sleep(.1)


    def refreshRead():
        while True:
            text = buffer2[0]                                # cria-se uma variavel auxiliar para armazear a msg escrita
            semaphore.acquire()
            if text != nomeLabel.cget("text"):
                nomeLabel.config(text=text)                 # seta o label para a msg escrita

            semaphore.release()
            time.sleep(.1)


    nomeLabel = Label(master,font=fontePadrao)             # criacao do label q recebera a msg escrita na caixa de texto
    label = Label(master,text="Output")
    label.pack(side="top")
    nomeLabel["height"] = 5
    nomeLabel["width"] = 50
    nomeLabel.config(wraplength=350)                        # quebra de linha
    nomeLabel.pack()
    time.sleep(.1)

    thread1 = Thread(target=refreshWrite)                   # thread de escrita
    thread2 = Thread(target=refreshRead)                    # thread de leitura
    thread1.start()
    thread2.start()

    if master is None:
        os.popen("pkill -9 python")
        os.waitpid()

root = Tk()
w1 = Toplevel()
root.title("Tela 1")# cria multiplas janelas
w1.title("Tela 2")

smf1 = Semaphore()

interface(root, buffer1, buffer2, smf1)
interface(w1, buffer2, buffer1, smf1)
# print(root.state())

root.mainloop()
os.popen("pkill python")