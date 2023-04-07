#!/usr/bin/env python3

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon
import json

class GuiThItem(QtWidgets.QWidget):

    def __init__(self, item):
        super(GuiThItem, self).__init__()
        self.gui_win = loadUi('design/recth_item.ui', self)

        data=item.split(';')

        self.gui_win.name.setStyleSheet("QLabel{ background:transparent; color:#ffffff; font-family:Bahnschrift SemiBold; font-size:18px; }")
        self.gui_win.name.setText(data[0])

        if int(data[1]) > 7:
            self.gui_win.score.setStyleSheet("QLabel{background:transparent; color:#eb6134; font-family:Bahnschrift SemiBold; font-weight:bold; font-size:20px;}")
        else:
            self.gui_win.score.setStyleSheet("QLabel{background:transparent; color:#80eb34; font-family:Bahnschrift SemiBold; font-weight:bold; font-size:20px;}")
        self.gui_win.score.setText(data[1]+"/12")

        _vector = "Sc:"+data[2]+"; Pc:"+data[3]+"; Ex:"+data[4]+"; Pt:"+data[5]+"; Tt:"+data[6]+"; Ui:"+data[7]+"; Va:"+data[8]+"; Ia:"+data[9]+"; Dw:"+data[10]
        self.gui_win.lb_vector.setText(_vector)
