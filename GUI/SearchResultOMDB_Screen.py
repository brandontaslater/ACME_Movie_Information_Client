import os
from os.path import normpath
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from InitialiseDB import _Main
import json
from UI.SearchResultOMDB_Screen import Ui_Dialog


class SearchResultWindow(QtWidgets.QDialog):
    def __init__(self, dictionary):
        print("Search Result Window OMDB")

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
            for i in range(25):
                self.Dictionary.append("No Data Found")
        self.ui.Title_txtbx.setText(self.Dictionary[0])
        self.ui.Year_txtbx.setText(self.Dictionary[1])
        self.ui.Rated_txtbx.setText(self.Dictionary[2])
        self.ui.Released_txtbx.setText(self.Dictionary[3])
        self.ui.Runtime_txtbx.setText(self.Dictionary[4])
        self.ui.Genre_txtbx.setText(self.Dictionary[5])
        self.ui.Director_txtbx.setText(self.Dictionary[6])
        self.ui.Writer_txtbx.setText(self.Dictionary[7])
        self.ui.Actors_txtbx.setText(self.Dictionary[8])
        self.ui.Plot_txtbx.setText(self.Dictionary[9])
        self.ui.Language_txtbx.setText(self.Dictionary[10])
        self.ui.Country_txtbx.setText(self.Dictionary[11])
        self.ui.Awards_txtbx.setText(self.Dictionary[12])
        self.ui.Poster_txtbx.setText(self.Dictionary[13])
        self.ui.Ratings_txtbx.setText(json.dumps(self.Dictionary[14]))
        self.ui.Metascore_txtbx.setText(self.Dictionary[15])
        self.ui.imdbRating_txtbx.setText(self.Dictionary[16])
        self.ui.imdbVotes_txtbx.setText(self.Dictionary[17])
        self.ui.imdbID_txtbx.setText(self.Dictionary[18])
        self.ui.Type_txtbx.setText(self.Dictionary[19])
        self.ui.DVD_txtbx.setText(self.Dictionary[20])
        self.ui.BoxOffice_txtbx.setText(self.Dictionary[21])
        self.ui.Production_txtbx.setText(self.Dictionary[22])
        self.ui.Website_txtbx.setText(self.Dictionary[23])
        self.ui.Response_txtbx.setText(self.Dictionary[24])
        self.ui.AddWishList_btn.clicked.connect(self.AddWishList_Clicked)
        print("Finished Setting Text")

    @pyqtSlot()
    def AddWishList_Clicked(self):
        print("Adding To Wish List")
        if self.Dictionary[0] != "No Data Found":
            WishlistDict = {'Title': str(self.Dictionary[0]), 'IMDbID': str(self.Dictionary[18]),
                            'ReleaseDate': str(self.Dictionary[3]), 'Plot': str(self.Dictionary[9])}
            _Main.InsertIntoTable(self.path, 'WishList', WishlistDict)
            print("Finished Adding To Wish List")
