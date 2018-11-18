# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DownloadViewer_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1093, 869)
        Dialog.setStyleSheet("alternate-background-color: rgb(213, 213, 213);")
        self.Download_tbl = QtWidgets.QTableWidget(Dialog)
        self.Download_tbl.setGeometry(QtCore.QRect(30, 30, 1031, 331))
        self.Download_tbl.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Download_tbl.setObjectName("Download_tbl")
        self.Download_tbl.setColumnCount(0)
        self.Download_tbl.setRowCount(0)
        self.SearchRecord_btn = QtWidgets.QPushButton(Dialog)
        self.SearchRecord_btn.setGeometry(QtCore.QRect(50, 760, 121, 61))
        self.SearchRecord_btn.setObjectName("SearchRecord_btn")
        self.IMDbID_txtbx = QtWidgets.QTextEdit(Dialog)
        self.IMDbID_txtbx.setGeometry(QtCore.QRect(140, 600, 231, 31))
        self.IMDbID_txtbx.setObjectName("IMDbID_txtbx")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 610, 47, 13))
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 390, 751, 451))
        self.frame.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.label_4.raise_()
        self.Delete_btn = QtWidgets.QPushButton(Dialog)
        self.Delete_btn.setGeometry(QtCore.QRect(240, 760, 121, 61))
        self.Delete_btn.setObjectName("Delete_btn")
        self.AddWishList_btn = QtWidgets.QPushButton(Dialog)
        self.AddWishList_btn.setGeometry(QtCore.QRect(430, 760, 121, 61))
        self.AddWishList_btn.setObjectName("AddWishList_btn")
        self.RecordID_txtbx = QtWidgets.QTextEdit(Dialog)
        self.RecordID_txtbx.setGeometry(QtCore.QRect(140, 560, 231, 31))
        self.RecordID_txtbx.setObjectName("RecordID_txtbx")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 570, 47, 13))
        self.label_5.setObjectName("label_5")
        self.AllRecords_btn = QtWidgets.QPushButton(Dialog)
        self.AllRecords_btn.setGeometry(QtCore.QRect(610, 760, 121, 61))
        self.AllRecords_btn.setObjectName("AllRecords_btn")
        self.frame.raise_()
        self.Download_tbl.raise_()
        self.SearchRecord_btn.raise_()
        self.IMDbID_txtbx.raise_()
        self.label_2.raise_()
        self.Delete_btn.raise_()
        self.AddWishList_btn.raise_()
        self.RecordID_txtbx.raise_()
        self.label_5.raise_()
        self.AllRecords_btn.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Download_tbl.setSortingEnabled(True)
        self.SearchRecord_btn.setText(_translate("Dialog", "Search Records"))
        self.label_2.setText(_translate("Dialog", "IMDb ID:"))
        self.label_4.setText(_translate("Dialog", "Search Records:"))
        self.label_6.setText(_translate("Dialog", "Record ID or IMDb ID are Required"))
        self.Delete_btn.setText(_translate("Dialog", "Delete Record"))
        self.AddWishList_btn.setText(_translate("Dialog", "Add to Wish List"))
        self.label_5.setText(_translate("Dialog", "Record ID:"))
        self.AllRecords_btn.setText(_translate("Dialog", "All Records"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

