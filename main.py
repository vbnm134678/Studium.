import sys
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic

import multiprocessing
import Drowsiness_Detection
import Sticker

form_class = uic.loadUiType("Main.ui")[0]
t = 0


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start.clicked.connect(self.bf1)
        self.myinfo.clicked.connect(self.bf2)
        self.mission.clicked.connect(self.bf3)
        self.setting.clicked.connect(self.bf4)

    def bf1(self):
        Drowsiness_Detection.detect(0)
        #Sticker.main_s(0) -> 이건 아마 ui넘어가는 거로 시도해보면 해결가능할수도.

    def bf2(self):
        print("bt2")

    def bf3(self):
        print("bt3")

    def bf4(self):
        print("bt4")


if __name__ == "__main__":
    app =QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()