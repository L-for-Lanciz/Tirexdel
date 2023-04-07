from PyQt6 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt6.QtGui import QIcon
import os

class Ui_WebView(object):
    def setupUi(self, typeOfIOC, Dialog, IOC):
        Dialog.setObjectName("OTX Navigator")
        Dialog.resize(900, 450)
        Dialog.setWindowIcon(QIcon('images/otx_logo_dark.png'))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        if typeOfIOC == 1 :
            URL = 'https://otx.alienvault.com/indicator/ip/'
        elif typeOfIOC == 2 :
            URL = 'https://otx.alienvault.com/indicator/url/'
        elif typeOfIOC == 3 :
            URL = 'https://otx.alienvault.com/indicator/file/'
        else :
            return
        self.webEngineView.load(QtCore.QUrl(URL+IOC))
        self.verticalLayout.addWidget(self.webEngineView)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "OTX Navigator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
