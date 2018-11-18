# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchOMDB_Screen.ui'
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
        self.MovieID_txtbx = QtWidgets.QTextEdit(Dialog)
        self.MovieID_txtbx.setGeometry(QtCore.QRect(90, 150, 121, 31))
        self.MovieID_txtbx.setObjectName("MovieID_txtbx")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 150, 51, 31))
        self.label.setObjectName("label")
        self.Type_txtbx = QtWidgets.QTextEdit(Dialog)
        self.Type_txtbx.setGeometry(QtCore.QRect(140, 240, 121, 31))
        self.Type_txtbx.setObjectName("Type_txtbx")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 150, 81, 31))
        self.label_3.setObjectName("label_3")
        self.MovieTitle_txtbx = QtWidgets.QTextEdit(Dialog)
        self.MovieTitle_txtbx.setGeometry(QtCore.QRect(310, 150, 121, 31))
        self.MovieTitle_txtbx.setObjectName("MovieTitle_txtbx")
        self.Year_txtbx = QtWidgets.QTextEdit(Dialog)
        self.Year_txtbx.setGeometry(QtCore.QRect(140, 290, 121, 31))
        self.Year_txtbx.setObjectName("Year_txtbx")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 81, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 340, 81, 31))
        self.label_5.setObjectName("label_5")
        self.Plot_txtbx = QtWidgets.QTextEdit(Dialog)
        self.Plot_txtbx.setGeometry(QtCore.QRect(140, 340, 121, 31))
        self.Plot_txtbx.setObjectName("Plot_txtbx")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 390, 101, 31))
        self.label_6.setObjectName("label_6")
        self.ReturnType_txtbx = QtWidgets.QTextEdit(Dialog)
        self.ReturnType_txtbx.setGeometry(QtCore.QRect(140, 390, 121, 31))
        self.ReturnType_txtbx.setReadOnly(True)
        self.ReturnType_txtbx.setObjectName("ReturnType_txtbx")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 561, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(30, 200, 561, 31))
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
        self.APIKey_txtbx = QtWidgets.QTextEdit(Dialog)
        self.APIKey_txtbx.setGeometry(QtCore.QRect(140, 440, 121, 31))
        self.APIKey_txtbx.setReadOnly(True)
        self.APIKey_txtbx.setObjectName("APIKey_txtbx")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 440, 101, 31))
        self.label_7.setObjectName("label_7")
        self.Search_btn = QtWidgets.QPushButton(Dialog)
        self.Search_btn.setGeometry(QtCore.QRect(30, 500, 171, 51))
        self.Search_btn.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.Search_btn.setObjectName("Search_btn")
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
        self.label.setText(_translate("Dialog", "Movie ID:"))
        self.label_2.setText(_translate("Dialog", "Type:"))
        self.label_3.setText(_translate("Dialog", "Movie Title:"))
        self.label_4.setText(_translate("Dialog", "Year:"))
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
        self.APIKey_txtbx.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">7476698c</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "API Key:"))
        self.Search_btn.setText(_translate("Dialog", "Search"))
        self.label_11.setText(_translate("Dialog", "The Open Movie Database:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

