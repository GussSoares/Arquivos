# coding=utf-8
from threading import Thread
import subprocess, os, time
import pprint as pp
import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

import face1

path = "/home/gustavo/Área\ de\ Trabalho/GitHub/Arquivos/Trabalhos/trabalho3/item_c/"

def ler_pdf(path):
    imgFontes = PDFResourceManager()
    binario = io.StringIO()
    codec = "utf-8"

    device = TextConverter(imgFontes, binario, codec = codec)

    fp = open(path, "rb")

    interpreter = PDFPageInterpreter(imgFontes, device)

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)

    aux = [word.lower() for word in binario.getvalue().split()]
    aux2 = [aux.count(word) for word in aux]
    aux3 = []

    for i in range(len(aux)):
        aux3.append((aux[i]))

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
        # print(caminho)

        # print(file)
        # os.popen(("pdftotext {} {}").format(a, a.replace(".pdf", ".txt")))
        # time.sleep(.5)
        #
        # with open(str(caminho.replace(".pdf", ".txt"))) as file_text:
        #
        #     palavras = []
        #     # print("entrou with")
        #     for line in file_text:
        #         line = line.split(" ")
        #         for word in line:
        #             palavras.append(word.strip("\n").lower())
        # palavras = sorted(set(palavras))
        # print("ordenado: ", palavras)
        # ler_pdf(caminho)
        lista.append((caminho, ler_pdf(caminho)))

    print("LISTA: ", lista, "\n\n\n")
    return lista

def busca_na_lista(word, list):

    resultado = []
    for i in range(len(list)):

        if word.lower() in list[i][1] or word.lower() in list[i][0].split("/")[-1].lower():
            # print(list[i][0])

            resultado.append(word.lower())
    print("BUSCA NA LISTA: ", resultado, "\n\n")
    return resultado

lista = []
for i in range(len(busca(path))):
    lista.append(busca(path)[i][1])
print("NOVA: ",lista)
# except:
#     print("\"{}\" Not Found".format(word))

def main_():
    pass

if __name__ == '__main__':
    import sys




    app = face1.QtWidgets.QApplication(sys.argv)
    MainWindow = face1.QtWidgets.QMainWindow()
    ui = face1.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # for i in range(len(busca_na_lista(ui.lineEdit.text(), lista))):
    #     print(busca_na_lista(ui.lineEdit.text(), lista)[i])

    completer = face1.QtWidgets.QCompleter()
    ui.lineEdit.setCompleter(completer)

    model = face1.QtCore.QStringListModel()
    completer.setModel(model)
    ui.get_data(model)

    MainWindow.show()
    sys.exit(app.exec_())
