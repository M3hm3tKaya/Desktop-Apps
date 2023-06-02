from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from TheGift_python import Ui_MainWindow

class TheGift(QMainWindow):
    def __init__(self):
        super().__init__()
        file = open("gunluk/gunluk_sayfa_1.txt", "r",encoding='utf-8')
        self.tum_metinler = file.read()
        file.close()

        print(self.tum_metinler)

        self.sayfalar = self.tum_metinler.split(";~;¨")
        self.sayfa_sayisi = len(self.sayfalar)
        print(self.sayfalar)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.TemaChange(0)

        self.mevcut_sayfa = 0
        self.ui.label.setText(f"{self.mevcut_sayfa+1} / {self.sayfa_sayisi}")

        self.sayfa_yazisi = self.sayfalar[self.mevcut_sayfa]

        print(self.sayfa_yazisi)
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setText(self.sayfa_yazisi)

        self.ui.actionKaydet.triggered.connect(self.kaydet)
        self.ui.actionDuzenle.triggered.connect(self.duzenle)

        self.ui.pushButton_previous.pressed.connect(self.previousPressed)
        self.ui.pushButton_previous.released.connect(self.previousReleased)

        self.ui.pushButton_next.pressed.connect(self.nextPressed)
        self.ui.pushButton_next.released.connect(self.nextReleased)

        self.ui.textEdit.textChanged.connect(self.uzunlukKontrol)

        self.ui.actionNormal.triggered.connect(lambda : self.TemaChange(0))
        #self.ui.actionKaranlik.triggered.connect(lambda : self.TemaChange(1))

        if self.mevcut_sayfa >= self.sayfa_sayisi:
            self.ui.pushButton_next.setEnabled(False)
        else:
            self.ui.pushButton_next.setEnabled(True)

        if self.mevcut_sayfa <= 0:
            self.ui.pushButton_previous.setEnabled(False)
        else:
            self.ui.pushButton_previous.setEnabled(True)

    def TemaChange(self,TemaNumarasi):
        file = open("gunluk/gunluk_ayarları.txt","r",encoding="utf-8")
        ayarlar = file.read()
        temalar = ayarlar.split("**tema_ayrimi**")
        tema , icons = temalar[TemaNumarasi].split("**icon_ayrimi**")[0] , temalar[TemaNumarasi].split("**icon_ayrimi**")[1]
        button_tema_baslangic = tema.find("#pushButton_next")
        button_tema_bitis = tema[button_tema_baslangic:].find("}")
        button_tema_bitis += button_tema_baslangic+1
        print(button_tema_baslangic," ",button_tema_bitis)
        self.button_tema_next = tema[button_tema_baslangic:button_tema_bitis]
        print(self.button_tema_next)

        button_tema_baslangic = tema.find("#pushButton_previous")
        button_tema_bitis = tema[button_tema_baslangic:].find("}")
        button_tema_bitis += button_tema_baslangic + 1
        print(button_tema_baslangic, " ", button_tema_bitis)
        self.button_tema_previous = tema[button_tema_baslangic:button_tema_bitis]
        print(self.button_tema_previous)

        icons = icons.split("\n")
        icons.pop(0)
        self.setStyleSheet(tema)

        self.ui.actionKaydet.setIcon(QIcon(icons[0]))
        self.ui.actionDuzenle.setIcon(QIcon(icons[1]))

    def getSayfalar(self):
        file = open("gunluk/gunluk_sayfa_1.txt", "r", encoding='utf-8')
        self.tum_metinler = file.read()
        file.close()
        self.sayfalar = self.tum_metinler.split(";~;¨")
        self.sayfa_sayisi = len(self.sayfalar)

    def previousPressed(self):
        button_rgb_1 = self.button_tema_previous.find("rgb(")
        print(button_rgb_1)
        button_rgb_2 = self.button_tema_previous[button_rgb_1:].find(")") + button_rgb_1
        print(button_rgb_2)
        self.button_rgb_pre = self.button_tema_previous[button_rgb_1+4:button_rgb_2].split(", ")
        print(self.button_rgb_pre)
        self.ui.pushButton_previous.setStyleSheet(f"background-color: rgb({int(self.button_rgb_pre[0])-50}, {int(self.button_rgb_pre[1])-50}, {int(self.button_rgb_pre[2])-50});border-radius : 20px;")
    def previousReleased(self):
        self.ui.pushButton_previous.setStyleSheet(f"background-color: rgb({self.button_rgb_pre[0]}, {self.button_rgb_pre[1]}, {self.button_rgb_pre[2]});border-radius : 20px;")
        self.kaydet()
        self.mevcut_sayfa -= 1
        self.getSayfalar()
        # print(self.sayfa_sayisi)
        # print(self.mevcut_sayfa)

        self.sayfa_yazisi = self.sayfalar[self.mevcut_sayfa]
        self.ui.textEdit.setText(self.sayfa_yazisi)
        self.ui.label.setText(f"{self.mevcut_sayfa + 1} / {self.sayfa_sayisi}")

        self.kontrolSonraki()
        self.kontrolOnceki()

    def nextPressed(self):
        button_rgb_1 = self.button_tema_previous.find("rgb(")
        print(button_rgb_1)
        button_rgb_2 = self.button_tema_previous[button_rgb_1:].find(")") + button_rgb_1
        print(button_rgb_2)
        self.button_rgb_next = self.button_tema_previous[button_rgb_1 + 4:button_rgb_2].split(", ")
        print(self.button_rgb_next)
        self.ui.pushButton_next.setStyleSheet(f"background-color: rgb({int(self.button_rgb_next[0])-50}, {int(self.button_rgb_next[1])-50}, {int(self.button_rgb_next[2])-50});border-radius : 20px;")
    def nextReleased(self):
        self.ui.pushButton_next.setStyleSheet(f"background-color: rgb({self.button_rgb_next[0]}, {self.button_rgb_next[1]}, {self.button_rgb_next[2]});border-radius : 20px;")

        self.kaydet()
        self.mevcut_sayfa += 1
        self.getSayfalar()
        # print(self.sayfa_sayisi)
        # print(self.mevcut_sayfa)

        self.sayfa_yazisi = self.sayfalar[self.mevcut_sayfa]
        self.ui.textEdit.setText(self.sayfa_yazisi)
        self.ui.label.setText(f"{self.mevcut_sayfa+1} / {self.sayfa_sayisi}")

        self.kontrolSonraki()
        self.kontrolOnceki()

    def kontrolSonraki(self):
        if self.mevcut_sayfa + 1 >= self.sayfa_sayisi:
            self.ui.pushButton_next.setEnabled(False)
        else:
            self.ui.pushButton_next.setEnabled(True)
    def kontrolOnceki(self):
        if self.mevcut_sayfa <= 0:
            self.ui.pushButton_previous.setEnabled(False)
        else:
            self.ui.pushButton_previous.setEnabled(True)
    def uzunlukKontrol(self):
        metin = self.ui.textEdit.toPlainText()
        l = len(metin)
        n = metin.count("\n")
        #print(f"karakter : {l}      yeni satır : {n}")

    def kaydet(self):
        metin = self.ui.textEdit.toPlainText()
        self.sayfalar[self.mevcut_sayfa] = metin
        print(self.sayfalar)
        toFileText = ""
        if self.sayfalar[-1] == "":
            for x in self.sayfalar[:-1]:
                print(x)
                toFileText += f"{x};~;¨"
        else:
            for x in self.sayfalar:
                print(x)
                toFileText += f"{x};~;¨"
        file = open("gunluk/gunluk_sayfa_1.txt","w",encoding="utf-8")
        file.write(toFileText)
        file.close()
        self.ui.textEdit.setReadOnly(True)
        self.ui.textEdit.setPlaceholderText("Düzenlemek için 'Düzenle'ye basın")

        self.getSayfalar()
        self.ui.label.setText(f"{self.mevcut_sayfa + 1} / {self.sayfa_sayisi}")

        self.kontrolOnceki()
        self.kontrolSonraki()
        self.ui.statusbar.setStyleSheet("color : rgb(50,200,50)")
        self.ui.statusbar.showMessage(f"Sayfa {self.mevcut_sayfa+1} Kayıt Edildi .",2000)

    def duzenle(self):
        self.ui.textEdit.setReadOnly(False)
        self.ui.statusbar.setStyleSheet("color : rgb(50,50,200)")
        self.ui.statusbar.showMessage(f"Düzenleme Modu Açık.", 2000)
uygulama = QApplication([])
pencere = TheGift()
pencere.show()
uygulama.exec()