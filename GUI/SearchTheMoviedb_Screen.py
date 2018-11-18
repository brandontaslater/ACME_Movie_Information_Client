import os
from os.path import normpath

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from _OMDb import AccessWebsite
from _TMDb import AccessWebsite
from GUI import SearchResultMovieDb_Screen
from UI.SearchTheMoviedb_Screen import Ui_Dialog


class SearchWindow(QtWidgets.QDialog):
    def __init__(self, WebsiteName):
        print("SearchWindow TMDB")
        location = str(os.getcwd()) + "\ACME_Storage.db"
        self.path = normpath(location)
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
        print("Searching TMDb")
        self.ParameterList.append(self.ui.MovieTitle_txtbx.toPlainText())
        self.ParameterList.append(self.ui.APIKey_txtbx.toPlainText())
        WebsiteInfo = AccessWebsite.ChromeAccessURL(self.ParameterList, self.WebsiteName)
        self.DataDictionary = WebsiteInfo.get_dict()
        self.close()
        self.SearchResult = SearchResultMovieDb_Screen.SearchResultWindow(self.DataDictionary)
        print("Finished Searching TMDB")

    def get_dict(self):
        print("Returning Dictionary")
        return self.DataDictionary


