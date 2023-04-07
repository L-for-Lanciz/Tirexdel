#!/usr/bin/env python3

from configparser import ConfigParser

class Credits(object):

    def creator(self, SecondWindow):
        sindow = SecondWindow
        sindow.btc.setStyleSheet("QFrame{ image: url(images/btc.jpg) }")
        sindow.eth.setStyleSheet("QFrame{ image: url(images/eth.jpg) }")
