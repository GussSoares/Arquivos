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
from multiprocessing import *

def filho(nome, r, w):

    root = Tk()

    print("2")

    prompt = Label(root, text="Insere algo")
    prompt.pack(side="top")

    print("100")

    texto = Text(root, width=15, height=5)
    texto.pack(side="left")

    label = Label(root, text="", borderwidth=1, relief="groove")
    label["width"] = 15
    label["height"] = 5
    label.config(wraplength = 100)
    label.pack(side="top")

    print("3")

    label.config(text="asduiuidfdfh")

    print("1")

    root.title(nome)
    root.after(100, filho, nome, r, w)
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
