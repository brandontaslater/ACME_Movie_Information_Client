import os
import sys
from os.path import normpath

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from InitialiseDB import _Main
from GUI import Popup_Screen
from UI.WishList_Screen import Ui_Dialog


class WishList(QtWidgets.QDialog):
    def __init__(self, Table):
        print("WishList")
        super(WishList, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.Table = Table  # stores the table in use
        location = str(os.getcwd()) + "\ACME_Storage.db"
        self.path = normpath(location)
        self.DownloadedTableData = _Main.FetchAllData(self.path, Table)
        self.ColumnNames = []
        self.NoInTable = 0
        self.CurrentTableData = [[]]
        self.load_table(self.DownloadedTableData)
        self.ui.Search_btn.clicked.connect(self.Search_Clicked)
        self.ui.Delete_btn.clicked.connect(self.Delete_Click)
        self.ui.AllRecords_btn.clicked.connect(self.Refresh_Clicked)
        self.show()


    @pyqtSlot()
    def Refresh_Clicked(self):
        print("Refreshing Table")
        self.DownloadedTableData = _Main.FetchAllData(self.path, self.Table)
        self.load_table(self.DownloadedTableData)
        print("Finished Refreshing Table")

    @pyqtSlot()
    def Search_Clicked(self):
        print("Searhcing Table")
        if self.NoInTable != 0:
            RecordId = self.ui.RecordID_txtbx.toPlainText()
            ImdbId = self.ui.IMDbID_txtbx.toPlainText()
            if RecordId.strip() == "":
                if ImdbId.strip() == "":
                    print("Both empty")
                    self.PopupScreen = Popup_Screen.PopUp()
                else:
                    print("ImdbId")
                    self.SearchData(ImdbId, 2)
            else:
                print("RecordId")
                self.SearchData(RecordId, 0)
        else:
            self.PopupScreen = Popup_Screen.PopUp()
        print("Finished Searching Table")

    def SearchData(self, CheckData, position):
        print("Search Table Method")
        FoundList = []
        InputList = []
        for i in range(len(self.DownloadedTableData)):
            if CheckData == str(self.DownloadedTableData[i][position]):
                for x in range(len(self.DownloadedTableData[0])):
                    InputList.append(str(self.DownloadedTableData[i][x]))
        if not InputList:
            self.load_table(self.DownloadedTableData)
        else:
            FoundList.append(InputList)
            self.load_table(FoundList)
        print("Finished Search Table Method")

    @pyqtSlot()
    def Delete_Click(self):
        print("Deleting")
        if self.NoInTable == 0 or self.NoInTable > 1:
            self.PopupScreen = Popup_Screen.PopUp()
            print("Couldnt Deleted Record")
        else:
            _Main.DeleteData(self.path, self.Table, self.CurrentTableData[0][0])
            self.Refresh_Clicked()
            print("Finished Deleting")

    @pyqtSlot()
    def load_table(self, TableData):
        print("Loading Table")
        self.ui.Download_tbl.setRowCount(0)
        self.NoInTable = 0
        self.CurrentTableData = TableData
        if TableData != 0:
            self.NoInTable = len(TableData)
            self.CurrentTableData = TableData
            self.ColumnNames = _Main.FetchColumnNames(self.path, self.Table)
            self.ui.Download_tbl.setColumnCount(len(TableData[0]))
            self.ui.Download_tbl.setHorizontalHeaderLabels(self.ColumnNames)
            for i in range(len(TableData)):
                self.ui.Download_tbl.setRowCount(i + 1)
                for y in range(len(TableData[0])):
                    self.ui.Download_tbl.setItem(i, y, QTableWidgetItem(str(TableData[i][y])))
            self.ui.Download_tbl.verticalHeader().hide()
        print("Finished Loading Table")


if __name__ == "__main__":
    app1 = QtWidgets.QApplication(sys.argv)
    window1 = WishList()
    sys.exit(app1.exec_())

