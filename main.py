import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic
from timer import Timer
from Info import Info
import multiprocessing
import Drowsiness_Detection
import Sticker

form_class = uic.loadUiType("Main.ui")[0]
t = 0


class MainWindow(QMainWindow, QWidget, form_class):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.toolButton.clicked.connect(self.bf1)
        self.toolButton_2.clicked.connect(self.bf2)
        self.toolButton_3.clicked.connect(self.bf3)
        self.toolButton_4.clicked.connect(self.bf4)
    def bf1(self):
        self.hide()
        self.timer=Timer()
        self.timer.exec()
        self.show()
        # Drowsiness_Detection.detect(0)
        #Sticker.main_s(0) -> 이건 아마 ui넘어가는 거로 시도해보면 해결가능할수도.

    def bf2(self):
        print("bt2")

    def bf3(self):
        self.hide()
        self.Info = Info()
        self.Info.exec()
        self.show()

    def bf4(self):
        print("bt4")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    sys.exit(app.exec_())