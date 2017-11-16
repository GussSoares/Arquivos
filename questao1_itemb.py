#encoding: UTF8
from tkinter import *
import time
from threading import Thread, Semaphore

buffer1 = ["", "", "", "", "", ""]                          # buffer1
buffer2 = ["", "", "", "", "", ""]                          # buffer2
v1 = [buffer1, 0, 0]                                        # vetor para manipular buffer circular
v2 = [buffer2, 0, 0]

def _full(i,f):                                            # verifica se o buffer circular esta cheio (final = inicio-1)
    if f==i-1:
        return True
    return False

def _empty(i,f):                                           # verifica se o buffer circular está vazio (inicio = final-1)
    if i == f-1:
        return True
    return False

def interface(master,v1,v2,semaphore):                              # criacao das janelas
    fontePadrao = ("Arial", "10")                           # fonte padrao
    label = Label(master, text="Enter text")                # label de indicação
    label.pack(side="top")                                  # posicao do label
    text_box = Text(master, height=5, width=50)             # caixa de texto que recebera a escrita
    text_box.pack(side="top")                               # posicao da caixa de texto

    def refreshWrite():                                     # atualiza esrita
        while True:
            if _full(v1[1], v1[2]) is True:                 # se o buffer estiver cheio ele volta e verifica ate não estar mais cheio
                continue

            v1[2] += 1
            semaphore.acquire()
            v1[0][0] = text_box.get(1.0, END)               # recebe o texto escrito
            semaphore.release()
            time.sleep(.1)


    def refreshRead():
        while True:
            if _empty(v2[1], v2[2]) is True:                # se o buffer estiver cheio ele volta e verifica ate não estar mais cheio
                continue

            v2[1] += 1
            text = v2[0][0]                                 # cria-se uma variavel auxiliar para armazear a msg escrita
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
    button = Button(master, text="Close", command=exit).pack()     # botao para fechar as janelas

    thread1 = Thread(target=refreshWrite)                   # thread de escrita
    thread2 = Thread(target=refreshRead)                    # thread de leitura
    thread1.start()
    thread2.start()

root = Tk()
# root.withdraw()
w1 = Toplevel()                                             # cria multiplas janelas
w2 = Toplevel()
smf1 = Semaphore()
smf2 = Semaphore()
interface(w1, v1, v2, smf1)
interface(w2, v2, v1, smf1)
root.mainloop()
