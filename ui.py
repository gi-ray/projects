# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(906, 488)
        MainWindow.setStyleSheet("background-image: url(:/image/images/download.jpeg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.p_card_1 = QtWidgets.QLabel(self.centralwidget)
        self.p_card_1.setGeometry(QtCore.QRect(570, 340, 101, 141))
        self.p_card_1.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.p_card_1.setText("")
        self.p_card_1.setScaledContents(True)
        self.p_card_1.setObjectName("p_card_1")
        self.d_card_1 = QtWidgets.QLabel(self.centralwidget)
        self.d_card_1.setGeometry(QtCore.QRect(570, 10, 101, 141))
        self.d_card_1.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.d_card_1.setText("")
        self.d_card_1.setScaledContents(True)
        self.d_card_1.setObjectName("d_card_1")
        self.p_card_2 = QtWidgets.QLabel(self.centralwidget)
        self.p_card_2.setGeometry(QtCore.QRect(460, 340, 101, 141))
        self.p_card_2.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.p_card_2.setText("")
        self.p_card_2.setScaledContents(True)
        self.p_card_2.setObjectName("p_card_2")
        self.p_card_3 = QtWidgets.QLabel(self.centralwidget)
        self.p_card_3.setGeometry(QtCore.QRect(350, 340, 101, 141))
        self.p_card_3.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.p_card_3.setText("")
        self.p_card_3.setScaledContents(True)
        self.p_card_3.setObjectName("p_card_3")
        self.p_card_4 = QtWidgets.QLabel(self.centralwidget)
        self.p_card_4.setGeometry(QtCore.QRect(240, 340, 101, 141))
        self.p_card_4.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.p_card_4.setText("")
        self.p_card_4.setScaledContents(True)
        self.p_card_4.setObjectName("p_card_4")
        self.p_card_5 = QtWidgets.QLabel(self.centralwidget)
        self.p_card_5.setGeometry(QtCore.QRect(130, 340, 101, 141))
        self.p_card_5.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.p_card_5.setText("")
        self.p_card_5.setScaledContents(True)
        self.p_card_5.setObjectName("p_card_5")
        self.p_card_6 = QtWidgets.QLabel(self.centralwidget)
        self.p_card_6.setGeometry(QtCore.QRect(20, 340, 101, 141))
        self.p_card_6.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.p_card_6.setText("")
        self.p_card_6.setScaledContents(True)
        self.p_card_6.setObjectName("p_card_6")
        self.d_card_2 = QtWidgets.QLabel(self.centralwidget)
        self.d_card_2.setGeometry(QtCore.QRect(460, 10, 101, 141))
        self.d_card_2.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.d_card_2.setText("")
        self.d_card_2.setScaledContents(True)
        self.d_card_2.setObjectName("d_card_2")
        self.d_card_3 = QtWidgets.QLabel(self.centralwidget)
        self.d_card_3.setGeometry(QtCore.QRect(350, 10, 101, 141))
        self.d_card_3.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.d_card_3.setText("")
        self.d_card_3.setScaledContents(True)
        self.d_card_3.setObjectName("d_card_3")
        self.d_card_4 = QtWidgets.QLabel(self.centralwidget)
        self.d_card_4.setGeometry(QtCore.QRect(240, 10, 101, 141))
        self.d_card_4.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.d_card_4.setText("")
        self.d_card_4.setScaledContents(True)
        self.d_card_4.setObjectName("d_card_4")
        self.d_card_5 = QtWidgets.QLabel(self.centralwidget)
        self.d_card_5.setGeometry(QtCore.QRect(130, 10, 101, 141))
        self.d_card_5.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.d_card_5.setText("")
        self.d_card_5.setScaledContents(True)
        self.d_card_5.setObjectName("d_card_5")
        self.d_card_6 = QtWidgets.QLabel(self.centralwidget)
        self.d_card_6.setGeometry(QtCore.QRect(20, 10, 101, 141))
        self.d_card_6.setStyleSheet("border: 1px solid yellow;\n"
"border-radius: 5px")
        self.d_card_6.setText("")
        self.d_card_6.setScaledContents(True)
        self.d_card_6.setObjectName("d_card_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 160, 81, 31))
        self.label.setStyleSheet("font-size: 20px;\n"
"font-family: Georgia, serif;\n"
"color: white;\n"
"background-image: url(\"\");")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 300, 81, 31))
        self.label_2.setStyleSheet("font-size: 20px;\n"
"font-family: Georgia, serif;\n"
"color: white;\n"
"background-image: url(\"\");")
        self.label_2.setObjectName("label_2")
        self.playerPoints = QtWidgets.QLabel(self.centralwidget)
        self.playerPoints.setGeometry(QtCore.QRect(120, 310, 47, 13))
        self.playerPoints.setStyleSheet("color: white;background-image: url(\"\");")
        self.playerPoints.setText("")
        self.playerPoints.setObjectName("playerPoints")
        self.dealerPoints = QtWidgets.QLabel(self.centralwidget)
        self.dealerPoints.setGeometry(QtCore.QRect(120, 170, 47, 13))
        self.dealerPoints.setStyleSheet("color: white;\n"
"opacity: 0%;background-image: url(\"\");")
        self.dealerPoints.setText("")
        self.dealerPoints.setObjectName("dealerPoints")
        self.moneyLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.moneyLabel.setGeometry(QtCore.QRect(790, 10, 101, 51))
        self.moneyLabel.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.moneyLabel.setStyleSheet("color: white;\n"
"border: 1px solid white;")
        self.moneyLabel.setObjectName("moneyLabel")
        self.betLabel = QtWidgets.QLCDNumber(self.centralwidget)
        self.betLabel.setGeometry(QtCore.QRect(250, 300, 64, 31))
        self.betLabel.setStyleSheet("color: white;")
        self.betLabel.setObjectName("betLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 300, 61, 31))
        self.label_3.setStyleSheet("font-size: 20px;\n"
"font-family: Georgia, serif;\n"
"color: white;background-image: url(\"\");")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(690, 260, 191, 221))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame.setStyleSheet("background-image: url(C:/Users/herme/Desktop/BlackJack UI/assets/images/black.jpg);\n"
"border: 2px outset #5A002C;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hitButton = QtWidgets.QPushButton(self.frame)
        self.hitButton.setEnabled(True)
        self.hitButton.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.hitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hitButton.setStyleSheet("background-color: #008000;\n"
"border-radius: 30px;\n"
"border: 2px solid grey;\n"
"border-style: outset;\n"
"background-image: url(\"\");\n"
"color: white;\n"
"font-size: 14px")
        self.hitButton.setObjectName("hitButton")
        self.standButton = QtWidgets.QPushButton(self.frame)
        self.standButton.setGeometry(QtCore.QRect(10, 80, 61, 61))
        self.standButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.standButton.setStyleSheet("background-color: #880808;\n"
"border-radius: 30px;\n"
"border: 2px solid grey;\n"
"border-style: outset;\n"
"background-image: url(\"\");\n"
"color: white;\n"
"font-size: 14px;")
        self.standButton.setObjectName("standButton")
        self.surrenderButton = QtWidgets.QPushButton(self.frame)
        self.surrenderButton.setGeometry(QtCore.QRect(10, 150, 61, 61))
        self.surrenderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.surrenderButton.setStyleSheet("background-color: blue;\n"
"border-radius: 30px;\n"
"border: 2px solid grey;\n"
"border-style: outset;\n"
"background-image: url(\"\");\n"
"color: white;\n"
"font-size: 14px;")
        self.surrenderButton.setObjectName("surrenderButton")
        self.ddButton = QtWidgets.QPushButton(self.frame)
        self.ddButton.setEnabled(True)
        self.ddButton.setGeometry(QtCore.QRect(120, 10, 61, 61))
        self.ddButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ddButton.setStyleSheet("background-color: black;\n"
"border-radius: 30px;\n"
"border: 2px solid grey;\n"
"border-style: outset;\n"
"background-image: url(\"\");\n"
"color: white;\n"
"font-size: 12px")
        self.ddButton.setObjectName("ddButton")
        self.chip50Button = QtWidgets.QPushButton(self.centralwidget)
        self.chip50Button.setGeometry(QtCore.QRect(300, 190, 91, 81))
        self.chip50Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chip50Button.setAutoFillBackground(False)
        self.chip50Button.setStyleSheet("border-radius: 40px;\n"
"\n"
"border-style: outset;\n"
"border-image: url(:image/images/chip50.png);\n"
"")
        self.chip50Button.setText("")
        self.chip50Button.setObjectName("chip50Button")
        self.chip10Button = QtWidgets.QPushButton(self.centralwidget)
        self.chip10Button.setGeometry(QtCore.QRect(190, 190, 91, 81))
        self.chip10Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chip10Button.setMouseTracking(True)
        self.chip10Button.setAutoFillBackground(False)
        self.chip10Button.setStyleSheet("border-radius: 40px;\n"
"\n"
"border-style: outset;\n"
"border-image: url(:/image/images/chip10.png);\n"
"")
        self.chip10Button.setText("")
        self.chip10Button.setObjectName("chip10Button")
        self.chip100Button = QtWidgets.QPushButton(self.centralwidget)
        self.chip100Button.setGeometry(QtCore.QRect(410, 190, 91, 81))
        self.chip100Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chip100Button.setAutoFillBackground(False)
        self.chip100Button.setStyleSheet("border-radius: 40px;\n"
"border-image: url(:/image/images/chip100.png);\n"
"\n"
"")
        self.chip100Button.setText("")
        self.chip100Button.setObjectName("chip100Button")
        self.betButton = QtWidgets.QPushButton(self.centralwidget)
        self.betButton.setGeometry(QtCore.QRect(530, 210, 91, 41))
        self.betButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.betButton.setStyleSheet("color: white;")
        self.betButton.setObjectName("betButton")
        self.messageBox = QtWidgets.QFrame(self.centralwidget)
        self.messageBox.setEnabled(True)
        self.messageBox.setGeometry(QtCore.QRect(320, 170, 251, 121))
        self.messageBox.setStyleSheet("border: 3px groove grey;\n"
"background-image: url(\"\");\n"
"background-color: green;")
        self.messageBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.messageBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.messageBox.setObjectName("messageBox")
        self.messageLabel = QtWidgets.QLabel(self.messageBox)
        self.messageLabel.setGeometry(QtCore.QRect(30, 20, 181, 41))
        self.messageLabel.setStyleSheet("color: white;\n"
"border: 0px solid white;\n"
"font-size: 20px;\n"
"font-family: Georgia, serif;")
        self.messageLabel.setText("")
        self.messageLabel.setObjectName("messageLabel")
        self.messageButton = QtWidgets.QPushButton(self.messageBox)
        self.messageButton.setGeometry(QtCore.QRect(150, 80, 91, 31))
        self.messageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.messageButton.setStyleSheet("background-color: white;\n"
"background-image: url(\"\");\n"
"border-radius: 10px \n"
"")
        self.messageButton.setObjectName("messageButton")
        self.menuFrame = QtWidgets.QFrame(self.centralwidget)
        self.menuFrame.setEnabled(True)
        self.menuFrame.setGeometry(QtCore.QRect(0, -10, 921, 501))
        self.menuFrame.setStyleSheet("background-image: url(:/image/images/blackjack-menu-background.jpg);")
        self.menuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuFrame.setObjectName("menuFrame")
        self.startButton = QtWidgets.QPushButton(self.menuFrame)
        self.startButton.setGeometry(QtCore.QRect(360, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet("font-size: 25px;\n"
"color: white;\n"
"font-family: Times New Roman;\n"
"font-weight: bold;")
        self.startButton.setObjectName("startButton")
        self.label_4 = QtWidgets.QLabel(self.menuFrame)
        self.label_4.setGeometry(QtCore.QRect(370, 310, 81, 21))
        self.label_4.setStyleSheet("background-image: url(\"\");\n"
"color: white;\n"
"font-family: Times New Roman;\n"
"font-size: 15px;\n"
"font-weight: bold;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.menuFrame)
        self.label_5.setGeometry(QtCore.QRect(280, 0, 351, 191))
        self.label_5.setStyleSheet("background-image: url(\"\");\n"
"border-image: url(:/image/images/blackjack_title.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.moneyInput = QtWidgets.QLineEdit(self.menuFrame)
        self.moneyInput.setGeometry(QtCore.QRect(460, 310, 61, 20))
        self.moneyInput.setStyleSheet("background-image: url(\"\")")
        self.moneyInput.setObjectName("moneyInput")
        self.menuMessage = QtWidgets.QFrame(self.menuFrame)
        self.menuMessage.setEnabled(True)
        self.menuMessage.setGeometry(QtCore.QRect(340, 180, 241, 101))
        self.menuMessage.setStyleSheet("border: 3px groove grey;\n"
"background-image: url(\"\");\n"
"background-color: green;")
        self.menuMessage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menuMessage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuMessage.setObjectName("menuMessage")
        self.menuMessageLabel = QtWidgets.QLabel(self.menuMessage)
        self.menuMessageLabel.setGeometry(QtCore.QRect(10, 20, 211, 41))
        self.menuMessageLabel.setStyleSheet("color: white;\n"
"border: 0px solid white;\n"
"font-size: 15px;\n"
"font-family: Georgia, serif;")
        self.menuMessageLabel.setObjectName("menuMessageLabel")
        self.menuMessageButton = QtWidgets.QPushButton(self.menuMessage)
        self.menuMessageButton.setGeometry(QtCore.QRect(140, 70, 81, 21))
        self.menuMessageButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.menuMessageButton.setStyleSheet("background-color: white;\n"
"background-image: url(\"\");\n"
"border-radius: 10px \n"
"")
        self.menuMessageButton.setObjectName("menuMessageButton")
        self.p_card_1.raise_()
        self.d_card_1.raise_()
        self.p_card_2.raise_()
        self.p_card_3.raise_()
        self.p_card_4.raise_()
        self.p_card_5.raise_()
        self.p_card_6.raise_()
        self.d_card_2.raise_()
        self.d_card_3.raise_()
        self.d_card_4.raise_()
        self.d_card_5.raise_()
        self.d_card_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.playerPoints.raise_()
        self.dealerPoints.raise_()
        self.moneyLabel.raise_()
        self.betLabel.raise_()
        self.label_3.raise_()
        self.chip50Button.raise_()
        self.chip10Button.raise_()
        self.chip100Button.raise_()
        self.betButton.raise_()
        self.messageBox.raise_()
        self.frame.raise_()
        self.menuFrame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Krupiye"))
        self.label_2.setText(_translate("MainWindow", "Oyuncu"))
        self.betLabel.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Bahis:"))
        self.hitButton.setText(_translate("MainWindow", "Kart Çek"))
        self.standButton.setText(_translate("MainWindow", "Kal"))
        self.surrenderButton.setText(_translate("MainWindow", "Teslim Ol"))
        self.ddButton.setText(_translate("MainWindow", "Bahsi İkiye"))
        self.betButton.setText(_translate("MainWindow", "Bahsi Onayla"))
        self.messageButton.setText(_translate("MainWindow", "Devam"))
        self.startButton.setText(_translate("MainWindow", "Başla"))
        self.label_4.setText(_translate("MainWindow", "Kasa Parası:"))
        self.moneyInput.setPlaceholderText(_translate("MainWindow", "Miktar"))
        self.menuMessageLabel.setText(_translate("MainWindow", "Lütfen geçerli bir değer giriniz!"))
        self.menuMessageButton.setText(_translate("MainWindow", "Devam"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
