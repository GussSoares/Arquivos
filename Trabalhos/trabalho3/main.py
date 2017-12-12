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
    lista = deque()
    lista_contadores = []
    lista_contadores_separados = []

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
                lista_contadores_separados.append(count_word_1)
                lista_contadores_separados.append(count_word_2)
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
                lista_contadores_separados.append(count_word_1)
                lista_contadores_separados.append(count_word_2)

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
                lista_contadores_separados.append(count_word_1)
                lista_contadores_separados.append(count_word_2)

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
                lista_contadores_separados.append(count_word_1)
                lista_contadores_separados.append(count_word_2)

    print("lista contadores:", lista_contadores)
    print(len(lista))


    def ordenar(lista, lista_contadores):
        lista_ordenada_arquivos = deque()
        lista_ordenada_count = deque()

        principal = lista[0]
        while max(lista_contadores) != -1:
            for i in range(len(lista_contadores)):
                if lista_contadores[i] == max(lista_contadores):
                    lista_ordenada_arquivos.append(lista[i])
                    lista_ordenada_count.appendleft(lista_contadores[i])
                    print(lista[i])
                    # lista_contadores.remove(lista_contadores[i])
                    lista_contadores[i]=-1
                    # lista.remove(lista[i])
        if len(string) > 1:
            if string[0] in principal and string[1] in principal:
                if principal in lista_ordenada_arquivos:
                    lista_ordenada_arquivos.remove(principal)
                lista_ordenada_arquivos.appendleft(principal)
        else:

            pass

        return (lista_ordenada_arquivos, lista_ordenada_count)

    result = ordenar(lista, lista_contadores)
    print("RETORNO 1",result[0])
    print("RETORNO 2", result[1])
    print("Lista Ordenada: ",result)

    return result

def insere_tabel(path):
    list = search_in_files(ui.lineEdit.text(), path)[0]
    count = search_in_files(ui.lineEdit.text(),path)[1]
    print("COUNT:",count)
    print("LEN LIST: ", len(list))
    interface2.ui.tableWidget_2.setRowCount(len(list))
    interface2.ui.tableWidget_3.setRowCount(len(count))
    # interface2.ui.tableWidget_2.setColumnCount(2)
    for i in range(len(list)):
        # for j in range(2):
        interface2.ui.tableWidget_2.setItem(i, 0, QtWidgets.QTableWidgetItem(list[i]))
            # interface2.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(count[i]))
    for j in range(len(count)):
        for k in range(2):
            interface2.ui.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(count[i]))


# noinspection PyTypeChecker
def main_(path):

    interface2.MainWindow = QtWidgets.QMainWindow()
    interface2.ui = interface2.Ui_MainWindow()
    interface2.ui.setupUi(interface2.MainWindow)
    interface2.MainWindow.show()

    # cria um vetor de palavras
    word = ui.lineEdit.text().split(" ")

    print("SEARCH: ",search_in_files(ui.lineEdit.text(), path))

    insere_tabel(path)
            # interface2.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(m[i][j]))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(partial(main_, "/home/gustavo/"))

    sys.exit(app.exec_())