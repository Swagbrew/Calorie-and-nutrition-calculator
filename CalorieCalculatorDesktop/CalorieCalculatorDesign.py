# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalorieCalculatorDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 0, 991, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.header.setFont(font)
        self.header.setAutoFillBackground(False)
        self.header.setTextFormat(QtCore.Qt.AutoText)
        self.header.setScaledContents(True)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setWordWrap(False)
        self.header.setObjectName("header")
        self.labelKcal = QtWidgets.QLabel(self.centralwidget)
        self.labelKcal.setGeometry(QtCore.QRect(30, 130, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelKcal.setFont(font)
        self.labelKcal.setObjectName("labelKcal")
        self.labelWegl = QtWidgets.QLabel(self.centralwidget)
        self.labelWegl.setGeometry(QtCore.QRect(30, 170, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelWegl.setFont(font)
        self.labelWegl.setObjectName("labelWegl")
        self.labelBia = QtWidgets.QLabel(self.centralwidget)
        self.labelBia.setGeometry(QtCore.QRect(30, 210, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelBia.setFont(font)
        self.labelBia.setObjectName("labelBia")
        self.labelTlu = QtWidgets.QLabel(self.centralwidget)
        self.labelTlu.setGeometry(QtCore.QRect(30, 250, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTlu.setFont(font)
        self.labelTlu.setObjectName("labelTlu")
        self.valueKcal = QtWidgets.QLabel(self.centralwidget)
        self.valueKcal.setGeometry(QtCore.QRect(440, 130, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valueKcal.setFont(font)
        self.valueKcal.setObjectName("valueKcal")
        self.valueWegl = QtWidgets.QLabel(self.centralwidget)
        self.valueWegl.setGeometry(QtCore.QRect(360, 170, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valueWegl.setFont(font)
        self.valueWegl.setObjectName("valueWegl")
        self.valueBia = QtWidgets.QLabel(self.centralwidget)
        self.valueBia.setGeometry(QtCore.QRect(270, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valueBia.setFont(font)
        self.valueBia.setObjectName("valueBia")
        self.valueTlu = QtWidgets.QLabel(self.centralwidget)
        self.valueTlu.setGeometry(QtCore.QRect(290, 250, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.valueTlu.setFont(font)
        self.valueTlu.setObjectName("valueTlu")
        self.scrollAreaProducts = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaProducts.setGeometry(QtCore.QRect(30, 350, 421, 431))
        self.scrollAreaProducts.setWidgetResizable(True)
        self.scrollAreaProducts.setObjectName("scrollAreaProducts")
        self.scrollAreaProducts_2 = QtWidgets.QWidget()
        self.scrollAreaProducts_2.setGeometry(QtCore.QRect(0, 0, 419, 429))
        self.scrollAreaProducts_2.setObjectName("scrollAreaProducts_2")
        self.tableWidgetProducts = QtWidgets.QTableWidget(self.scrollAreaProducts_2)
        self.tableWidgetProducts.setGeometry(QtCore.QRect(0, 0, 421, 481))
        self.tableWidgetProducts.setObjectName("tableWidgetProducts")
        self.tableWidgetProducts.setColumnCount(0)
        self.tableWidgetProducts.setRowCount(0)
        self.scrollAreaProducts.setWidget(self.scrollAreaProducts_2)
        self.scrollAreaSelectedProducts = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaSelectedProducts.setGeometry(QtCore.QRect(540, 350, 421, 431))
        self.scrollAreaSelectedProducts.setWidgetResizable(True)
        self.scrollAreaSelectedProducts.setObjectName("scrollAreaSelectedProducts")
        self.scrollAreaSelectedProducts_2 = QtWidgets.QWidget()
        self.scrollAreaSelectedProducts_2.setGeometry(QtCore.QRect(0, 0, 419, 429))
        self.scrollAreaSelectedProducts_2.setObjectName("scrollAreaSelectedProducts_2")
        self.tableWidgetSelectedProducts = QtWidgets.QTableWidget(self.scrollAreaSelectedProducts_2)
        self.tableWidgetSelectedProducts.setGeometry(QtCore.QRect(-1, 0, 431, 481))
        self.tableWidgetSelectedProducts.setObjectName("tableWidgetSelectedProducts")
        self.tableWidgetSelectedProducts.setColumnCount(0)
        self.tableWidgetSelectedProducts.setRowCount(0)
        self.scrollAreaSelectedProducts.setWidget(self.scrollAreaSelectedProducts_2)
        self.comboTypes = QtWidgets.QComboBox(self.centralwidget)
        self.comboTypes.setGeometry(QtCore.QRect(30, 290, 205, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypes.setFont(font)
        self.comboTypes.setObjectName("comboTypes")
        self.progressKcal = QtWidgets.QProgressBar(self.centralwidget)
        self.progressKcal.setGeometry(QtCore.QRect(540, 130, 371, 31))
        self.progressKcal.setProperty("value", 24)
        self.progressKcal.setTextVisible(True)
        self.progressKcal.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressKcal.setObjectName("progressKcal")
        self.progressWegl = QtWidgets.QProgressBar(self.centralwidget)
        self.progressWegl.setGeometry(QtCore.QRect(540, 170, 371, 31))
        self.progressWegl.setProperty("value", 24)
        self.progressWegl.setTextVisible(True)
        self.progressWegl.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressWegl.setObjectName("progressWegl")
        self.progressBia = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBia.setGeometry(QtCore.QRect(540, 210, 371, 31))
        self.progressBia.setProperty("value", 24)
        self.progressBia.setTextVisible(True)
        self.progressBia.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBia.setObjectName("progressBia")
        self.progressTlu = QtWidgets.QProgressBar(self.centralwidget)
        self.progressTlu.setGeometry(QtCore.QRect(540, 250, 371, 31))
        self.progressTlu.setProperty("value", 24)
        self.progressTlu.setTextVisible(True)
        self.progressTlu.setInvertedAppearance(False)
        self.progressTlu.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressTlu.setObjectName("progressTlu")
        self.insertDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.insertDataButton.setGeometry(QtCore.QRect(380, 70, 235, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertDataButton.sizePolicy().hasHeightForWidth())
        self.insertDataButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.insertDataButton.setFont(font)
        self.insertDataButton.setObjectName("insertDataButton")
        self.valueKcal_2 = QtWidgets.QLabel(self.centralwidget)
        self.valueKcal_2.setGeometry(QtCore.QRect(920, 130, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.valueKcal_2.setFont(font)
        self.valueKcal_2.setObjectName("valueKcal_2")
        self.valueKcal_3 = QtWidgets.QLabel(self.centralwidget)
        self.valueKcal_3.setGeometry(QtCore.QRect(920, 170, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.valueKcal_3.setFont(font)
        self.valueKcal_3.setObjectName("valueKcal_3")
        self.valueKcal_4 = QtWidgets.QLabel(self.centralwidget)
        self.valueKcal_4.setGeometry(QtCore.QRect(920, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.valueKcal_4.setFont(font)
        self.valueKcal_4.setObjectName("valueKcal_4")
        self.valueKcal_5 = QtWidgets.QLabel(self.centralwidget)
        self.valueKcal_5.setGeometry(QtCore.QRect(920, 250, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.valueKcal_5.setFont(font)
        self.valueKcal_5.setObjectName("valueKcal_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Kalkulator kalorii i wartości odżywczych"))
        self.labelKcal.setText(_translate("MainWindow", "Dziennie zapotrzebowanie kalorii wynosi [kcal]: "))
        self.labelWegl.setText(_translate("MainWindow", "Zapotrzebowanie węglowodanów [g]: "))
        self.labelBia.setText(_translate("MainWindow", "Zapotrzebowanie białek [g]:"))
        self.labelTlu.setText(_translate("MainWindow", "Zapotrzebowanie tłuszczy [g]:"))
        self.valueKcal.setText(_translate("MainWindow", "TextLabel"))
        self.valueWegl.setText(_translate("MainWindow", "TextLabel"))
        self.valueBia.setText(_translate("MainWindow", "TextLabel"))
        self.valueTlu.setText(_translate("MainWindow", "TextLabel"))
        self.progressKcal.setFormat(_translate("MainWindow", "%p"))
        self.progressWegl.setFormat(_translate("MainWindow", "%p"))
        self.progressBia.setFormat(_translate("MainWindow", "%p"))
        self.progressTlu.setFormat(_translate("MainWindow", "%p"))
        self.insertDataButton.setText(_translate("MainWindow", "Wprowadź swoje dane"))
        self.valueKcal_2.setText(_translate("MainWindow", "TextLabel"))
        self.valueKcal_3.setText(_translate("MainWindow", "TextLabel"))
        self.valueKcal_4.setText(_translate("MainWindow", "TextLabel"))
        self.valueKcal_5.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
