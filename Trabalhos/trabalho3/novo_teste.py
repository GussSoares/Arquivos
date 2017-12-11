import main, os, subprocess, time

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

import subprocess

path="/home/gustavo/"

def busca_arquivo_com_diretorio(text_box, path):                                  # retorna lista de diretorio de arquivos
    string = text_box.split(" ")
    lista=[]

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


            if string[0].lower() in file.lower() and string[1].lower() and not file in lista:
                lista.append(str(file))
                print("==================")
                print("Arquivo Adicionado")
                print("==================")

            if string[0].lower() in file.lower() and not file in lista:
                print(f)

                lista.append(str(file))

                print(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))

                os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
                time.sleep(.5)

                print(a.replace(".pdf", ".txt"))

                with open(str(a.replace(".pdf", ".txt"))) as file_text:
                    print("entrou with")
                    for line in file_text:
                        line = line.split(" ")
                        for word in line:
                            if string[0].lower() in str(word).lower():
                                count_word_1 += 1
                            if string[1].lower() in str(word).lower():
                                count_word_2 += 1

            if string[1].lower() in file.lower() and not file in lista:
                print(f)

                lista.append(str(file))

                print(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))

                os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
                time.sleep(.5)

                print(a.replace(".pdf", ".txt"))

                with open(str(a.replace(".pdf", ".txt"))) as file_text:
                    print("entrou with")
                    for line in file_text:
                        line = line.split(" ")
                        for word in line:
                            if string[0].lower() in str(word).lower():
                                count_word_1 += 1
                            if string[1].lower() in str(word).lower():
                                count_word_2 += 1

        else:

            if string[0].lower() in file.lower() and not file in lista:
                print("\n===========================")
                print("APENAS UMA PALAVRA DIGITADA")
                print("===========================\n")
                print(f)

                lista.append(str(file))

                print(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))

                os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
                time.sleep(.5)

                print(a.replace(".pdf", ".txt"))

                with open(str(a.replace(".pdf", ".txt").replace("\\",""))) as file_text:
                    print("entrou with")
                    for line in file_text:
                        line = line.split(" ")
                        for word in line:
                            if string[0].lower() in str(word).lower():
                                count_word_1 += 1


    return lista

print(busca_arquivo_com_diretorio("felipe",path))
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
