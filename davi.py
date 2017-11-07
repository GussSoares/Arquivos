# import os

# def child():
#    print('\nA new child ',  os.getpid())
#    os._exit(0)  

# def parent():
#    while True:
#       newpid = os.fork()
#       if newpid == 0:
#          child()
#       else:
#          pids = (os.getpid(), newpid)
#          print("parent: %d, child: %d\n" % pids)
#       reply = input("q for quit / c for new fork")
#       if reply == 'c': 
#           continue
#       else:
#           break

# parent()

from tkinter import *
import time
import threading

def filho(nome, r, w):

  print(id(r[0]))
  print(id(w[0]))

  def vailogo(master):

    print("2")

    prompt = Label(master, text="Insere algo")
    prompt.pack(side="top")

    print("100")

    texto = Text(master, width=15, height=5)
    texto.pack(side="left")

    label = Label(master, text="", borderwidth=1, relief="groove")
    label["width"] = 15
    label["height"] = 5
    label.config(wraplength = 100)
    label.pack(side="top")

    print("3")

    # FILHO 1       q1[0] -> le          q2[1] -> escreve
    # FILHO 2       q1[1] -> le          q2[0] -> escreve

    def atualizaEscrita():
      while 1:
        w[0] = texto.get(1.0, END)
        time.sleep(.1000)

    def atualizaLeitura():
      while 1:

        aux = r[0]

        if aux != label.cget("text"):
          label.config(text = aux)

        time.sleep(.1000)

    t1 = threading.Thread(target=atualizaEscrita)
    t2 = threading.Thread(target=atualizaLeitura)
    t1.start()
    t2.start()

  print("1")

  root = Tk()
  root.title(nome)
  vailogo(root)
  root.mainloop()

def pai():

  print("sda")

  q1 = [""]
  q2 = [""]

  t1 = threading.Thread(target=filho, args=("FILHO 1",q1, q2,))
  t2 = threading.Thread(target=filho, args=("FILHO 2",q2, q1,))
  t1.start()
  t2.start()

pai()