 # Standard Python Packages
import os

# PyQt6 Packages
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# Stuff From Project
from generated.HomeUI import Ui_HomeWidget

# Config
from widgets import config

class HomeWidget(QtWidgets.QWidget, Ui_HomeWidget):

    def __init__(self, mainWindow):
        super(HomeWidget, self).__init__(parent)
        self.setupUi(self)

        self.mainWindow = mainWindow
        self.threadpool = QThreadPool()

        # Share resources from main window
        self.threadpool = self.mainWindow.threadpool
        self.wrapper = mainWindow.wrapper
        self.logger = self.mainWindow.logger

        self.btnWindows.clicked.connect(self.btnWindowsClicked)
