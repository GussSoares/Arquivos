import sys, os
from functools import partial

from interface1 import *
import interface2



def search(text_box, initial_path):
    list=[]
    for path, dirs, files in os.walk(initial_path):
        print(files)
        for f in files:
            if text_box.lower() in f.lower():
                list.append(str(path+f))
    return list

def main_(path):

    interface2.MainWindow = QtWidgets.QMainWindow()
    interface2.ui = interface2.Ui_MainWindow()
    interface2.ui.setupUi(interface2.MainWindow)
    interface2.MainWindow.show()

    list = search(ui.lineEdit.text(), path)

    interface2.ui.tableWidget.setRowCount(len(list)-1)
    for i in range(len(list)-1):

        interface2.ui.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(list[i+1]))


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.pushButton.clicked.connect(partial(main_, "/home/gustavo/"))

    sys.exit(app.exec_())