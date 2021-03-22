import os
import sys
import pyautogui, time
from PyQt5 import QtWidgets, QtGui

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi = QtWidgets.QLabel("Spamlanacak mesajı gir")
        self.sec = QtWidgets.QPushButton("veya dosyalardan seç")
        self.mesaj = QtWidgets.QTextEdit()
        self.yazi2 = QtWidgets.QLabel("Süre:") 
        self.sure = QtWidgets.QSpinBox()
        self.yazi3 = QtWidgets.QLabel("Zaman Aşımı:") 
        self.zaman_asimi = QtWidgets.QSpinBox()
        self.buton = QtWidgets.QPushButton("Başlat")
        self.yazi4 = QtWidgets.QLabel("Varsayılan ayarlar için süre ile zaman aşımını 0 olarak bırakınız!")
        self.yazi4.setStyleSheet("color:#0073ff")

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
        hb.addWidget(self.sure)
        hb.addWidget(self.yazi3)
        hb.addWidget(self.zaman_asimi)
        vb.addLayout(hb)

        vb2 = QtWidgets.QVBoxLayout()
        vb2.addWidget(self.buton)
        vb2.addWidget(self.yazi4)
        vb.addLayout(vb2)

        self.setLayout(vb)
        self.show()

        self.buton.clicked.connect(self.baslat)
        self.sec.clicked.connect(self.secme)

    def baslat(self):
        time.sleep(self.zaman_asimi.value())
        dosya = self.mesaj.toPlainText()
        if dosya == "":
            self.yazi4.setText("Mesaj girilimedi!")
            self.yazi4.setStyleSheet("color:red")
        else:
            self.yazi4.deleteLater()
            for i in dosya:
                i = dosya
                while i == dosya:
                    time.sleep(self.sure.value())
                    pyautogui.typewrite(i)
                    pyautogui.press("enter")

    def secme(self):
        secme_seysi = QtWidgets.QFileDialog.getOpenFileName(self, "Dosya Seç", os.getenv("Desktop"))
        with open(secme_seysi[0], "r", encoding="utf-8") as file:
            self.mesaj.setText(file.read())

obje = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("by Larei")
pencere.setFixedSize(315,230)
sys.exit(obje.exec())

# larei was here
