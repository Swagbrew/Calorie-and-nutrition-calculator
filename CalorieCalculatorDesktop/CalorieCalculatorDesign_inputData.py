# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalorieCalculatorDesign_inputData.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 640)
        self.header2 = QtWidgets.QLabel(Form)
        self.header2.setGeometry(QtCore.QRect(0, 210, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header2.sizePolicy().hasHeightForWidth())
        self.header2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header2.setFont(font)
        self.header2.setAutoFillBackground(False)
        self.header2.setTextFormat(QtCore.Qt.AutoText)
        self.header2.setScaledContents(True)
        self.header2.setAlignment(QtCore.Qt.AlignCenter)
        self.header2.setWordWrap(False)
        self.header2.setObjectName("header2")
        self.radioButtonHigh = QtWidgets.QRadioButton(Form)
        self.radioButtonHigh.setGeometry(QtCore.QRect(40, 480, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonHigh.setFont(font)
        self.radioButtonHigh.setObjectName("radioButtonHigh")
        self.radioButtonAverage = QtWidgets.QRadioButton(Form)
        self.radioButtonAverage.setGeometry(QtCore.QRect(40, 390, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonAverage.setFont(font)
        self.radioButtonAverage.setObjectName("radioButtonAverage")
        self.labelLow = QtWidgets.QLabel(Form)
        self.labelLow.setGeometry(QtCore.QRect(20, 360, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelLow.setFont(font)
        self.labelLow.setObjectName("labelLow")
        self.labelAge = QtWidgets.QLabel(Form)
        self.labelAge.setGeometry(QtCore.QRect(40, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAge.setFont(font)
        self.labelAge.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelAge.setObjectName("labelAge")
        self.textBrowserHigh = QtWidgets.QTextBrowser(Form)
        self.textBrowserHigh.setGeometry(QtCore.QRect(20, 510, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowserHigh.setFont(font)
        self.textBrowserHigh.setAutoFillBackground(True)
        self.textBrowserHigh.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowserHigh.setLineWidth(0)
        self.textBrowserHigh.setObjectName("textBrowserHigh")
        self.radioButtonVeryLow = QtWidgets.QRadioButton(Form)
        self.radioButtonVeryLow.setGeometry(QtCore.QRect(40, 270, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonVeryLow.setFont(font)
        self.radioButtonVeryLow.setObjectName("radioButtonVeryLow")
        self.radioButtonPro = QtWidgets.QRadioButton(Form)
        self.radioButtonPro.setGeometry(QtCore.QRect(40, 550, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonPro.setFont(font)
        self.radioButtonPro.setObjectName("radioButtonPro")
        self.labelHeight = QtWidgets.QLabel(Form)
        self.labelHeight.setGeometry(QtCore.QRect(40, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelHeight.setFont(font)
        self.labelHeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelHeight.setObjectName("labelHeight")
        self.lineEditAge = QtWidgets.QLineEdit(Form)
        self.lineEditAge.setGeometry(QtCore.QRect(160, 70, 161, 31))
        self.lineEditAge.setObjectName("lineEditAge")
        self.lineEditHeight = QtWidgets.QLineEdit(Form)
        self.lineEditHeight.setGeometry(QtCore.QRect(160, 170, 161, 31))
        self.lineEditHeight.setObjectName("lineEditHeight")
        self.textBrowserAverage = QtWidgets.QTextBrowser(Form)
        self.textBrowserAverage.setGeometry(QtCore.QRect(20, 420, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowserAverage.setFont(font)
        self.textBrowserAverage.setAutoFillBackground(False)
        self.textBrowserAverage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowserAverage.setLineWidth(0)
        self.textBrowserAverage.setObjectName("textBrowserAverage")
        self.header = QtWidgets.QLabel(Form)
        self.header.setGeometry(QtCore.QRect(0, 0, 401, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.header.setFont(font)
        self.header.setAutoFillBackground(False)
        self.header.setTextFormat(QtCore.Qt.AutoText)
        self.header.setScaledContents(True)
        self.header.setAlignment(QtCore.Qt.AlignCenter)
        self.header.setWordWrap(False)
        self.header.setObjectName("header")
        self.lineEditWeight = QtWidgets.QLineEdit(Form)
        self.lineEditWeight.setGeometry(QtCore.QRect(160, 120, 161, 31))
        self.lineEditWeight.setObjectName("lineEditWeight")
        self.labelVeryLow = QtWidgets.QLabel(Form)
        self.labelVeryLow.setGeometry(QtCore.QRect(20, 300, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelVeryLow.setFont(font)
        self.labelVeryLow.setObjectName("labelVeryLow")
        self.radioButtonLow = QtWidgets.QRadioButton(Form)
        self.radioButtonLow.setGeometry(QtCore.QRect(40, 330, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonLow.setFont(font)
        self.radioButtonLow.setObjectName("radioButtonLow")
        self.labelWeight = QtWidgets.QLabel(Form)
        self.labelWeight.setGeometry(QtCore.QRect(40, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelWeight.setFont(font)
        self.labelWeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelWeight.setObjectName("labelWeight")
        self.buttonReady = QtWidgets.QPushButton(Form)
        self.buttonReady.setGeometry(QtCore.QRect(130, 590, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttonReady.setFont(font)
        self.buttonReady.setObjectName("buttonReady")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header2.setText(_translate("Form", "Jaka jest twoja aktywność fizyczna?"))
        self.radioButtonHigh.setText(_translate("Form", "Wysoka"))
        self.radioButtonAverage.setText(_translate("Form", "Umiarkowana"))
        self.labelLow.setText(_translate("Form", "Praca siedziąca, do 3 lekkich treningów w tygodniu"))
        self.labelAge.setText(_translate("Form", "Wiek"))
        self.textBrowserHigh.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Praca fizyczna, do 4 treningów w tygodniu</p></body></html>"))
        self.radioButtonVeryLow.setText(_translate("Form", "Bardzo niska"))
        self.radioButtonPro.setText(_translate("Form", "Zawodowe uprawianie sportu"))
        self.labelHeight.setText(_translate("Form", "Wzrost [cm]"))
        self.textBrowserAverage.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Praca siedząca, do 4 treningów w tygodniu lub praca fizyczna bez treningów</span></p></body></html>"))
        self.header.setText(_translate("Form", "Wprowadź swoje dane"))
        self.labelVeryLow.setText(_translate("Form", "Praca siedziąca, brak treningów"))
        self.radioButtonLow.setText(_translate("Form", "Niska"))
        self.labelWeight.setText(_translate("Form", "Waga [kg]"))
        self.buttonReady.setText(_translate("Form", "Gotowe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
