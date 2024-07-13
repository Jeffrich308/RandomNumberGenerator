# -------------------------------------------------------------------------------
# Name:             Random.py
# Purpose:          Simplify Example of a Random Number Generator
#
# Author:           Jeffreaux
#
# Created:          13 July 24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit, QLabel
from PyQt5 import uic
import sys
import random


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Random_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.actExit = self.findChild(QAction, "actExit")
        self.txtMax = self.findChild(QLineEdit, "txtMax")
        self.btnGo = self.findChild(QPushButton, "btnGo")
        self.lblResults = self.findChild(QLabel, "lblResults")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.btnGo.clicked.connect(self.get_random)
        self.txtMax.returnPressed.connect(self.get_random)

        self.actExit.triggered.connect(self.closeEvent)

        # Show the app
        self.show()

    def get_random(self):
        min_value = 1
        # Get ending value from user input
        max_value = int(self.txtMax.text())  # Setting the Max value
        # Generate the number from the values given
        roll = random.randint(min_value, max_value)
        print(roll)
        # Print results to the form
        self.lblResults.setText(str(roll))
        self.txtMax.clear()  # Clears the text box after running

    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
