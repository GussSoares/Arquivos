#encoding: UTF8
from multiprocessing import *
from tkinter import *
import time
import threading

# from teste import *

def soon(name, read, write):
    def interface(master=None):
        fontePadrao = ("Arial", "10")
        label = Label(master, text="Digite aqui")
        label.pack(side="top")
        text_box = Text(master, height=10, width=30)
        text_box.pack(side="top")

        def refreshWrite():
            while True:
                write.send(text_box.get(1.0, END))
                time.sleep(.10)
        def refreshRead():
            while True:
                aux = read.recv()
                if aux != nomeLabel.cget("text"):
                    nomeLabel.config(text=aux)
            time.sleep(.10)

        nomeLabel = Label(master, font=fontePadrao)
        nomeLabel["width"] = 30
        nomeLabel["height"] = 10
        nomeLabel.config(wraplength=100)
        nomeLabel.pack()

        thread1 = threading.Thread(target=refreshWrite)
        thread2 = threading.Thread(target=refreshRead)
        thread1.start()
        thread2.start()

    root = Tk()
    interface(root)
    root.title("Prompt")
    root.mainloop()

def father():
    read1, write1 = Pipe()
    read2, write2 = Pipe()

    process1 = Process(target=soon, args=("SOON_1", read1, write2))
    process2 = Process(target=soon, args=("SOON_2", read2, write1))
    process1.start()
    process2.start()

father()
