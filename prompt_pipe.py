#encoding: UTF8
from multiprocessing import *
from tkinter import *
import time
import threading

def soon(name, read, write):                        # processo pai
    def interface(master=None):                     # criacao das janelas
        fontePadrao = ("Arial", "10")               # fonte padrao
        label = Label(master, text="Enter text")    # label de indicação
        label.pack(side="top")                      # posicao do label
        text_box = Text(master, height=10, width=30)# caixa de texto que recebera a escrita
        text_box.pack(side="top")                   # posicao da caixa de texto

        def refreshWrite():                         # escrita
            while True:
                write.send(text_box.get(1.0, END))  # captura o texto escrito
                time.sleep(.10)                     # delay de 10ms

        def refreshRead():                          # leitura
            while True:
                text = read.recv()                  # cria-se uma variavel auxiliar para armazear a msg escrita
                if text != nomeLabel.cget("text"):
                    nomeLabel.config(text=text)     # seta o label para a msg escrita
            time.sleep(.10)                         #delay de 10ms

        nomeLabel = Label(master, font=fontePadrao) # criacao do label q recebera a msg escrita na caixa de texto
        nomeLabel["width"] = 30
        nomeLabel["height"] = 10
        nomeLabel.config(wraplength=100)            # quebra de linha
        nomeLabel.pack()

        thread1 = threading.Thread(target=refreshWrite) # thread de escrita
        thread2 = threading.Thread(target=refreshRead)  # thread de leitura
        thread1.start()                             # inicia a thread
        thread2.start()                             # inicia a thread

    root = Tk()
    interface(root)
    root.title(name)
    root.mainloop()                                 # inicializa a interface


def father():

    read1, write1 = Pipe()                          # cria os pipes
    read2, write2 = Pipe()                          # cria os pipes
    # cria os processos
    process1 = Process(target=soon, args=("SOON_1", read1, write2)) # le do 1, escreve no 2.
    process2 = Process(target=soon, args=("SOON_2", read2, write1)) # le do 2, escreve no 1.
    process1.start()
    process2.start()

def main():
    father()

if __name__ == '__main__':
    main()
