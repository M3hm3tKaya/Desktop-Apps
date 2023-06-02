from pytube import YouTube
import os
from PyQt5.QtTest import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from YT_mp3Donusturucu_python import Ui_MainWindow

class YoutubeMp3(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.pressed.connect(self.pressed_button)
        self.ui.pushButton.released.connect(self.released_button)

        self.ui.pushButton_2.pressed.connect(self.pressed_button2)
        self.ui.pushButton_2.released.connect(self.released_button2)

    def pressed_button(self):
        self.ui.pushButton.setStyleSheet("background-color: rgb(209, 209, 209);border-radius : 15px;")
    def released_button(self):
        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);border-radius : 15px;")
        text = str(self.ui.lineEdit.text())
        self.ui.pushButton.setText("İndiriliyor...")
        self.ui.pushButton.setEnabled(0)
        QApplication.processEvents()
        try:
            yt = YouTube(text)
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download()
            out_file_name = out_file[:-4]
            new_file = out_file_name + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " Başarıyla Yüklendi.")
            self.ui.statusbar.setStyleSheet("color:rgb(0,230,0);")
            self.ui.statusbar.showMessage(yt.title + " Başarıyla Yüklendi.",2000)

        except:
            self.ui.statusbar.setStyleSheet("color:rgb(200,0,0);")
            self.ui.statusbar.showMessage("Hata Oluştu Lütfen linki kontrol edin.ya da videou 2. defa indirmeye çalışıyor olabilirsiniz",5000)
        self.ui.pushButton.setText("Dönüştür")
        self.ui.pushButton.setEnabled(1)

    def pressed_button2(self):
        self.ui.pushButton.setStyleSheet("background-color: rgb(209, 209, 209);border-radius : 15px;")
    def released_button2(self):
        self.ui.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);border-radius : 15px;")
        text = str(self.ui.lineEdit.text())
        self.ui.pushButton.setText("İndiriliyor...")
        self.ui.pushButton.setEnabled(0)

        self.ui.pushButton_2.setText("İndiriliyor...")
        self.ui.pushButton_2.setEnabled(0)

        QApplication.processEvents()
        try:
            yt = YouTube(text)
            video = yt.streams.filter(res="720p").first()
            out_file = video.download()
            out_file_name = out_file[:-4]
            new_file = out_file_name + '.mp3'
            os.rename(out_file, new_file)
            print(yt.title + " Başarıyla Yüklendi.")
            self.ui.statusbar.setStyleSheet("color:rgb(0,230,0);")
            self.ui.statusbar.showMessage(yt.title + " Başarıyla Yüklendi.",2000)

        except:
            self.ui.statusbar.setStyleSheet("color:rgb(200,0,0);")
            self.ui.statusbar.showMessage("Hata Oluştu Lütfen linki kontrol edin.ya da videou 2. defa indirmeye çalışıyor olabilirsiniz",5000)
        self.ui.pushButton.setText("Dönüştür")
        self.ui.pushButton.setEnabled(1)

        self.ui.pushButton_2.setText("Dönüştür")
        self.ui.pushButton_2.setEnabled(1)



uygulama = QApplication([])
pencere = YoutubeMp3()
pencere.show()
uygulama.exec()