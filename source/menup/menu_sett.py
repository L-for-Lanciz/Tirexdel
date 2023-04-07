#!/usr/bin/env python3

from PyQt6 import QtWidgets, QtCore
from PyQt6.uic import loadUi

from configparser import ConfigParser

class GuiSettings(QtWidgets.QMainWindow):
    gui_set = None
    widget = None
    menu_wg = None
    cfg = ConfigParser()
    cfg.read('config/config.ini')
    #setting bools
    sslbp_bool = None
    repxdbll_bool = None
    #apikeys
    cfg_vt_key = None
    cfg_abid_key = None
    cfg_puldv_key = None
    cfg_shod_key = None
    cfg_xforce_key = None
    cfg_meta_key = None

    def __init__(self):
        #load gui
        super(GuiSettings, self).__init__()
        self.gui_set = loadUi('design/settings.ui', self)
        #stylesheet
        self.gui_set.settingswidget.setStyleSheet("QWidget{ background-color:#463595; }")
        self.gui_set.pic_pref.setStyleSheet("QToolButton{ image: url(images/dwpa_sett.png);}")
        self.gui_set.pic_apik.setStyleSheet("QToolButton{ image: url(images/apik_sett.png);}")
        self.gui_set.bt_save.setStyleSheet("QToolButton{ border:1px solid #fff; background: transparent; color: white; font-weight: bold;}""QToolButton:hover{border:1px solid #6aa0de; color:#6aa0de;}")
        self.gui_set.bt_saveandexit.setStyleSheet("QToolButton{ border:1px solid #fff; background: transparent; color: white; font-weight: bold;}""QToolButton:hover{border:1px solid #6aa0de; color:#6aa0de;}")
        self.gui_set.bt_exit.setStyleSheet("QToolButton{ border:1px solid #fff; background: transparent; color: white; font-weight: bold;}""QToolButton:hover{border:1px solid #6aa0de; color:#6aa0de;}")

        self.gui_set.infobutton.setStyleSheet("QToolButton{ image: url(images/infobutt.png); background: transparent;}")
        #buttons
        self.gui_set.sslButton.clicked.connect(self.setSSLBypass)
        self.gui_set.laypButton.clicked.connect(self.setLayoutIp)
        #save/exit
        self.gui_set.bt_save.clicked.connect(self.onClickSave)
        self.gui_set.bt_saveandexit.clicked.connect(self.onSaveNExit)
        self.gui_set.bt_exit.clicked.connect(self.onHomeClicked)
        #preferences
        try :
            self.gui_set.edit_dwpath.setText(self.cfg.get('settings', 'downloadto'))
            self.sslbp_bool = self.cfg.get('settings', 'ssl_cert')
            self.repxdbll_bool = self.cfg.get('settings', 'ip_layout')
        except Exception as e:
            print("Error Code 6020: could not read - preferences. "+str(e))
        self.gui_set.sslButton.setText(self.sslbp_bool)
        self.gui_set.laypButton.setText(self.repxdbll_bool)
        #sslbypass
        if self.sslbp_bool == "FALSE" :
            self.gui_set.sslButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background:transparent; color:rgb(255,0,0); font-size:12px; font-weight:bold;}")
        else :
            self.gui_set.sslButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background:transparent; color:#00ff7f; font-size:12px; font-weight:bold;}")
        #iplayout
        if self.repxdbll_bool == "OLD" :
            self.gui_set.laypButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background:transparent; color:rgb(255,0,0); font-size:12px; font-weight:bold;}")
        else :
            self.gui_set.laypButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background:transparent; color:#00ff7f; font-size:12px; font-weight:bold;}")
        #apikeys
        try :
            self.cfg_vt_key = self.cfg.get('settings', 'virustotal_apikey')
            self.cfg_abid_key = self.cfg.get('settings', 'abuseipdb_apikey')
            self.cfg_puldv_key = self.cfg.get('settings', 'shodan_apikey')
            self.cfg_shod_key = self.cfg.get('settings', 'pulsedive_apikey')
            self.cfg_xforce_key = self.cfg.get('settings', 'xforce_apikey')
            self.cfg_meta_key = self.cfg.get('settings', 'meta_apikey')
        except :
            print("Error Code 6000: could not read - apikeys")
        self.gui_set.edit_vt.setText(self.cfg_vt_key)
        self.gui_set.edit_abid.setText(self.cfg_abid_key)
        self.gui_set.edit_shod.setText(self.cfg_puldv_key)
        self.gui_set.edit_puldv.setText(self.cfg_shod_key)
        self.gui_set.edit_xforce.setText(self.cfg_xforce_key)
        self.gui_set.edit_meta.setText(self.cfg_meta_key)

    def setSSLBypass(self):
        if self.sslbp_bool == "TRUE" :
            self.gui_set.sslButton.setText("FALSE")
            self.sslbp_bool = "FALSE"
            self.gui_set.sslButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background: transparent; color: rgb(255, 0, 0); font-weight: bold;}")
        else :
            self.gui_set.sslButton.setText("TRUE")
            self.sslbp_bool = "TRUE"
            self.gui_set.sslButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background: transparent; color:#00ff7f; font-weight: bold;}")

    def setLayoutIp(self):
        if self.repxdbll_bool == "NEW" :
            self.gui_set.laypButton.setText("OLD")
            self.repxdbll_bool = "OLD"
            self.gui_set.laypButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background: transparent; color: rgb(255, 0, 0); font-weight: bold;}")
        else :
            self.gui_set.laypButton.setText("NEW")
            self.repxdbll_bool = "NEW"
            self.gui_set.laypButton.setStyleSheet("QToolButton{ border:1px solid; border-color:white; background: transparent; color:#00ff7f; font-weight: bold;}")

    def onClickSave(self) :
        #preferences
        #downloadpath
        dw_path = self.gui_set.edit_dwpath.text()
        if (dw_path != self.cfg.get('settings', 'downloadto')) :
            self.cfg.set("settings", "downloadto", dw_path)
            with open("config/config.ini", 'w') as configfile:
                 self.cfg.write(configfile)
        #sslbypass
        if self.sslbp_bool != self.cfg.get('settings', 'ssl_cert') :
            self.cfg.set("settings", "ssl_cert", self.sslbp_bool)
            with open("config/config.ini", 'w') as configfile:
                 self.cfg.write(configfile)
        #layoutip
        if self.repxdbll_bool != self.cfg.get('settings', 'ip_layout') :
            self.cfg.set("settings", "ip_layout", self.repxdbll_bool)
            with open("config/config.ini", 'w') as configfile:
                 self.cfg.write(configfile)
        #apikeys
        vt_key = self.gui_set.edit_vt.text()
        abid_key = self.gui_set.edit_abid.text()
        puldv_key = self.gui_set.edit_puldv.text()
        shod_key = self.gui_set.edit_shod.text()
        xforce_key = self.gui_set.edit_xforce.text()
        meta_key = self.gui_set.edit_meta.text()
        #checksetapikeys
        if (vt_key != self.cfg_vt_key) :
            if (len(vt_key)<57 or len(vt_key)>71 ) :
                print("Error Code 6001: not valid")
            else :
                self.cfg.set("settings", "virustotal_apikey", vt_key)
                with open("config/config.ini", 'w') as configfile:
                    self.cfg.write(configfile)
        if (abid_key != self.cfg_abid_key) :
            if (len(abid_key)<70 or len(abid_key)>90 ) :
                print("Error Code 6002: not valid")
            else :
                self.cfg.set("settings", "abuseipdb_apikey", abid_key)
                with open("config/config.ini", 'w') as configfile:
                    self.cfg.write(configfile)
        if (shod_key != self.cfg_shod_key) :
            if (len(shod_key)<28 or len(shod_key)>36 ) :
                print("Error Code 6003: not valid")
            else :
                self.cfg.set("settings", "shodan_apikey", shod_key)
                with open("config/config.ini", 'w') as configfile:
                    self.cfg.write(configfile)
        if (puldv_key != self.cfg_puldv_key) :
            if (len(puldv_key)<57 or len(puldv_key)>71 ) :
                print("Error Code 6004: not valid")
            else :
                self.cfg.set("settings", "pulsedive_apikey", puldv_key)
                with open("config/config.ini", 'w') as configfile:
                    self.cfg.write(configfile)
        if (xforce_key != self.cfg_xforce_key) :
            if (len(xforce_key)<65 or len(xforce_key)>85 ) :
                print("Error Code 6005: not valid")
            else :
                self.cfg.set("settings", "xforce_apikey", xforce_key)
                with open("config/config.ini", 'w') as configfile:
                    self.cfg.write(configfile)
        if (meta_key != self.cfg_meta_key) :
            if (len(meta_key)<28 or len(meta_key)>36 ) :
                print("Error Code 6006: not valid")
            else :
                self.cfg.set("settings", "meta_apikey", meta_key)
                with open("config/config.ini", 'w') as configfile:
                    self.cfg.write(configfile)

    def onSaveNExit(self) :
        self.onClickSave()
        self.onHomeClicked()

    def onHomeClicked(self) :
        self.widget.setCurrentIndex(0)
        self.widget.removeWidget(self.menu_wg)

    def tunnelWidget(self, widget, menu_wg) :
        self.widget = widget
        self.menu_wg = menu_wg
