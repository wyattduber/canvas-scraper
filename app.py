# Standard Python Packages
import os
import sys
import ctypes
import pexpect
from sys import platform
import logging

# PyQt6 Packages
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# Stuff from Project
from widgets import HomeWidget
from widgets import WindowsWidget
from widgets import config

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    EXIT_CODE_REBOOT = -123

    def __init__(self):
        super(MainWindow, self).__init__()

        # logging
        if os.path.exists(config.DEFAULT_LOG_FILE):
            try:
                os.remove(config.DEFAULT_LOG_FILE)
            except Exception as e:
                # throws an error if restart button is clicked as the logger is still running. Just don't delete the
                # file in this case
                print(f"Error removing log file {config.DEFAULT_LOG_FILE}! Exception: {e}")
        logging.basicConfig(level=config.CONSOLE_LOG_LEVEL, format=config.LOG_FORMAT)
        self.logger = logging.getLogger(__name__)
        fh = logging.FileHandler(config.DEFAULT_LOG_FILE)
        fh.setLevel(config.FILE_LOG_LEVEL)
        formatter = logging.Formatter(config.LOG_FORMAT)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)    


        self.setupUi(self)
        self.threadpool = QThreadPool()
        self.exception_close = False

        # Widgets
        self.home = HomeWidget(self)
        self.windows = WindowsWidget(self)

        from widgets import StackedLayout
        self.centerWidget = QtWidgets.QWidget()
        self.centerLayout = QVBoxLayout()
        self.centerLayout.addLayout(self.stack)
        self.centerWidget.setLayout(self.centerLayout)
        self.setCentralWidget(self.centerWidget)

        self.widgets = []
        self.widgets.append(self.home)
        self.widgets.append(self.windows)
        # Add more widgets here #
        for widget in self.widgets:
            self.stack.addWidget(widget)
        self.stack.setCurrentIndex(0)

        self.current_index = 0

        self.show()

    ### The following are methods for switching to different widgets of the gui application. ###

    def switchToHome(self):
        self.stack.setCurrentIndex(0)
        self.current_index = 0
        self.logger.debug("Switched to Home")

    def switchToWindows(self):
        self.stack.setCurrentIndex(1)
        self.current_index = 1
        self.logger.debug("Switched to Windows")

    def closeEvent(self, event):
        if self.exception_close:
            self.logger.debug("Exited window from exception")
            return
        close = QMessageBox.question(self,
                                     "Quit Canvas Scraper",
                                     "Are you sure?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            self.logger.debug("Exited window")
            event.accept()
        else:
            event.ignore()

class StackedLayout(QtWidgets.QStackedLayout):
    def minimumSize(self):
        if self.currentWidget():
            s = self.currentWidget().minimumSize()
            if s.isEmpty():
                s = self.currentWidget().minimumSizeHint()
            return s
        return super().minimumSize()


if __name__ == "__main__":
    app = None
    currentExitCode = MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        app = QtWidgets.QApplication(sys.argv)
        main = MainWindow()
        currentExitCode = app.exec_()
        app = None