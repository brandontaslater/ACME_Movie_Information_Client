# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchTheMoviedb_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 612)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 81, 31))
        self.label_3.setObjectName("label_3")
        self.MovieTitle_txtbx = QtWidgets.QTextEdit(Dialog)
        self.MovieTitle_txtbx.setGeometry(QtCore.QRect(100, 160, 121, 31))
        self.MovieTitle_txtbx.setObjectName("MovieTitle_txtbx")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 81, 31))
        self.label_5.setObjectName("label_5")
        self.Plot_txtbx = QtWidgets.QTextEdit(Dialog)
        self.Plot_txtbx.setGeometry(QtCore.QRect(140, 280, 121, 31))
        self.Plot_txtbx.setReadOnly(True)
        self.Plot_txtbx.setObjectName("Plot_txtbx")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 330, 101, 31))
        self.label_6.setObjectName("label_6")
        self.ReturnType_txtbx = QtWidgets.QTextEdit(Dialog)
        self.ReturnType_txtbx.setGeometry(QtCore.QRect(140, 330, 121, 31))
        self.ReturnType_txtbx.setReadOnly(True)
        self.ReturnType_txtbx.setObjectName("ReturnType_txtbx")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 120, 561, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 240, 561, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(30, 10, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.Search_btn = QtWidgets.QPushButton(Dialog)
        self.Search_btn.setGeometry(QtCore.QRect(30, 500, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Search_btn.setFont(font)
        self.Search_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Search_btn.setObjectName("Search_btn")
        self.APIKey_txtbx = QtWidgets.QTextEdit(Dialog)
        self.APIKey_txtbx.setGeometry(QtCore.QRect(140, 380, 211, 31))
        self.APIKey_txtbx.setReadOnly(True)
        self.APIKey_txtbx.setObjectName("APIKey_txtbx")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 380, 101, 31))
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(30, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Movie Title:"))
        self.label_5.setText(_translate("Dialog", "short or full Plot:"))
        self.Plot_txtbx.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">full</p></body></html>"))
        self.label_6.setText(_translate("Dialog", "Data Return Type:"))
        self.ReturnType_txtbx.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Json</p></body></html>"))
        self.label_8.setText(_translate("Dialog", "Movie ID or Movie Title are Required:"))
        self.label_9.setText(_translate("Dialog", "The Following are not Required:"))
        self.label_10.setText(_translate("Dialog", "Movie/Tv Show Search Criteria"))
        self.Search_btn.setText(_translate("Dialog", "Search"))
        self.APIKey_txtbx.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">74e005648630a661dc96a1087b37e66b</p></body></html>"))
        self.label_7.setText(_translate("Dialog", "API Key:"))
        self.label_11.setText(_translate("Dialog", "The Movie Database:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

