import random
import time
from PyQt5.QtTest import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from valorant_choice_python  import Ui_MainWindow


valorantSkins ={
    "Şampiyon Vandal" : ":/icons/icons/v1.png",
    "Zamanın Ötesi Vandal" : ":/icons/icons/v2.png",
    "Ejder Ateşi Vandal" : ":/icons/icons/v3.png",
    "Gaia'nın İntikamı Vandal" : ":/icons/icons/v4.png",
    "İyon Vandal" : ":/icons/icons/v5.png",
    "Asil Vandal" : ":/icons/icons/v6.png",
    "Yağmacı Vandal" : ":/icons/icons/v7.png",
    "RGX 11z Pro Vandal" : ":/icons/icons/v8.png",
    "Işık Muhafızları Vandal" : ":/icons/icons/v9.png"
}

class Valorant(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.pressed.connect(self.pressed_button)
        self.ui.pushButton.released.connect(self.released_button)

    def pressed_button(self):
        self.ui.pushButton.setStyleSheet("background-color: rgb(209, 209, 209);border-radius : 10px;")
    def released_button(self):
        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);border-radius : 10px;")
        self.ui.pushButton.setEnabled(0)
        skinName = ""
        zaman = 0.01
        sayac = 0
        self.ui.label.setText("SEÇİLİYOR")
        while zaman < 1:
            skinName = random.choice(list(valorantSkins.keys()))
            skinUrl = valorantSkins[skinName]
            self.ui.frame.setStyleSheet(
                f"image:url({skinUrl});background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 180), stop:1 rgba(255, 255, 255, 255));border-radius : 20px")

            QTest.qWait(int(zaman * 1000))
            sayac += 1
            QApplication.processEvents()
            if sayac > 3:
                sayac = 0
                zaman *= 1.5

        self.ui.label.setText(skinName)
        self.ui.pushButton.setEnabled(1)

uygulama = QApplication([])
pencere = Valorant()
pencere.show()
uygulama.exec()