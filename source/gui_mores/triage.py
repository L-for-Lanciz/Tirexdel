#!/usr/bin/env python3

from PyQt6 import QtWidgets, QtCore
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QVBoxLayout

import json
import os

import src.gui_mores.gui_trghist_item as th_item

class Triage(QtWidgets.QMainWindow):
    gui_trg = None
    widget = None
    menu_wg = None
    r1Count = 9
    r2Count = 9
    r3Count = 9
    r4Count = 9
    r5Count = 9
    r6Count = 9
    r7Count = 9
    r8Count = 9
    r9Count = 9
    totalCount = 0
    vbox = QVBoxLayout()

    def __init__(self):
        #load gui
        super(Triage, self).__init__()
        self.gui_trg = loadUi('design/triage.ui', self)
        #stylesheet
        self.gui_trg.triagewidget.setStyleSheet("QWidget{ background-color:#463595}")
        self.gui_trg.home_butt.setStyleSheet("QToolButton{ image: url(images/home.png); background:transparent; }""QToolButton:hover{image: url(images/home_hover);}")
        self.gui_trg.home_butt.clicked.connect(self.onHomeClicked)
        self.gui_trg.bt_save.clicked.connect(self.onClickSave)
        self.gui_trg.bt_saveandreset.clicked.connect(self.onSaveNReset)
        self.gui_trg.bt_reset.clicked.connect(self.onClickReset)
        self.gui_trg.bt_save.setStyleSheet("QToolButton{ border:1px solid #fff; background: transparent; color: white; font-weight: bold;}""QToolButton:hover{border:1px solid #6aa0de; color:#6aa0de;}")
        self.gui_trg.bt_saveandreset.setStyleSheet("QToolButton{ border:1px solid #fff; background: transparent; color: white; font-weight: bold;}""QToolButton:hover{border:1px solid #6aa0de; color:#6aa0de;}")
        self.gui_trg.bt_reset.setStyleSheet("QToolButton{ border:1px solid #fff; background: transparent; color: white; font-weight: bold;}""QToolButton:hover{border:1px solid #6aa0de; color:#6aa0de;}")
        self.gui_trg.scrollAreaWidgetContents.setLayout(self.vbox)
        self.setStyleSheets()
        self.clearLayout(self.vbox)
        self.setHistory()

        self.gui_trg.r11.mousePressEvent=(lambda case: self.OnClickR1(1))
        self.gui_trg.r12.mousePressEvent=(lambda case: self.OnClickR1(2))
        self.gui_trg.r13.mousePressEvent=(lambda case: self.OnClickR1(3))
        self.gui_trg.r14.mousePressEvent=(lambda case: self.OnClickR1(4))

        self.gui_trg.r21.mousePressEvent=(lambda case: self.OnClickR2(1))
        self.gui_trg.r22.mousePressEvent=(lambda case: self.OnClickR2(2))

        self.gui_trg.r31.mousePressEvent=(lambda case: self.OnClickR3(1))
        self.gui_trg.r32.mousePressEvent=(lambda case: self.OnClickR3(2))

        self.gui_trg.r41.mousePressEvent=(lambda case: self.OnClickR4(1))
        self.gui_trg.r42.mousePressEvent=(lambda case: self.OnClickR4(2))
        self.gui_trg.r43.mousePressEvent=(lambda case: self.OnClickR4(3))

        self.gui_trg.r51.mousePressEvent=(lambda case: self.OnClickR5(1))
        self.gui_trg.r52.mousePressEvent=(lambda case: self.OnClickR5(2))

        self.gui_trg.r61.mousePressEvent=(lambda case: self.OnClickR6(1))
        self.gui_trg.r62.mousePressEvent=(lambda case: self.OnClickR6(2))

        self.gui_trg.r71.mousePressEvent=(lambda case: self.OnClickR7(1))
        self.gui_trg.r72.mousePressEvent=(lambda case: self.OnClickR7(2))

        self.gui_trg.r81.mousePressEvent=(lambda case: self.OnClickR8(1))
        self.gui_trg.r82.mousePressEvent=(lambda case: self.OnClickR8(2))

        self.gui_trg.r91.mousePressEvent=(lambda case: self.OnClickR9(1))
        self.gui_trg.r92.mousePressEvent=(lambda case: self.OnClickR9(2))


    def setHistory(self):
        # Opening file
        with open('config/triages.history', 'r') as histf:
            # returns object
            data = histf.readlines()
            # Iterating through the list
            for matrix in data:
                self.vbox.addWidget(th_item.GuiThItem(matrix))

    def OnClickR1(self, case):
        if case == 1:
            self.r1Count = 0
            self.setTheTotalCount()
            self.gui_trg.r11.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r12.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r13.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r14.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r1Count = 1
            self.setTheTotalCount()
            self.gui_trg.r11.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r12.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r13.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r14.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 3:
            self.r1Count = 2
            self.setTheTotalCount()
            self.gui_trg.r11.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r12.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r13.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r14.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 4:
            self.r1Count = 3
            self.setTheTotalCount()
            self.gui_trg.r11.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r12.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r13.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r14.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR2(self, case):
        if case == 1:
            self.r2Count = 0
            self.setTheTotalCount()
            self.gui_trg.r21.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r22.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r2Count = 1
            self.setTheTotalCount()
            self.gui_trg.r21.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r22.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR3(self, case):
        if case == 1:
            self.r3Count = 0
            self.setTheTotalCount()
            self.gui_trg.r31.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r32.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r3Count = 1
            self.setTheTotalCount()
            self.gui_trg.r31.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r32.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR4(self, case):
        if case == 1:
            self.r4Count = 0
            self.setTheTotalCount()
            self.gui_trg.r41.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r42.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r43.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r4Count = 1
            self.setTheTotalCount()
            self.gui_trg.r41.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r42.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r43.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 3:
            self.r4Count = 2
            self.setTheTotalCount()
            self.gui_trg.r41.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r42.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r43.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR5(self, case):
        if case == 1:
            self.r5Count = 0
            self.setTheTotalCount()
            self.gui_trg.r51.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r52.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r5Count = 1
            self.setTheTotalCount()
            self.gui_trg.r51.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r52.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR6(self, case):
        if case == 1:
            self.r6Count = 0
            self.setTheTotalCount()
            self.gui_trg.r61.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r62.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r6Count = 1
            self.setTheTotalCount()
            self.gui_trg.r61.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r62.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR7(self, case):
        if case == 1:
            self.r7Count = 0
            self.setTheTotalCount()
            self.gui_trg.r71.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r72.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r7Count = 1
            self.setTheTotalCount()
            self.gui_trg.r71.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r72.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR8(self, case):
        if case == 1:
            self.r8Count = 0
            self.setTheTotalCount()
            self.gui_trg.r81.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r82.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r8Count = 1
            self.setTheTotalCount()
            self.gui_trg.r81.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r82.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
    def OnClickR9(self, case):
        if case == 1:
            self.r9Count = 0
            self.setTheTotalCount()
            self.gui_trg.r91.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")
            self.gui_trg.r92.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        elif case == 2:
            self.r9Count = 1
            self.setTheTotalCount()
            self.gui_trg.r91.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
            self.gui_trg.r92.setStyleSheet("QLabel{ background:transparent; color:#6aa0de; font-family:Tahoma; font-weight:bold; font-size:14px; }")

    def setTheTotalCount(self):
        if self.r1Count != 9:
            _r1Count=self.r1Count
        else:
            _r1Count=0
        if self.r2Count != 9:
            _r2Count=self.r2Count
        else:
            _r2Count=0
        if self.r3Count != 9:
            _r3Count=self.r3Count
        else:
            _r3Count=0
        if self.r4Count != 9:
            _r4Count=self.r4Count
        else:
            _r4Count=0
        if self.r5Count != 9:
            _r5Count=self.r5Count
        else:
            _r5Count=0
        if self.r6Count != 9:
            _r6Count=self.r6Count
        else:
            _r6Count=0
        if self.r7Count != 9:
            _r7Count=self.r7Count
        else:
            _r7Count=0
        if self.r8Count != 9:
            _r8Count=self.r8Count
        else:
            _r8Count=0
        if self.r9Count != 9:
            _r9Count=self.r9Count
        else:
            _r9Count=0
        self.totalCount = _r1Count+_r2Count+_r3Count+_r4Count+_r5Count+_r6Count+_r7Count+_r8Count+_r9Count
        self.gui_trg.lb_totalCount.setText(str(self.totalCount)+" /12")
        if self.totalCount <= 5:
            self.gui_trg.lb_totalCount.setStyleSheet("QLabel{ background:transparent; color:#80eb34; font-family:Bahnschrift SemiBold; font-size:24px; }")
        elif self.totalCount <= 7:
            self.gui_trg.lb_totalCount.setStyleSheet("QLabel{ background:transparent; color:#ebe834; font-family:Bahnschrift SemiBold; font-size:24px; }")
        else:
            self.gui_trg.lb_totalCount.setStyleSheet("QLabel{ background:transparent; color:#eb6134; font-family:Bahnschrift SemiBold; font-size:24px; }")

    def onClickSave(self):
        if (self.r1Count==9 or self.r2Count==9 or self.r3Count==9 or self.r4Count==9 or self.r5Count==9 or self.r6Count==9 or self.r7Count==9 or self.r8Count==9 or self.r9Count==9):
            print("Triage not complete.")
            return
        # create json
        matrix_name = self.gui_trg.lb_name.text()
        new_matrix =(matrix_name+";"
            +str(self.totalCount)+";"
            +str(self.r1Count)+";"
            +str(self.r2Count)+";"
            +str(self.r3Count)+";"
            +str(self.r4Count)+";"
            +str(self.r5Count)+";"
            +str(self.r6Count)+";"
            +str(self.r7Count)+";"
            +str(self.r8Count)+";"
            +str(self.r9Count)+"\n")
        json_mtx = json.dumps(new_matrix)
        # Opening JSON file
        with open('src/gui_mores/triages.history', "r") as storeddata:
            # returns JSON object as a dictionary
            data = storeddata.readlines()
            currentSize = len(data)
        os.remove("src/gui_mores/triages.history")
        if currentSize < 20:
            data.insert(0, new_matrix)
        elif currentSize == 20:
            data.pop(19)
            data.insert(0, new_matrix)
        # write to file
        with open('src/gui_mores/triages.history', "a") as storeddata:
            for item in data:
                storeddata.write(item)
        self.clearLayout(self.vbox)
        self.setHistory()

    def onSaveNReset(self):
        self.onClickSave()
        self.setStyleSheets()

    def onClickReset(self):
        self.setStyleSheets()

    def onHomeClicked(self):
        self.widget.setCurrentIndex(0)
        self.widget.removeWidget(self.menu_wg)

    def tunnelWidget(self, widget, menu_wg):
        self.widget = widget
        self.menu_wg = menu_wg

    def setStyleSheets(self):
        self.totalCount = 0
        self.r1Count = 9
        self.r2Count = 9
        self.r3Count = 9
        self.r4Count = 9
        self.r5Count = 9
        self.r6Count = 9
        self.r7Count = 9
        self.r8Count = 9
        self.r9Count = 9
        self.gui_trg.lb_name.setText("Unnamed")
        self.gui_trg.lb_totalCount.setText("0 /12")
        self.gui_trg.lb_totalCount.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Bahnschrift SemiBold; font-size:24px; }")
        self.gui_trg.r11.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r12.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r13.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r14.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r21.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r22.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r31.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r32.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r41.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r42.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r43.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r51.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r52.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r61.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r62.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r71.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r72.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r81.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r82.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r91.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")
        self.gui_trg.r92.setStyleSheet("QLabel{ background:transparent; color:white; font-family:Tahoma; font-weight:bold; font-size:13px; }")

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
