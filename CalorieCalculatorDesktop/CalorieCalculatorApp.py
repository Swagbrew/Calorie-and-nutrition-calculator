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
        MainWindow.resize(1001, 851)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(0, 10, 1001, 61))
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
        self.labelKcal.setGeometry(QtCore.QRect(30, 160, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelKcal.setFont(font)
        self.labelKcal.setObjectName("labelKcal")
        self.labelWegl = QtWidgets.QLabel(self.centralwidget)
        self.labelWegl.setGeometry(QtCore.QRect(30, 200, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelWegl.setFont(font)
        self.labelWegl.setObjectName("labelWegl")
        self.labelBia = QtWidgets.QLabel(self.centralwidget)
        self.labelBia.setGeometry(QtCore.QRect(30, 240, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelBia.setFont(font)
        self.labelBia.setObjectName("labelBia")
        self.labelTlu = QtWidgets.QLabel(self.centralwidget)
        self.labelTlu.setGeometry(QtCore.QRect(30, 280, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.labelTlu.setFont(font)
        self.labelTlu.setObjectName("labelTlu")
        self.valueKcal = QtWidgets.QLabel(self.centralwidget)
        self.valueKcal.setGeometry(QtCore.QRect(420, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueKcal.setFont(font)
        self.valueKcal.setAlignment(QtCore.Qt.AlignCenter)
        self.valueKcal.setObjectName("valueKcal")
        self.valueWegl = QtWidgets.QLabel(self.centralwidget)
        self.valueWegl.setGeometry(QtCore.QRect(420, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueWegl.setFont(font)
        self.valueWegl.setAlignment(QtCore.Qt.AlignCenter)
        self.valueWegl.setObjectName("valueWegl")
        self.valueBia = QtWidgets.QLabel(self.centralwidget)
        self.valueBia.setGeometry(QtCore.QRect(420, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueBia.setFont(font)
        self.valueBia.setAlignment(QtCore.Qt.AlignCenter)
        self.valueBia.setObjectName("valueBia")
        self.valueTlu = QtWidgets.QLabel(self.centralwidget)
        self.valueTlu.setGeometry(QtCore.QRect(420, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueTlu.setFont(font)
        self.valueTlu.setAlignment(QtCore.Qt.AlignCenter)
        self.valueTlu.setObjectName("valueTlu")
        self.scrollAreaProducts = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollAreaProducts.setGeometry(QtCore.QRect(30, 390, 421, 431))
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
        self.scrollAreaSelectedProducts.setGeometry(QtCore.QRect(550, 390, 421, 431))
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
        self.comboTypes.setGeometry(QtCore.QRect(30, 330, 205, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboTypes.setFont(font)
        self.comboTypes.setObjectName("comboTypes")
        self.progressKcal = QtWidgets.QProgressBar(self.centralwidget)
        self.progressKcal.setGeometry(QtCore.QRect(590, 160, 381, 31))
        self.progressKcal.setProperty("value", 24)
        self.progressKcal.setTextVisible(False)
        self.progressKcal.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressKcal.setObjectName("progressKcal")
        self.progressWegl = QtWidgets.QProgressBar(self.centralwidget)
        self.progressWegl.setGeometry(QtCore.QRect(590, 200, 381, 31))
        self.progressWegl.setProperty("value", 24)
        self.progressWegl.setTextVisible(False)
        self.progressWegl.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressWegl.setObjectName("progressWegl")
        self.progressBia = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBia.setGeometry(QtCore.QRect(590, 240, 381, 31))
        self.progressBia.setProperty("value", 24)
        self.progressBia.setTextVisible(False)
        self.progressBia.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBia.setObjectName("progressBia")
        self.progressTlu = QtWidgets.QProgressBar(self.centralwidget)
        self.progressTlu.setGeometry(QtCore.QRect(590, 280, 381, 31))
        self.progressTlu.setProperty("value", 24)
        self.progressTlu.setTextVisible(False)
        self.progressTlu.setInvertedAppearance(False)
        self.progressTlu.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressTlu.setObjectName("progressTlu")
        self.insertDataButton = QtWidgets.QPushButton(self.centralwidget)
        self.insertDataButton.setGeometry(QtCore.QRect(380, 70, 241, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.insertDataButton.sizePolicy().hasHeightForWidth())
        self.insertDataButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.insertDataButton.setFont(font)
        self.insertDataButton.setObjectName("insertDataButton")
        self.valueActualKcal = QtWidgets.QLabel(self.centralwidget)
        self.valueActualKcal.setGeometry(QtCore.QRect(510, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueActualKcal.setFont(font)
        self.valueActualKcal.setAlignment(QtCore.Qt.AlignCenter)
        self.valueActualKcal.setObjectName("valueActualKcal")
        self.valueActualWegl = QtWidgets.QLabel(self.centralwidget)
        self.valueActualWegl.setGeometry(QtCore.QRect(510, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueActualWegl.setFont(font)
        self.valueActualWegl.setAlignment(QtCore.Qt.AlignCenter)
        self.valueActualWegl.setObjectName("valueActualWegl")
        self.valueActualTlu = QtWidgets.QLabel(self.centralwidget)
        self.valueActualTlu.setGeometry(QtCore.QRect(510, 280, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueActualTlu.setFont(font)
        self.valueActualTlu.setAlignment(QtCore.Qt.AlignCenter)
        self.valueActualTlu.setObjectName("valueActualTlu")
        self.valueActualBia = QtWidgets.QLabel(self.centralwidget)
        self.valueActualBia.setGeometry(QtCore.QRect(510, 240, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.valueActualBia.setFont(font)
        self.valueActualBia.setAlignment(QtCore.Qt.AlignCenter)
        self.valueActualBia.setObjectName("valueActualBia")
        self.buttonNewProduct = QtWidgets.QPushButton(self.centralwidget)
        self.buttonNewProduct.setGeometry(QtCore.QRect(770, 330, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonNewProduct.setFont(font)
        self.buttonNewProduct.setObjectName("buttonNewProduct")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(490, 160, 20, 31))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(490, 200, 21, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(490, 240, 21, 31))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(490, 280, 21, 31))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.labelMax = QtWidgets.QLabel(self.centralwidget)
        self.labelMax.setGeometry(QtCore.QRect(420, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelMax.setFont(font)
        self.labelMax.setAlignment(QtCore.Qt.AlignCenter)
        self.labelMax.setObjectName("labelMax")
        self.labelActual = QtWidgets.QLabel(self.centralwidget)
        self.labelActual.setGeometry(QtCore.QRect(500, 130, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelActual.setFont(font)
        self.labelActual.setAlignment(QtCore.Qt.AlignCenter)
        self.labelActual.setObjectName("labelActual")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(420, 150, 161, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header.setText(_translate("MainWindow", "Kalkulator kalorii i wartości odżywczych"))
        self.labelKcal.setText(_translate("MainWindow", "Zapotrzebowanie kalorii wynosi [kcal]: "))
        self.labelWegl.setText(_translate("MainWindow", "Zapotrzebowanie węglowodanów [g]: "))
        self.labelBia.setText(_translate("MainWindow", "Zapotrzebowanie białek [g]:"))
        self.labelTlu.setText(_translate("MainWindow", "Zapotrzebowanie tłuszczy [g]:"))
        self.valueKcal.setText(_translate("MainWindow", "123456"))
        self.valueWegl.setText(_translate("MainWindow", "TextLabel"))
        self.valueBia.setText(_translate("MainWindow", "TextLabel"))
        self.valueTlu.setText(_translate("MainWindow", "TextLabel"))
        self.progressKcal.setFormat(_translate("MainWindow", "%p"))
        self.progressWegl.setFormat(_translate("MainWindow", "%p"))
        self.progressBia.setFormat(_translate("MainWindow", "%p"))
        self.progressTlu.setFormat(_translate("MainWindow", "%p"))
        self.insertDataButton.setText(_translate("MainWindow", "Wprowadź swoje dane"))
        self.valueActualKcal.setText(_translate("MainWindow", "123456"))
        self.valueActualWegl.setText(_translate("MainWindow", "TextLabel"))
        self.valueActualTlu.setText(_translate("MainWindow", "TextLabel"))
        self.valueActualBia.setText(_translate("MainWindow", "TextLabel"))
        self.buttonNewProduct.setText(_translate("MainWindow", "Dodaj nowy produkt"))
        self.labelMax.setText(_translate("MainWindow", "Maks"))
        self.labelActual.setText(_translate("MainWindow", "Aktualnie"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
