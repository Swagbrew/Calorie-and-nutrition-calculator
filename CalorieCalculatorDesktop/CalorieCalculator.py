from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 800, 500)
    win.setWindowTitle("Calorie and Nutrition Calculator")

    win.show()
    sys.exit(app.exec_())


window()