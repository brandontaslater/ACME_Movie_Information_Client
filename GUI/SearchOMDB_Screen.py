from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from _OMDb import AccessWebsite
from GUI import SearchResultOMDB_Screen
from UI.SearchOMDB_Screen import Ui_Dialog


class SearchWindow(QtWidgets.QDialog):
    def __init__(self, WebsiteName):
        print("SearchWindow OMDB")
        self.WebsiteName = WebsiteName
        self.ParameterList = []
        self.DataDictionary = {}
        super(SearchWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Search_btn.clicked.connect(self.Search_Click)
        self.show()


    @pyqtSlot()
    def Search_Click(self):
        print("Searching OMDB")
        self.ParameterList.append(self.ui.MovieID_txtbx.toPlainText())
        self.ParameterList.append(self.ui.MovieTitle_txtbx.toPlainText())
        self.ParameterList.append(self.ui.Type_txtbx.toPlainText())
        self.ParameterList.append(self.ui.Year_txtbx.toPlainText())
        self.ParameterList.append(self.ui.Plot_txtbx.toPlainText())
        self.ParameterList.append(self.ui.ReturnType_txtbx.toPlainText())
        self.ParameterList.append(self.ui.APIKey_txtbx.toPlainText())
        WebsiteInfo = AccessWebsite.ChromeAccessURL(self.ParameterList, self.WebsiteName)
        self.DataDictionary = WebsiteInfo.get_dict()
        self.close()
        self.SearchResult = SearchResultOMDB_Screen.SearchResultWindow(self.DataDictionary)
        print("Finished Searching OMDB")

    def get_dict(self):
        print("Returning Dictionary")
        return self.DataDictionary


