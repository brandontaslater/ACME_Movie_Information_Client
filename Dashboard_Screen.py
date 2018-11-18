import sys
import random
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

from GUI import SearchResultOMDB_Screen, SearchOMDB_Screen, SearchTheMoviedb_Screen, DownloadViewer_Screen, \
    WishList_Screen
from InitialiseDB import _Main
from _OMDb import AccessWebsite
from UI.Dashboard_Screen import Ui_MainWindow


class Dashboard(QtWidgets.QMainWindow):
    def __init__(self):
        print("Dashboard")
        _Main.main()
        self.Dictionary = {}
        super(Dashboard, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # The open movie db Buttons
        self.ui.SearchOMDb_btn.clicked.connect(self.SearchOMDb_Clicked)
        self.ui.ViewDownloadOMDb_btn.clicked.connect(self.ViewDownloadOMDb_Clicked)

        # The movie db Buttons
        self.ui.SearchTMDb_btn.clicked.connect(self.SearchTMDb_Clicked)
        self.ui.ViewDownloadTMDb_btn.clicked.connect(self.ViewDownloadTMDb_Clicked)

        # Wish list Button
        self.ui.WishList_btn.clicked.connect(self.WishList_Clicked)
        self.ui.Random_btn.clicked.connect(self.Randomise)


    @pyqtSlot()
    def Randomise(self):
        print("Randomising Movie/Tv show")
        imdbId = "tt"
        for i in range(7):
            imdbId = imdbId + str(random.randint(1, 9))
        parameterList = [imdbId, "", "", "", "full", "Json", "7476698c", ]
        WebsiteInfo = AccessWebsite.ChromeAccessURL(parameterList, 'DownloadHistoryOMDb')
        DataDictionary = WebsiteInfo.get_dict()
        Dictionary = list(DataDictionary.values())
        if Dictionary[0] == "N/A":
            print("Unable to print Movie/Tv show")
        else:
            self.SearchResult = SearchResultOMDB_Screen.SearchResultWindow(DataDictionary)
            print("Finished Randomising Movie/Tv show")

    @pyqtSlot()
    def SearchOMDb_Clicked(self):
        print("Search OMDB")
        self.SearchOMDbScreen = SearchOMDB_Screen.SearchWindow('DownloadHistoryOMDb')


    @pyqtSlot()
    def SearchTMDb_Clicked(self):
        print("Search TMDB")
        self.SearchTMDbScreen = SearchTheMoviedb_Screen.SearchWindow('DownloadHistoryTMDb')

    @pyqtSlot()
    def ViewDownloadOMDb_Clicked(self):
        print("Downloaded History OMDB")
        self.DownloadOMDbViewer = DownloadViewer_Screen.DownloadViewer('DownloadHistoryOMDb')


    @pyqtSlot()
    def ViewDownloadTMDb_Clicked(self):
        print("Downloaded History TMDB")
        self.DownloadOMDbViewer = DownloadViewer_Screen.DownloadViewer('DownloadHistoryTMDb')


    @pyqtSlot()
    def WishList_Clicked(self):
        print("Wish List")
        self.WishList = WishList_Screen.WishList('WishList')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())

