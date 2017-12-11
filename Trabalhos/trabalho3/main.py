import sys, os, time
from functools import partial

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


def search_in_files(text_box, initial_path):
    string = text_box.split(" ")

    list = []
    count_word_1 = 0
    count_word_2 = 0
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
                        print(("pdftotext {}/{}\ {} {}/{}\ {}").format(path, novaString[0], novaString[1], path,
                                                                     novaString[0],
                                                                     novaString[1].replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{}\ {} {}/{}\ {}").format(path, novaString[0], novaString[1], path,
                                                                        novaString[0],
                                                                        novaString[1].replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path +"/"+ str(f).replace(".pdf", ".txt"))) as file_txt:
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
                    else:

                        count_word_1 = 0
                        count_word_2 = 0
                        print("entrou else")
                        print(("pdftotext {}/{} {}/{}").format(path, f, path, str(f).replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path, f, path, str(f).replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path +"/"+ str(f).replace(".pdf", ".txt"))) as file_txt:
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
                        print(("pdftotext {}/{}\ {} {}/{}\ {}").format(path, novaString[0], novaString[1], path,
                                                                     novaString[0],
                                                                     novaString[1].replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{}\ {} {}/{}\ {}").format(path, novaString[0], novaString[1], path,
                                                                        novaString[0],
                                                                        novaString[1].replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path +"/"+ str(f).replace(".pdf", ".txt"))) as file_txt:
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
                    else:

                        count_word_1 = 0
                        count_word_2 = 0
                        print("entrou else")
                        print(("pdftotext {}/{} {}/{}").format(path, f, path, str(f).replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path, f, path, str(f).replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path +"/"+ str(f).replace(".pdf", ".txt"))) as file_txt:
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
                        print(("pdftotext {}/{}\ {} {}/{}\ {}").format(path, novaString[0], novaString[1], path, novaString[0], novaString[1].replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{}\ {} {}/{}\ {}").format(path, novaString[0], novaString[1], path, novaString[0], novaString[1].replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path +"/"+str(f).replace(".pdf", ".txt"))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1

                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)
                    else:

                        count_word_1 = 0
                        count_word_2 = 0
                        print("entrou else")
                        print(("pdftotext {}/{} {}/{}").format(path ,f, path, str(f).replace(".pdf", ".txt")))
                        os.popen(("pdftotext {}/{} {}/{}").format(path ,f, path, str(f).replace(".pdf", ".txt")))
                        time.sleep(1)
                        with open(str(path +"/"+str(f).replace(".pdf", ".txt"))) as file_txt:
                            print("entrou with")
                            for line in file_txt:
                                line = line.split(" ")
                                # print(line)
                                for word in line:
                                    if string[0].lower() in str(word).lower():
                                        count_word_1 += 1
                        print("count 1:", count_word_1)
                        print("count 2:", count_word_2)

    print(len(list))

    return list


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