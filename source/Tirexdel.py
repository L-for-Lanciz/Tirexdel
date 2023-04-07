#!/usr/bin/env python3

import sys
from configparser import ConfigParser

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QGuiApplication, QIcon, QFont, QMovie
from PyQt6.QtCore import QTimeLine

import src.gui.gui_ipaddr as g_ip
import src.gui.gui_ipaddr_newl as g_ipnl
import src.gui.gui_troppip as g_tip
import src.gui.gui_domurl as g_du
import src.gui.gui_hash as g_hs
import src.menup.menu_sett as g_ms
import src.menup.credits as creds
import src.gui_mores.triage as trge

class MainUi(QtWidgets.QMainWindow):
    guidomurl = None
    guihash = None

    def __init__(self):
        super(MainUi, self).__init__()
        gui_main = loadUi('design/main2.ui', self)
        gui_main.lb_titlem.setStyleSheet("QLabel{ background: transparent; color: white; text-align: left; font-family:Impact; font-size:40px; }")
        gui_main.maimwidget.setStyleSheet("QWidget{ background-color:#463595}")
        gui_main.bt_to_ip.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_url.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_hsh.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_men.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_trg.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_scan.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_tip.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:19px; }""QToolButton:hover{font-size:20px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_cred.setStyleSheet("QToolButton{ background: transparent; color: white; font-family:Bahnschrift SemiBold SemiConden; font-size:15px; }""QToolButton:hover{font-size:16px; color:#6aa0de; font-weight:bold;}")
        gui_main.bt_to_ip.clicked.connect(self.open_Gui_Ipaddr)
        gui_main.bt_to_url.clicked.connect(self.open_Gui_Domurl)
        gui_main.bt_to_hsh.clicked.connect(self.open_Gui_Hash)
        gui_main.bt_to_men.clicked.connect(self.open_Gui_Menu)
        gui_main.bt_to_trg.clicked.connect(self.open_Gui_Triage)
        gui_main.bt_to_tip.clicked.connect(self.open_Gui_Troppip)
        gui_main.bt_to_cred.clicked.connect(self.open_Gui_Creds)
        movie = QMovie("images/gif_mmenu.gif")
        gui_main.gif_back.setMovie(movie)
        movie.start()
        gui_main.gif_top.setStyleSheet("QFrame{ background:transparent; image:url(images/dino_back.png); }")

    def open_Gui_Ipaddr(self):
        guiipaddr.tunnelWidget(widget)
        widget.setCurrentIndex(1)
    def open_Gui_Domurl(self):
        guidomurl.tunnelWidget(widget)
        widget.setCurrentIndex(2)
    def open_Gui_Hash(self):
        guihash.tunnelWidget(widget)
        widget.setCurrentIndex(3)
    def open_Gui_Menu(self):
        guimenu = g_ms.GuiSettings()
        widget.addWidget(guimenu)
        guimenu.tunnelWidget(widget, guimenu)
        widget.setCurrentIndex(4)
    def open_Gui_Troppip(self):
        guitip = g_tip.GuiTipadr()
        widget.addWidget(guitip)
        guitip.tunnelWidget(widget, guitip)
        widget.setCurrentIndex(4)
    def open_Gui_Triage(self):
        guitrg = trge.Triage()
        widget.addWidget(guitrg)
        guitrg.tunnelWidget(widget, guitrg)
        widget.setCurrentIndex(4)
    def open_Gui_Creds(self):
        self.dialog = QtWidgets.QDialog()
        self.dialog = uic.loadUi('design/credits.ui')
        self.dialog.setWindowTitle("Credits")
        self.dialog.setWindowIcon(QIcon('images/auicon.ico'))
        self.dialog.setFixedSize(700, 438)
        self.ui = creds.Credits()
        self.ui.creator(self.dialog)
        self.dialog.setModal(True)
        self.dialog.show()

#instance
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainWindow = MainUi()
widget.addWidget(mainWindow)
#show
widget.show()
#load guis
cfg = ConfigParser()
cfg.read('config/config.ini')
repxdbll_state = cfg.get('settings', 'ip_layout')
if repxdbll_state == "NEW":
    guiipaddr = g_ipnl.GuiIpAddrNewl()
else:
    guiipaddr = g_ip.GuiIpAddr()
widget.addWidget(guiipaddr)
guidomurl = g_du.GuiUrl()
widget.addWidget(guidomurl)
guihash = g_hs.GuiHash()
widget.addWidget(guihash)
#style
widget.setWindowTitle("Tirexdel 2.8")
widget.setWindowIcon(QIcon('images/auicon.ico'))
widget.resize(1300, 850)
widget.setMinimumSize(1000, 600)

#execute
try:
    sys.exit(app.exec())
except:
    print("Exiting.")
