import main, os, subprocess, time
from collections import deque
import interface2

# print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "), path.replace(" ", "\ "), f.replace(" ", "\ ").replace(".pdf", ".txt")))
#
# print(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ ")))
#
# print("\n\n")
#
# print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "), path.replace(" ", "\ "), f.replace(" ", "\ ").replace(".pdf", ".txt")))
#
# print(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ ")))

# a = subprocess.Popen(("find /home/gustavo/ -type f -iname *.pdf"))
# # out = a.communicate()
# subprocess.check_output([])
# print(out)

import subprocess

path="/home/gustavo/"

def busca_arquivo_com_diretorio(text_box, path):                                  # retorna lista de diretorio de arquivos
    string = text_box.split(" ")
    lista = deque()
    lista_contadores = []

    count_word_1 = 0
    count_word_2 = 0

    command = ("find {} -maxdepth 4 -type f -iname \"*.pdf\"").format(path)  # the shell command

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.decode("UTF-8").replace("\n", "\n").split("\n")
    for f in result:
        # print (f.split("/")[-1])
        # lista.append(f.split("/")[-1])
        # lista.append(f)
        file = f.split("/")[-1]
        # f = f.replace(" ", "\ ")
        a = f.replace(" ", "\ ")
        if len(string) > 1:

            if string[0].lower() in file.lower() and string[1].lower() in file.lower() and not f in lista:

                print("\n===========================")
                print("DUAS PALAVRAs DIGITADAS")
                print("===========================\n")

                count_word_1 = 0
                count_word_2 = 0
                count_word_1 += 1
                count_word_2 += 1

                lista.appendleft(str(f))
                print(f.split("/")[-1] + "\n\n")
                lista_contadores.append(count_word_1+count_word_2)
                print("relevancia =", count_word_1 + count_word_2)
                # lista_contadores.append(count_word_2)

                # print("==================")
                # print("Arquivo Adicionado")
                # print("==================")

            if string[0].lower() in file.lower() and not f in lista:

                print("\n===========================")
                print("ACHOU PALAVRA UM")
                print("===========================\n")

                count_word_1 = 0
                count_word_2 = 0
                print(f.split("/")[-1]+"\n\n")

                lista.append(str(f))

                print(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))

                os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
                time.sleep(.5)

                print(a.replace(".pdf", ".txt"))

                with open(str(a.replace(".pdf", ".txt").replace("\\", ""))) as file_text:
                    print("entrou with")
                    for line in file_text:
                        line = line.split(" ")
                        for word in line:
                            if string[0].lower() in str(word).lower():
                                count_word_1 += 1
                            if string[1].lower() in str(word).lower():
                                count_word_2 += 1
                print("count 1:", count_word_1)
                print("count 2:", count_word_2)
                lista_contadores.append(count_word_1+count_word_2)
                # lista_contadores.append(count_word_2)
                print("relevancia =", count_word_1 + count_word_2)

            if string[1].lower() in file.lower() and not f in lista:

                print("\n===========================")
                print("ACHOU PALAVRA DOIS")
                print("===========================\n")

                count_word_1 = 0
                count_word_2 = 0
                print(f.split("/")[-1] + "\n\n")

                lista.append(str(f))

                print(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))

                os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
                time.sleep(.5)

                print(a.replace(".pdf", ".txt"))

                with open(str(a.replace(".pdf", ".txt").replace("\\", ""))) as file_text:
                    print("entrou with")
                    for line in file_text:
                        line = line.split(" ")
                        for word in line:
                            if string[0].lower() in str(word).lower():
                                count_word_1 += 1
                            if string[1].lower() in str(word).lower():
                                count_word_2 += 1
                print("count 1:", count_word_1)
                print("count 2:", count_word_2)
                lista_contadores.append(count_word_1+count_word_2)
                # lista_contadores.append(count_word_2)
                print("relevancia =", count_word_1 + count_word_2)

        else:

            if string[0].lower() in file.lower() and not f in lista:
                count_word_1 = 0
                count_word_2 = 0
                print("\n===========================")
                print("APENAS UMA PALAVRA DIGITADA")
                print("===========================\n")
                print(f.split("/")[-1] + "\n\n")

                lista.append(str(f))

                print(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))

                os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
                time.sleep(.5)

                print(a.replace(".pdf", ".txt"))

                with open(str(a.replace(".pdf", ".txt").replace("\\", ""))) as file_text:
                    print("entrou with")
                    for line in file_text:
                        line = line.split(" ")
                        for word in line:
                            if string[0].lower() in str(word).lower():
                                count_word_1 += 1
                print("count 1:", count_word_1)
                print("count 2:", count_word_2)
                lista_contadores.append(count_word_1+count_word_2)
                # lista_contadores.append(count_word_2)
                print("relevancia =", count_word_1+count_word_2)

    print("lista contadores:", lista_contadores)
    print(len(lista))


    def ordenar(lista, lista_contadores):
        lista_ordenada_arquivos = deque()
        principal = lista[0]
        while len(lista_contadores) != 0:
            for i in range(len(lista_contadores)):
                if lista_contadores[i] == max(lista_contadores):
                    lista_ordenada_arquivos.append(lista[i])
                    print(lista[i])
                    lista_contadores.remove(lista_contadores[i])
        lista_ordenada_arquivos.remove(principal)
        lista_ordenada_arquivos.appendleft(principal)
        return lista_ordenada_arquivos

    print(ordenar(lista, lista_contadores))


    return ordenar(lista, lista_contadores)

print("\n\nLista retornada:", busca_arquivo_com_diretorio("deepin interface",path))
#
# def busca_arquivo_sem_diretorio(lista):                                 # retorna lista de arquivos somente
#
#     # lista = busca_arquivo_com_diretorio("/home/gustavo/")
#     lista_arquivos=[]
#     for a in lista:
#         # print(a.split("/")[-1])
#         lista_arquivos.append(a.split("/")[-1])
#     return lista_arquivos
#
# lista = busca_arquivo_sem_diretorio(busca_arquivo_com_diretorio(path))
#
# i=0
# for a in lista:
#     i+=1
#     if "felipe" in str(a).lower():
#         print(a)
#         os.popen("pdftotext")
#         with open(busca_arquivo_com_diretorio(path)[i]) as file:
#             print("entrou")
