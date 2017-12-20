# coding=utf-8
from threading import Thread
import subprocess, os, time, io
from functools import partial
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

import face1, face2

path = "/home/gustavo/GitHub/Arquivos/Trabalhos/trabalho3/item_c/"

def ler_pdf(path):
    imgFontes = PDFResourceManager()
    binario = io.StringIO()
    codec = "utf-8"

    list_word = []
    current_word = []
    index_word = []

    device = TextConverter(imgFontes, binario, codec = codec)

    fp = open(path, "rb")

    interpreter = PDFPageInterpreter(imgFontes, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)

    aux = binario.getvalue()
    for pos, doc in enumerate(aux):
        if doc.isalnum():
            current_word.append(doc)
            index_word = pos
        elif current_word:
            word = u''.join(current_word)
            list_word.append(word)
            current_word = []

    if current_word:
        word = u' '.join(current_word)
        list_word.append(word.lower())

    aux2 = [list_word.count(word) for word in list_word]
    aux3 = []

    for i in range(len(list_word)):
        aux3.append(str(list_word[i]).lower())

    print (aux3, "\n\n")
    fp.close()
    device.close()
    binario.close()
    return aux3



def busca(path):

    command = ("find {} -maxdepth 8 -type f -iname \"*.pdf\"").format(path)  # the shell command

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.decode("UTF-8").replace("\n", "\n").split("\n")
    lista = []
    while "" in result:
        result.remove("")
    for caminho in result:

        a = caminho.replace(" ", "\ ")      # formata o caminho para espacamentos
        file = caminho.split("/")[-1]       # nome do arquivo pdf

        lista.append((caminho, ler_pdf(caminho)))

    print("LISTA: ", lista, "\n\n\n")
    return lista                            # lista com o nome do diretorio e as palavras do arquivo

def busca_na_lista(word, list):

    resultado = []
    digitada = str(word).split(" ")
    lista = list[0]
    for i in range(len(lista)):
        if digitada[0].lower() in lista[i][0].split("/")[-1] or digitada[1].lower() in lista[i][0].split("/")[-1]:
            resultado.append((lista[i][0], lista[i][1], list[1][i]))
        # if digitada[0].lower() in list[0][0][i][0].split("/")[-1] or digitada[1].lower() in list[0][0][i][0].split("/")[-1]:
        #     resultado.append((list[0][0][i][0], list[0][0][i][1], list[1][i]))
        #
        elif digitada[0].lower() in lista[i][1] or digitada[1].lower() in lista[i][1]:
            resultado.append((lista[i][0], lista[i][1], list[1][i]))

    for i in range(len(resultado)):
        if resultado[i][1] != digitada[0] and resultado[i][1] != digitada[1]:
            resultado[i] = -1
    while -1 in resultado:
        resultado.remove(-1)

    resultado.sort(key=lambda x: x[2])
    resultado.reverse()
    print("BUSCA NA LISTA: ", resultado, "\n\n")
    return resultado

lista = []
for i in range(len(busca(path))):
    lista.append(busca(path)[i][1])
print("NOVA: ",lista)                       # lista com as listas das palavras de cada pdf


def counter():
    lista_nova = []
    lista_count = []
    lista_word_direct = []
    result = busca(path)
    for i in range(len(result)):
        for j in range(len(result[i][1])):
            lista_nova.append((result[i][0], result[i][1][j], result[i][1].count(result[i][1][j])))

            lista_count.append(result[i][1].count(result[i][1][j]))  # contador de cada palavra

            lista_word_direct.append(((result[i][0], result[i][1][j])))  # diretorio do arquivo e palavra
    print("LISTA REALMENTE:",(lista_word_direct, lista_count))
    return (lista_word_direct, lista_count)

def ordenacao(lista):

    # ordenacao
    count_ord = []
    word_direct_ord = []
    lista_count = []

    for i in range(len(lista)):
        lista_count.append(int(lista[i][2]))
    print("count:", lista_count)
    while max(lista_count) != -1:
        for i in range(len(lista)):
            if int(lista[i][2]) == max(lista_count):
                count_ord.append(str(lista_count[i]))
                word_direct_ord.append(lista[i])

                lista_count[i] = -1
                lista[i] = -1

    while -1 in count_ord:
        count_ord.remove(-1)
    while -1 in word_direct_ord:
        word_direct_ord.remove(-1)

    print("tupla word_dict count",(word_direct_ord, count_ord))
    return (word_direct_ord, count_ord)

def insere_tabela():
    list_word = counter()[0]
    list_count = counter()[1]

    lista_pra_busca_lista = counter()

    lista_completa = busca_na_lista(ui.lineEdit.text(), lista_pra_busca_lista)


    print("LISTA_ORDENADA_FINAL:",lista_completa)

    face2.ui.tableWidget_2.setRowCount(len(lista_completa))
    face2.ui.tableWidget_3.setRowCount(len(lista_completa))

    for i in range(len(lista_completa)):
    #     # for j in range(2):
        face2.ui.tableWidget_2.setItem(i, 0, face2.QtWidgets.QTableWidgetItem(str(lista_completa[i][0])))
    #         # interface2.ui.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(count[i]))
    # for j in range(len(list_count)):
    #     for k in range(2):
    #         face2.ui.tableWidget_3.setItem(j, k, face2.QtWidgets.QTableWidgetItem(str(list_count[j][k])))
    #         print("COUNT J K: ",list_count[j][k])
    for i in range(len(lista_completa)):
        for k in range(2):
            face2.ui.tableWidget_3.setItem(i, k, face2.QtWidgets.QTableWidgetItem(str(lista_completa[i][2])))

def main_(path):
    # time.sleep(0.5)
    face2.MainWindow = face2.QtWidgets.QMainWindow()
    face2.ui = face2.Ui_MainWindow()
    face2.ui.setupUi(face2.MainWindow)
    face2.MainWindow.show()

    insere_tabela()

    vindo_da_counter = counter()
    busca_na_lista(ui.lineEdit.text(), vindo_da_counter)
if __name__ == '__main__':

    import sys

    app = face1.QtWidgets.QApplication(sys.argv)
    MainWindow = face1.QtWidgets.QMainWindow()
    ui = face1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    completer = face1.QtWidgets.QCompleter()
    ui.lineEdit.setCompleter(completer)

    model = face1.QtCore.QStringListModel()
    completer.setModel(model)
    ui.get_data(model)

    ui.pushButton.clicked.connect(partial(main_, path))

    MainWindow.show()
    sys.exit(app.exec_())
