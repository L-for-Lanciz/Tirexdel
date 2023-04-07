#!/usr/bin/env python3

from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QGuiApplication, QIcon, QFont
from PyQt6.QtCore import QDir, QObject, QThread, pyqtSignal
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

import sys

import src.scripts.hasheratops as hashrt
import src.utils.webview as webvw
import src.utils.xl_generator as xl_gen

class GuiHash(QtWidgets.QMainWindow):
    gui_win = None
    statusinfo = None
    cache_data = None
    cache_countries = None

    def __init__(self):
        super(GuiHash, self).__init__()
        self.gui_win = loadUi('design/grafic.ui', self)
        # set styles
        self.gui_win.bt_home.setStyleSheet("QToolButton{ image: url(images/home.png); background: transparent;}""QToolButton:hover{image: url(images/home_hover);}")
        self.gui_win.lb_title.setStyleSheet("QLabel{ background: transparent; color: white; text-align: left; font-family:url(fonts/NiveauGroteskBlack_SmallCaps); font-weight:bold; font-size:28px; margin-left:-20px;}")
        self.gui_win.lb_iplist.setStyleSheet("QLabel{ background: transparent; color: white; text-align: left; font-family:url(fonts/NiveauGroteskBlack_SmallCaps); font-weight:bold; font-size:18px; margin-left:-30px;}")
        self.gui_win.lb_iplist.setText("Hash list:")
        self.gui_win.fr_inp.setStyleSheet("QFrame{ image: url(images/betexedit.png); background:transparent; }")
        self.gui_win.inp_list.setStyleSheet("QTextEdit{ background: transparent; color: white; font-family:Calibri; font-size:17px}")
        self.gui_win.centralwidget.setStyleSheet("QWidget{ background-image: url(images/banner.jpg);}")
        self.gui_win.fr_logo.setStyleSheet("QFrame{ image: url(images/decor_pic.png); background:transparent; }")
        self.gui_win.bt_submit.setStyleSheet("QToolButton{ image: url(images/searchicon.png); background: transparent; color: white; font-family:url(fonts/NiveauGroteskBlack_SmallCaps); font-weight:bold; font-size:15px; }""QToolButton:hover{image: url(images/searchicon_hover);}")
        self.gui_win.bt_toxl.setStyleSheet("QToolButton{ image: url(images/toxl.png); background: transparent;}")
        self.gui_win.bt_otx.setStyleSheet("QToolButton{ image: url(images/otx.png); background: transparent;}")
        self.gui_win.table.setStyleSheet("QTableView{ color:white; }""QHeaderView::section { height:35px; font:13px; color:white; font-weight:bold; background-color:#4b4453; }""QTableCornerButton::section { background-color:#4b4453; }")
        # set behaviours
        # statusbar
        self.statusinfo = self.gui_win.statusbar
        # buttons
        self.gui_win.bt_submit.clicked.connect(self.submit_clicked)
        self.gui_win.bt_toxl.clicked.connect(self.toxl_clicked)
        self.gui_win.bt_toxl.setEnabled(False)
        self.gui_win.bt_otx.clicked.connect(self.onOtxClicked)
        self.gui_win.bt_home.clicked.connect(self.onHomeClicked)
        # progressbar
        self.gui_win.pb_progbar.setValue(0)
        # textedit
        self.gui_win.inp_list.setAcceptRichText(False)
        # plot
        self.gui_win.frame4borders.hide()
        self.gui_win.graphc.hide()
        #table
        self.gui_win.table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)

    def submit_clicked(self):
        print("INFO: submit clicked")
        given_ioclist = self.gui_win.inp_list.toPlainText()
        self.gui_win.table.clear()
        self.setToXlStatus(False)
        self.startThreadHash(given_ioclist)

    def toxl_clicked(self) :
        print("INFO: toxl clicked")
        exported = xl_gen.exportToXl(self.cache_data, 3)
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

    def setStatusBarOverUrlHash(self, printing) :
        self.statusinfo.showMessage(printing)
        if printing == 'Execution completed.' :
            self.setToXlStatus(True)

    def startThreadHash(self, given_hashlist) :
        if (len(given_hashlist)) > 31 :
            self.thread = QThread()
            self.worker = hashrt.Hasheratops()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.setLines(given_hashlist)
            self.thread.start()
            self.statusinfo.setStyleSheet("QStatusBar{color:black}")
            self.statusinfo.showMessage("Request in progress...")
            self.gui_win.bt_submit.setEnabled(False)
            self.worker.percentage.connect(self.progressBarLoading)
            self.worker.labarradistato.connect(self.setStatusBarOverUrlHash)
            self.worker.perlatabella.connect(self.setTable)
            self.worker.tablesetter.connect(self.fillTable)
            self.worker.passthedata.connect(self.getDataFromQuery)
            self.thread.finished.connect(self.onScriptFinished)
        else :
            self.statusinfo.setStyleSheet("QStatusBar{color:red}")
            self.statusinfo.showMessage("Please, provide a valid input!")

    def setTable(self, ioctype, row, cols) :
        table = self.gui_win.table
        table.setRowCount(row)
        table.setColumnCount(cols)
        if ioctype == 1 :
            table.horizontalHeader().setDefaultSectionSize(110)
            table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            table.setHorizontalHeaderLabels([
                'File Hash','Reputation','Community',
                'Product','Signer','Description'
            ])
        self.gui_win.bt_otx.show()

    def getDataFromQuery(self, data, countries) :
        self.cache_data = data
        self.cache_countries = countries

    def setToXlStatus(self, status) :
        if status == True:
            self.gui_win.bt_toxl.setStyleSheet("QToolButton{ image: url(images/toxl.png); background: transparent;}""QToolButton:hover{image: url(images/toxl_hover);}")
        self.gui_win.bt_toxl.setEnabled(status)

    def onOtxClicked(self) :
        row_cioc = self.gui_win.table.currentRow()
        col_cioc = self.gui_win.table.currentColumn()
        if col_cioc == 0 and row_cioc >= 0:
            try :
                got_cioc = self.cache_data[row_cioc]
                self.dialog = QtWidgets.QDialog()
                self.ui = webvw.Ui_WebView()
                self.ui.setupUi(3, self.dialog, got_cioc[0])
                self.dialog.setModal(True)
                self.dialog.show()
            except Exception as e:
                print(e)
                self.statusinfo.setStyleSheet("QStatusBar{color:red}")
                self.statusinfo.showMessage("Please select an IP for OTX.")
        else :
            self.statusinfo.setStyleSheet("QStatusBar{color:red}")
            self.statusinfo.showMessage("Please select an IP for OTX.")

    def fillTable(self, row, i, item) :
        if str(item) == "#PASS":
            self.gui_win.table.removeRow(row)
        else :
            self.gui_win.table.setItem(row,i,item)
