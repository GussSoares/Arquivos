import os, time
from tkinter import *

def search(text_box, initial_path):
    list=[""]
    for path, dirs, files in os.walk(initial_path):
        for f in files:
            if text_box.lower() in f.lower():
                list.append(str(path+f))
    return list

def interface(initial_path):

    def window(master=None):

        fontePadrao = ("Arial", "10")               # fonte padrao
        label = Label(master, text="Enter text")
        label.pack(side="top")
        text_box = Text(master, height=1, width=20)
        text_box.pack(side="top")
        nomeLabel = Label(master, font=fontePadrao)  # criacao do label q recebera a msg escrita na caixa de texto

        nomeLabel["height"] = 5
        nomeLabel["width"] = 50
        nomeLabel.config(wraplength=350)  # quebra de linha
        nomeLabel.pack()
        button = Button(master, text="Search", command=lambda: interface2(search(text_box.get(1.0, END).replace('\n',""), initial_path))).pack()
        # print(texto)
        #
    root = Tk()
    window(root)
    root.mainloop()


def interface2(list):

    def window2(master=None):


        label = Label(master, text=str(list).replace("{","").replace("}","").replace("[","").replace("]","").replace("'","").replace(",",'\n\n'))
        label["height"] = 30
        label["width"] = 100
        label.config(wraplength=500)
        label.grid(row=5, columns=1)
        label.pack(side="top")


    root = Tk()
    window2(root)
    root.mainloop()


if __name__ == '__main__':
    print(search("deepin", "/home/gustavo/"))
    interface("/home/gustavo/")
    # interface2()