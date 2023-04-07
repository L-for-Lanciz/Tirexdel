#!/usr/bin/env python3

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi
from PyQt6.QtGui import QIcon

class GuiRvItem(QtWidgets.QWidget):

    def __init__(self, item):
        super(GuiRvItem, self).__init__()
        self.gui_win = loadUi('design/recvw_item.ui', self)
        self.gui_win.fvt.setStyleSheet("QToolButton{ background:transparent; image:url(images/vt); }")
        self.gui_win.fabid.setStyleSheet("QToolButton{ background:transparent; image:url(images/abid); }")
        self.gui_win.fmtdf.setStyleSheet("QToolButton{ background:transparent; image:url(images/meta); }")
        self.gui_win.fibm.setStyleSheet("QToolButton{ background:transparent;  image:url(images/ibm); }")
        self.gui_win.fvtc.setStyleSheet("QToolButton{ background:transparent; image:url(images/vtc); }")
        self.gui_win.fpd.setStyleSheet("QToolButton{ background:transparent; image:url(images/pd); }")
        self.gui_win.fgn.setStyleSheet("QToolButton{ background:transparent; image:url(images/gn); }")
        self.gui_win.fotx.setStyleSheet("QToolButton{ background:transparent; image:url(images/otx); }")
        self.gui_win.fshd.setStyleSheet("QToolButton{ background:transparent; image:url(images/shd); }")
        data = item
        try:
            txd_splitted = data[5].split('[')
            scored = txd_splitted[1].replace(']','')
            score = float(scored.replace('%',''))
        except:
            txd_splitted = 0
            scored = 0
            score = 0
        if score > 75 :
            self.gui_win.widget.setStyleSheet("QWidget{ background:rgba(118, 0, 0, 100); color:white; }")
        elif score > 50 :
            self.gui_win.widget.setStyleSheet("QWidget{ background:rgba(255, 0, 0, 100); color:white; }")
        elif score > 20 :
            self.gui_win.widget.setStyleSheet("QWidget{ background:rgba(255, 170, 0, 100); color:white; }")
        elif score > 0 :
            self.gui_win.widget.setStyleSheet("QWidget{ background:rgba(255, 255, 0, 100); color:white; }")
        elif score == 0 :
            self.gui_win.widget.setStyleSheet("QWidget{ background:rgba(76, 255, 0, 100); color:white; }")
        self.gui_win.ip.setText(data[0])
        self.gui_win.cn.setText(data[1])
        self.gui_win.isp.setText(data[3])
        self.gui_win.use.setText(data[4])
        self.gui_win.score.setText((data[5]).upper())
        self.gui_win.vt.setText(data[7])
        self.gui_win.abid.setText(data[6])
        self.gui_win.mtdf.setText(data[9])
        self.gui_win.ibm.setText(data[8])
        self.gui_win.gn.setText(data[10])
        self.gui_win.pd.setText(data[11])
        self.gui_win.vtc.setText(data[12])
        self.gui_win.url.setText(data[15])
        self.gui_win.sop.setText(data[13])
        self.gui_win.csb.setText(data[14])
