import sys, os, time, subprocess
from functools import partial
from collections import deque

from interface1 import *
import interface2


# pesquisa o caminho completo desde o path passado por parametro ate achar os arquivos com aquele nome
def search_directory(text_box, initial_path):

    # text_box = text_box.split(" ")
    list=[]
    for path, dirs, files in os.walk(initial_path):
        for f in files:
            if text_box.lower() in f.lower():
                list.append(str(path+f))
    return list

# pesquisa os arquivos por nome
def search_files(text_box, initial_path):
    list=[]
    for path, dirs, files in os.walk(initial_path):
        for f in files:
            if text_box.lower() in f.lower():
                list.append(str(f))
    return list


def search_in_files(text_box, path):
    string = text_box.split(" ")
    lista = []
    lista_contadores = deque()

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

                print("\n===========================")
                print("DUAS PALAVRAs DIGITADAS")
                print("===========================\n")

                count_word_1 = 0
                count_word_2 = 0
                lista.append(str(file))
                print("==================")
                print("Arquivo Adicionado")
                print("==================")

            if string[0].lower() in file.lower() and not file in lista:

                print("\n===========================")
                print("ACHOU PALAVRA UM")
                print("===========================\n")

                count_word_1 = 0
                count_word_2 = 0
                print(f.split("/")[-1]+"\n\n")

                lista.append(str(file))

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
                lista_contadores.append(count_word_1)
                lista_contadores.append(count_word_2)

            if string[1].lower() in file.lower() and not file in lista:

                print("\n===========================")
                print("ACHOU PALAVRA DOIS")
                print("===========================\n")

                count_word_1 = 0
                count_word_2 = 0
                print(f.split("/")[-1] + "\n\n")

                lista.append(str(file))

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
                lista_contadores.append(count_word_1)
                lista_contadores.append(count_word_2)

        else:

            if string[0].lower() in file.lower() and not file in lista:
                count_word_1 = 0
                count_word_2 = 0
                print("\n===========================")
                print("APENAS UMA PALAVRA DIGITADA")
                print("===========================\n")
                print(f.split("/")[-1] + "\n\n")

                lista.append(str(file))

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
                lista_contadores.append(count_word_1)
                lista_contadores.append(count_word_2)

    print(len(lista))
    m = []
    print("contadores:", lista_contadores)
    for y in range(len(lista)):
        linha = []
        for x in range(2):
            linha.append(lista_contadores.popleft())
        m.append(linha)
    print(m)

    return lista


# noinspection PyTypeChecker
def main_(path):

    interface2.MainWindow = QtWidgets.QMainWindow()
    interface2.ui = interface2.Ui_MainWindow()
    interface2.ui.setupUi(interface2.MainWindow)
    interface2.MainWindow.show()

    # cria um vetor de palavras
    word = ui.lineEdit.text().split(" ")

    list = search_in_files(ui.lineEdit.text(), path)

    interface2.ui.tableWidget.setRowCount(len(list))
    for i in range(len(list)):

        interface2.ui.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(list[i]))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(partial(main_, "/home/gustavo/"))

    sys.exit(app.exec_())