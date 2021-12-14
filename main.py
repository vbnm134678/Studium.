import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

from Timer import Timer
from Info import Info
from Quest import Quest
form_class = uic.loadUiType("Main.ui")[0]

# Main ui
class MainWindow(QMainWindow, QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()


    def initUI(self):
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)
        self.GoalButton.clicked.connect(self.goal)
        self.InfoButton.clicked.connect(self.info)
        self.OptionButton.clicked.connect(self.option)

    def start(self):
        self.hide()
        self.Timer=Timer()
        self.Timer.exec()
        self.show()

    def goal(self):
        self.hide()
        self.Quest = Quest()
        self.Quest.exec()
        self.show()

    def info(self):
        self.hide()
        self.Info = Info()
        self.Info.exec()
        self.show()

    def option(self):
        print("bt4")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    myWindow = MainWindow()
    sys.exit(app.exec_())
