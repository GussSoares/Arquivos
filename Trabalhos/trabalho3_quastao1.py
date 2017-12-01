import os, subprocess

def search(word):
    var = subprocess.getoutput("ls")
    lista = var[var.replace('\n', " ")]
    print(lista)
    #
    # if word in var:
    #     print(word)

search("questao")