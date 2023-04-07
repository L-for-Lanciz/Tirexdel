#!/usr/bin/env python3

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QHeaderView, QScrollArea, QVBoxLayout
from PyQt6.QtGui import QGuiApplication, QIcon, QFont
from PyQt6.QtCore import QDir, QObject, QThread, pyqtSignal
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

import sys
from collections import Counter
import pyqtgraph as pg

import src.scripts.repxdbll as repx
import src.utils.webview as webvw
import src.utils.xl_generator as xl_gen
import src.gui.gui_rv_item as rvItem

class GuiIpAddrNewl(QtWidgets.QMainWindow):
    gui_win = None
    statusinfo = None
    cache_data = None
    cache_countries = None
    widget = None
    vbox = QVBoxLayout()

    def __init__(self):
        super(GuiIpAddrNewl, self).__init__()
        self.gui_win = loadUi('design/grafic_newl.ui', self)
        # set styles
        self.gui_win.bt_home.setStyleSheet("QToolButton{ image: url(images/home.png); background: transparent;}""QToolButton:hover{image: url(images/home_hover);}")
        self.gui_win.lb_iplist.setStyleSheet("QLabel{ background: transparent; color: white; text-align: left; font-family:url(fonts/NiveauGroteskBlack_SmallCaps); font-weight:bold; font-size:18px; margin-left:-30px;}")
        self.gui_win.fr_inp.setStyleSheet("QFrame{ image: url(images/bbetexedit.png); }")
        self.gui_win.inp_list.setStyleSheet("QTextEdit{ background: transparent; color: white; font-family:Calibri; font-size:17px}")
        self.gui_win.centralwidget.setStyleSheet("QWidget{ background-image: url(images/banner.jpg);}")
        self.gui_win.fr_logo.setStyleSheet("QFrame{ image: url(images/decor_pic.png); background:transparent; }")
        self.gui_win.bt_submit.setStyleSheet("QToolButton{ image: url(images/searchicon.png); background: transparent; color: white; font-family:url(fonts/NiveauGroteskBlack_SmallCaps); font-weight:bold; font-size:15px; }""QToolButton:hover{image: url(images/searchicon_hover);}")
        self.gui_win.bt_toxl.setStyleSheet("QToolButton{ image: url(images/toxl_hover.png); background: transparent;}""QToolButton:hover{image: url(images/toxl_hover);}")
        self.gui_win.bt_otx.setStyleSheet("QToolButton{ image: url(images/otx.png); background: transparent;}""QToolButton:hover{image: url(images/otx_hover);}")
        self.gui_win.frame4borders.setStyleSheet("QWidget{ image: url(images/framebord.png); background:transparent; }")
        # set behaviours
        # statusbar
        self.statusinfo = self.gui_win.statusbar
        # buttons
        self.gui_win.bt_submit.clicked.connect(self.submit_clicked)
        self.gui_win.bt_toxl.clicked.connect(self.toxl_clicked)
        self.gui_win.bt_toxl.setEnabled(False)
        #self.gui_win.bt_otx.clicked.connect(self.onOtxClicked)
        self.gui_win.bt_home.clicked.connect(self.onHomeClicked)
        # progressbar
        self.gui_win.pb_progbar.setValue(0)
        # textedit
        self.gui_win.inp_list.setAcceptRichText(False)
        # plot
        graficus = self.gui_win.graphc
        graficus.setBackground('transparent')
        graficus.getAxis('left').setTextPen('#f7f0c6')
        graficus.getAxis('left').setPen('#f7f0c6')
        graficus.getAxis('bottom').setTextPen('#f7f0c6')
        graficus.getAxis('bottom').setPen('#f7f0c6')
        graficus.setEnabled(False)
        self.gui_win.frame4borders.setStyleSheet("QWidget{ background:transparent }")
        graficus.hide()
        # other
        self.gui_win.bt_otx.hide()
        self.gui_win.pb_progbar.hide()
        self.gui_win.scrollAreaWidgetContents.setLayout(self.vbox)

    def submit_clicked(self) :
        print("INFO: submit clicked")
        given_ioclist = self.gui_win.inp_list.toPlainText()
        self.gui_win.pb_progbar.show()
        self.gui_win.graphc.hide()
        self.gui_win.graphc.clear()
        self.clearLayout(self.vbox)
        #self.setToXlStatus(False)
        self.startThread(given_ioclist)

    def toxl_clicked(self) :
        print("INFO: toxl clicked")
        exported = xl_gen.exportToXl(self.cache_data, 1)
        if exported :
            self.statusinfo.showMessage("Execution completed. You can find your results in the 'txd_results.xlsx' file.")
        else :
            self.statusinfo.showMessage("Error Code 5073: Error occurred during export.")

    def onHomeClicked(self) :
        self.widget.setCurrentIndex(0)

    def tunnelWidget(self, widget) :
        self.widget = widget

    def onScriptFinished(self) :
        self.gui_win.bt_submit.setEnabled(True)

    def progressBarLoading(self, x) :
        self.gui_win.pb_progbar.setValue(x)

    def setStatusBarOverIP(self, printing) :
        self.statusinfo.showMessage(printing)
        if printing == 'Execution completed.' :
            #self.setToXlStatus(True)
            self.setTheGraph(self.cache_countries)

    def startThread(self, given_iplist) :
        if (len(given_iplist)) > 6 :
            self.thread = QThread()
            self.worker = repx.Repxdbll()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.setLines(given_iplist)
            self.thread.start()
            self.statusinfo.setStyleSheet("QStatusBar{color:black}")
            self.statusinfo.showMessage("Request in progress...")
            self.gui_win.bt_submit.setEnabled(False)
            self.worker.percentage.connect(self.progressBarLoading)
            self.worker.labarradistato.connect(self.setStatusBarOverIP)
            #self.worker.perlatabella.connect(self.setRecyclerView)
            self.worker.tablesetter.connect(self.setRecyclerView)
            self.worker.passthedata.connect(self.getDataFromQuery)
            self.thread.finished.connect(self.onScriptFinished)
        else :
            self.statusinfo.setStyleSheet("QStatusBar{color:red}")
            self.statusinfo.showMessage("Please, provide a valid input!")

    def setRecyclerView(self, j1, j2, data) :
        self.vbox.addWidget(rvItem.GuiRvItem(data))

    def getDataFromQuery(self, data, countries) :
        self.cache_data = data
        self.cache_countries = countries

    def setToXlStatus(self, status) :
        if status == True:
            self.gui_win.bt_toxl.setStyleSheet("QToolButton{ image: url(images/toxl.png); background: transparent;}""QToolButton:hover{image: url(images/toxl_hover);}")
        self.gui_win.bt_toxl.setEnabled(status)

    def setTheGraph(self, countryList) :
        #show otx button since script finished
        self.gui_win.bt_otx.show()
        #set the graph for contries
        graficus = self.gui_win.graphc
        self.gui_win.frame4borders.setStyleSheet("QWidget{background-image: url(images/framebord.png);}")
        graficus.show()
        countries = list(Counter(countryList).keys()) # equals to list(set(words))
        y_axis = list(Counter(countryList).values()) # counts the elements' frequency
        labels = list(enumerate(countries))
        y_axisF = []
        labelsF = []
        countriesF = []
        x_axis = []
        topfifteen = sorted(range(len(y_axis)), key=lambda i: y_axis[i], reverse=True)[:16]
        for onecnt in range(len(topfifteen)) :
            y_axisF.append(y_axis[topfifteen[onecnt]])
            countriesF.append(countries[topfifteen[onecnt]])

        labelsF = list(enumerate(countriesF))
        index = 0
        for singleton in countriesF :
            x_axis.append(index)
            index = index+1

        ax=graficus.getAxis('bottom')
        ax.setTicks([labelsF])
        bargraph = pg.BarGraphItem(x = x_axis, height = y_axisF, width = 0.2, brush = '#444052')
        self.gui_win.graphc.addItem(bargraph)

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    #def onOtxClicked(self) :
    #smthing
