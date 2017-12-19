# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face1.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import teste1

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
path = "/home/gustavo/Área\ de\ Trabalho/GitHub/Arquivos/Trabalhos/trabalho3/item_c/"

class Ui_MainWindow(object):

    def get_data(self, model):

        # print(teste1.lista)
        list = []
        for item in teste1.lista:
            for i,word in enumerate(item):
                if i == len(item)-1:
                    print(word)
                    pass
                else:
                    print(word,item[i+1])
                    list.append(word+" "+item[i+1])
        model.setStringList(list)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(306, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(32, 40, 251, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 90, 80, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 306, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    completer = QtWidgets.QCompleter()
    ui.lineEdit.setCompleter(completer)

    model = QtCore.QStringListModel()
    completer.setModel(model)
    ui.get_data(model)

    MainWindow.show()
    sys.exit(app.exec_())