import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
import Drowsiness_Detection
from Sticker import Sticker
condition = 0
form_class = uic.loadUiType("timer.ui")[0]


class Timer(QDialog, QWidget, form_class):
    def __init__(self):
        super(Timer,self).__init__()
        self.initUI()
        self.show()
        condition = Drowsiness_Detection.detect()
        if condition == 1:
            self.stickers()
    def initUI(self):
        self.setupUi(self)
        self.toolButton_4.clicked.connect(self.back)

    def back(self):
        self.close()

    def stickers(self):
        image_x = random.randrange(0, 1800)
        image_y = random.randrange(0, 950)
        self.sticker = Sticker('gif/monster.png', xy=[image_x, image_y], size=2.0, on_top=True)
        self.exec()

