import os, subprocess


def search(word):

    var = str(subprocess.getoutput("ls")).split('\n')

    print(var)

    print(word in var)


search("teste")
