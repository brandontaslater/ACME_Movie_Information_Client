from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from UI.Popup_Screen import Ui_MainWindow


class PopUp(QtWidgets.QMainWindow):
    def __init__(self):
        print("Pop Up Window")
        super(PopUp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
