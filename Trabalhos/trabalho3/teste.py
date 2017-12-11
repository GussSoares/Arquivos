# -*- coding: utf-8 -*-

import os, time
from collections import deque


def search_directory(text_box, initial_path):
    string = text_box.split(" ")

    list = []

    for path, dirs, files in os.walk(initial_path):
        for f in files:
            if len(string) > 1:

                if string[0].lower() in f.lower() and string[1].lower() in f.lower() and not (path + f in list) and ".pdf" in f:
                    list.append(str(path + f))

                if string[0].lower() in f.lower() and not (path + f in list) and ".pdf" in f:
                    list.append(str(path + f))

                if string[1].lower() in f.lower() and not (path + f in list) and ".pdf" in f:
                    list.append(str(path + f))

            else:

                if (string[0].lower() in f.lower()) and not (path + f in list) and ".pdf" in f:
                    list.append(str(path + f))

    print(len(list))
    return list


def search_in_files(text_box, initial_path):
    string = text_box.split(" ")

    list = []
    count_word_1 = 0
    count_word_2 = 0
    lista_contadores = deque()
    for path, dirs, files in os.walk(initial_path):
        for f in files:
            if len(string) > 1:
                # print(str(f))
                # faz a verificacao quando recebe mais de uma palavra na caixa de texto
                if string[0].lower() in f.lower() and string[1].lower() in f.lower() and not (
                        f in list) and ".pdf" in f:
                    list.append(str(f))
                    print("==================")
                    print("Arquivo Adicionado")
                    print("==================")

                    # novaString = f
                    # novaString = novaString.split(" ")
                    # if len(novaString) > 1:
                    #
                    #     count_word_1 = 0
                    #     count_word_2 = 0
                    #     print(novaString[1])
                    #     print(("pdftotext {}{}\ {} {}{}\ {}").format(path, novaString[0], novaString[1], path,
                    #                                                  novaString[0],
                    #                                                  novaString[1].replace(".pdf", ".txt")))
                    #     os.popen(("pdftotext {}{}\ {} {}{}\ {}").format(path, novaString[0], novaString[1], path,
                    #                                                     novaString[0],
                    #                                                     novaString[1].replace(".pdf", ".txt")))
                    #     time.sleep(1)
                    #     with open(str(path + str(f).replace(".pdf", ".txt"))) as file_txt:
                    #         print("entrou with")
                    #         for line in file_txt:
                    #             line = line.split(" ")
                    #             print(line)
                    #             for word in line:
                    #                 if string[0].lower() in str(word).lower():
                    #                     count_word_1 += 1
                    #     print("count 1:", count_word_1)
                    #     print("count 2:", count_word_2)
                    # else:
                    #
                    #     count_word_1 = 0
                    #     count_word_2 = 0
                    #     print("entrou else")
                    #     print(("pdftotext {}{} {}{}").format(path, f, path, str(f).replace(".pdf", ".txt")))
                    #     os.popen(("pdftotext {}{} {}{}").format(path, f, path, str(f).replace(".pdf", ".txt")))
                    #     time.sleep(1)
                    #     with open(str(path + str(f).replace(".pdf", ".txt"))) as file_txt:
                    #         print("entrou with")
                    #         for line in file_txt:
                    #             line = line.split(" ")
                    #             print(line)
                    #             for word in line:
                    #                 if string[0].lower() in str(word).lower():
                    #                     count_word_1 += 1
                    #     print("count 1:", count_word_1)
                    #     print("count 2:", count_word_2)

                if string[0].lower() in f.lower() and not (f in list) and ".pdf" in f:
                    list.append(str(f))
                    print("==================")
                    print("Arquivo Adicionado")
                    print("==================")
                    novaString = f
                    novaString = novaString.split(" ")
                    if len(novaString) > 1:

                        count_word_1 = 0
                        count_word_2 = 0
                        # print(novaString[1])
                        print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ "))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1
                                    if string[1].lower() in str(word).lower():
                                        count_word_2 += 1
                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                        lista_contadores.append(count_word_1)
                        lista_contadores.append(count_word_2)
                    else:

                        count_word_1 = 0
                        count_word_2 = 0
                        print("entrou else")
                        print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ "))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1
                                    if string[1].lower() in str(word).lower():
                                        count_word_2 += 1
                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                        lista_contadores.append(count_word_1)
                        lista_contadores.append(count_word_2)

                if string[1].lower() in f.lower() and not (f in list) and ".pdf" in f:
                    list.append(str(f))
                    print("==================")
                    print("Arquivo Adicionado")
                    print("==================")
                    novaString = f
                    novaString = novaString.split(" ")
                    if len(novaString) > 1:

                        count_word_1 = 0
                        count_word_2 = 0
                        # print(novaString[1])
                        print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ "))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1
                                    if string[1].lower() in str(word).lower():
                                        count_word_2 += 1
                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                        lista_contadores.append(count_word_1)
                        lista_contadores.append(count_word_2)
                    else:

                        count_word_1 = 0
                        count_word_2 = 0
                        print("entrou else")
                        print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ "))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1
                                    if string[1].lower() in str(word).lower():
                                        count_word_2 += 1
                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                        lista_contadores.append(count_word_1)
                        lista_contadores.append(count_word_2)

            else:

                if (string[0].lower() in f.lower()) and not (f in list) and ".pdf" in f:
                    list.append(str(f))
                    print("==================")
                    print("Arquivo Adicionado")
                    print("==================")

                    novaString = f
                    novaString = novaString.split(" ")
                    if len(novaString) > 1:

                        count_word_1 = 0
                        count_word_2 = 0
                        # print(novaString[1])
                        print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ "))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1

                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                        lista_contadores.append(count_word_1)
                        lista_contadores.append(count_word_2)
                    else:

                        count_word_1 = 0
                        count_word_2 = 0
                        print("entrou else")
                        print(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path.replace(" ", "\ "), f.replace(" ", "\ "),
                                                               path.replace(" ", "\ "),
                                                               f.replace(" ", "\ ").replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path.replace(" ","\ ") +"/"+ str(f).replace(".pdf", ".txt").replace(" ", "\ "))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1
                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                        lista_contadores.append(count_word_1)
                        lista_contadores.append(count_word_2)

    print(len(list))
    m=[]
    print("contadores:",lista_contadores)
    for y in range(len(list)):
        linha = []
        for x in range(2):
            linha.append(lista_contadores.popleft())
        m.append(linha)
    print(m)
    return list
    # os.popen(("pdftotext {}.pdf {}.txt ").format(file, file))


# for f in search_directory("deepin", "/home/gustavo/Desktop/"):
#     print(f)
# for f in search_in_files("interface", "/home/gustavo/Desktop/"):
#     print(f)

print(search_in_files("lista", "/home/gustavo/Área\ de\ Trabalho"))