import os
from os.path import normpath
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from InitialiseDB import _Main
from UI.SearchResultTheMoviedb_Screen import Ui_Dialog


class SearchResultWindow(QtWidgets.QDialog):
    def __init__(self, dictionary):
        print("Search Result Window TMDB")
        location = str(os.getcwd()) + "\ACME_Storage.db"
        self.path = normpath(location)
        self.DictionaryData = dictionary
        self.Dictionary = list(dictionary.values())
        super(SearchResultWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.SetText()
        self.show()

    @pyqtSlot()
    def SetText(self):
        print("Setting Text")
        if self.Dictionary[0] == "N/A":
            self.Dictionary.pop()
            for i in range(14):
                self.Dictionary.append("No Data Found")
        self.ui.Title_txtbx.setText(str(self.Dictionary[4]))
        self.ui.OriginalTitle_txtbx.setText(str(self.Dictionary[8]))
        self.ui.GenreIds_txtbx.setText(str(self.Dictionary[9]))
        self.ui.Released_txtbx.setText(str(self.Dictionary[13]))
        self.ui.Adult_txtbx.setText(str(self.Dictionary[11]))
        self.ui.IMDbID_txtbx.setText(str(self.Dictionary[1]))
        self.ui.VoteAverage_txtbx.setText(str(self.Dictionary[3]))
        self.ui.VoteCount_txtbx.setText(str(self.Dictionary[0]))
        self.ui.Video_txtbx.setText(str(self.Dictionary[2]))
        self.ui.Popularity_txtbx.setText(str(self.Dictionary[5]))
        self.ui.PosterPath_txtbx.setText(str(self.Dictionary[6]))
        self.ui.OriginalLanguage_txtbx.setText(str(self.Dictionary[7]))
        self.ui.BackDropPath_txtbx.setText(str(self.Dictionary[10]))
        self.ui.Plot_txtbx.setText(str(self.Dictionary[12]))
        self.ui.AddWishList_btn.clicked.connect(self.AddWishList_Clicked)
        print("Finished Setting Text")

    @pyqtSlot()
    def AddWishList_Clicked(self):
        print("Adding To Wish List")
        if self.Dictionary[0] != "No Data Found":
            WishlistDict = {'Title': str(self.Dictionary[4]), 'IMDbID': str(self.Dictionary[1]), 'ReleaseDate': str(self.Dictionary[13]), 'Plot': str(self.Dictionary[12])}
            _Main.InsertIntoTable(self.path, 'WishList', WishlistDict)
            print("Finished Adding To Wish List")
