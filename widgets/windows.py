
 # Standard Python Packages
import time

# Selenium Packages
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# PyQt6 Packages
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# Stuff From Project
from generated.WindowsUI import Ui_WindowsWidget

# Config
from widgets import config

# Windows Driver File
driver = webdriver.Chrome(config.DRIVER_PATH)

class WindowsWidget(QtWidgets.QWidget, Ui_WindowsWidget):

    def __init__(self, mainWindow):
        super(WindowsWidget, self).__init__()
        self.setupUi(self)

        self.mainWindow = mainWindow

        # Share resources from main window
        self.threadpool = self.mainWindow.threadpool
        self.logger = self.mainWindow.logger


    def start(self):
        driver.get(config.CANVAS_URL)
        filesFound = 0
        time.sleep(15)
        for x in range(19993700, 20597550):
            driver.switch_to.window(driver.window_handles[0])
            filesFound += self.canvasFileDownloader(f"{config.CANVAS_URL}/courses/{config.COURSE_ID}/files/{x}", filesFound)
            driver.close()


    def canvasFileDownloader(self, url, ff):
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(f'{url}/download')
        timeout = .1
        try:
            element_present = EC.presence_of_element_located((By.ID, 'main'))
            WebDriverWait(driver, timeout).until(element_present)
        except TimeoutException:
            ff += 1
            print("File Found! " + str(ff) + " files found so far!")
            return 1
        finally:
            return 0


    def _show_error(self, message):
        """Private method to just show an error message box with a custom message"""
        self.logger.error(message)
        errorbox = QMessageBox(self)
        errorbox.setWindowTitle("Error")
        errorbox.setText(message)
        errorbox.setIcon(QMessageBox.Critical)
        errorbox.exec()


    def _show_message(self, title, message, subtext=None):
        """Private method to just show an info message box with a custom message"""
        self.logger.info(message)
        messagebox = QMessageBox(self)
        messagebox.setWindowTitle(title)
        messagebox.setText(message)
        messagebox.setInformativeText(subtext)
        messagebox.setIcon(QMessageBox.Information)
        messagebox.show()
        return messagebox
    