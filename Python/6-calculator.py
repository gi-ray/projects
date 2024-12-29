from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()

    def initUI(self):
        label = QtWidgets.Qlabel(self)
        label.setText("My First Label")
        label.move(50,50)

        b_add = QtWidgets.QPushButton(self)
        b_add.setText("+")
        b_add.clicked.connect(addition)

def addition(self):
    


def window():
    app= QApplication(sys.argv)
    win =

