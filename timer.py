from PyQt5.QtWidgets import *
from PyQt5 import uic
import Drowsiness_Detection
from Sticker import Sticker

import time
import winsound as sd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
# firebase
db_url = 'https://studium-28d4b-default-rtdb.firebaseio.com/'
cred = credentials.Certificate('studium-28d4b-firebase-adminsdk-94egj-795b3ae3e7.json')
default_app = firebase_admin.initialize_app(cred, {'databaseURL' : db_url})

# 데이터 update
ref = db.reference('test')

form_class = uic.loadUiType("Timer.ui")[0]
# Timer ui
class Timer(QDialog, QWidget, form_class):
    def __init__(self):
        super(Timer,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)
        self.RestartButton.clicked.connect(self.restart)
        self.PauseButton.clicked.connect(self.stop)
        self.BackButton.clicked.connect(self.back)

    def start(self):
        condition = Drowsiness_Detection.detect()
        if condition == 1:
            self.stickers()

    def restart(self):
        print("bt")

    def stop(self):
        ref.update({'check' : 0})

    def back(self):
        self.close()

    def stickers(self):
        beepsound()
        self.sticker = Sticker('gif/move.gif', size=0.5, on_top=True)

def beepsound():
    fr = 2000
    du = 1000
    sd.Beep(fr, du)

def time_check(i):
    playtime = i
    print("playtime : %2f" %playtime)
    if playtime > 10 :
        beepsound()
    condition = Drowsiness_Detection.detect()
    if condition == 1:
        beepsound()


