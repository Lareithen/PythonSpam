import os
import sys
import pyautogui
import time
import pyperclip
from PyQt5 import QtWidgets, QtGui

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.menubar = QtWidgets.QMenuBar()
        self.menu = self.menubar.addMenu("Menü")

        self.yazi = QtWidgets.QLabel("Spamlanacak mesajı gir")
        self.sec = QtWidgets.QPushButton("veya dosyalardan seç")
        self.mesaj = QtWidgets.QTextEdit()
        self.yazi2 = QtWidgets.QLabel("Tekrar:") 
        self.tekrar = QtWidgets.QSpinBox()
        self.tekrar.setMaximum(2147483647)
        self.yazi3 = QtWidgets.QLabel("Aralık:") 
        self.aralik = QtWidgets.QSpinBox()
        self.yazi4 = QtWidgets.QLabel("Zaman Aşımı:") 
        self.zaman_asimi = QtWidgets.QSpinBox()
        self.buton = QtWidgets.QPushButton("Başlat")
        self.yazi5 = QtWidgets.QLabel("Varsayılan ayarlar için süre ile zaman aşımını 0 olarak bırakınız!")
        self.yazi5.setStyleSheet("color:#0073ff")

        vb = QtWidgets.QVBoxLayout()

        hbb = QtWidgets.QHBoxLayout()
        hbb.addWidget(self.yazi)
        hbb.addWidget(self.sec)
        vb.addLayout(hbb)

        vvb = QtWidgets.QVBoxLayout()
        vvb.addWidget(self.mesaj)
        vb.addLayout(vvb)

        hb = QtWidgets.QHBoxLayout()
        hb.addWidget(self.yazi2)
        hb.addWidget(self.tekrar)
        hb.addWidget(self.yazi3)
        hb.addWidget(self.aralik)
        hb.addWidget(self.yazi4)
        hb.addWidget(self.zaman_asimi)
        vb.addLayout(hb)

        vb2 = QtWidgets.QVBoxLayout()
        vb2.addWidget(self.buton)
        vb2.addWidget(self.yazi5)
        vb.addLayout(vb2)

        self.setLayout(vb)
        self.show()

        self.buton.clicked.connect(self.baslat)
        self.sec.clicked.connect(self.secme)

    def baslat(self):
        time.sleep(self.zaman_asimi.value())
        yazi = self.mesaj.toPlainText()
        self.sayi = 0
        if yazi == "":
            QtWidgets.QMessageBox.critical(self, "Hata", "Spam işlemi başarısız, spamlanacak bir yazı yok!")
        else:
            if self.tekrar.value() == 0:
                time.sleep(self.zaman_asimi.value())
                while True:
                    time.sleep(self.aralik.value())
                    pyperclip.copy(yazi)
                    pyautogui.hotkey("ctrl", "v")
                    pyautogui.press("enter")
            else:
                time.sleep(self.zaman_asimi.value())
                while self.sayi < self.tekrar.value():
                    time.sleep(self.aralik.value())
                    pyperclip.copy(yazi)
                    pyautogui.hotkey("ctrl", "v")
                    pyautogui.press("enter")
                    self.sayi+=1

    def secme(self):
        secme_seysi = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Seç", os.getenv("Desktop"), filter="(*.txt)")
        with open(secme_seysi[0], "r", encoding="utf-8") as file:
            self.mesaj.setText(file.read())

obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("by Larei v2.0")
pencere.setFixedSize(320,300)
sys.exit(obje.exec())

# larei was here
