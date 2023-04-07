#!/usr/bin/env python3

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QTableWidgetItem

from configparser import ConfigParser
import requests

class Troppip(QObject):
    finished = pyqtSignal()
    percentage = pyqtSignal(int)
    tablesetter = pyqtSignal(int, int, object)
    labarradistato = pyqtSignal(str)
    perlatabella = pyqtSignal(int)
    passthedata = pyqtSignal(list, list)
    cfg = ConfigParser()
    lines=None

    # API URLs
    AbuseIPDB_URL = "https://api.abuseipdb.com/api/v2/check"

    # Define "main" function
    def main(self):
        # API KEYs
        self.cfg.read('config/config.ini')
        AbuseIPDB_APIKEY = self.cfg.get('settings', 'abuseipdb_apikey')

        # check for mandatory
        if AbuseIPDB_APIKEY=='None' :
            self.labarradistato.emit("Error: Missing ABUSEIPDB API.")
            self.finished.emit()
            return

        self.lines = self.lines.split("\n")

        # Set parameters for XLSX
        row = 0
        prog_index = 0
        filedata = []
        countryList = []
        self.perlatabella.emit(len(self.lines))
        # Initial call to print 0% progress
        self.printProgressBar(0, len(self.lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
        flag_SSL_Bypass = self.cfg.get('settings', 'ssl_cert')
        try :
            # Peform API request for every IP in input /w for loop
            for IP in self.lines:
                # Delete unwanted chars
                IP = IP.strip()
                IP = IP.replace('\n', '')
                IP = IP.replace('[', '')
                IP = IP.replace(']', '')
                IP = IP.replace('(', '')
                IP = IP.replace(')', '')
                if len(IP) < 7 or len(IP) > 15 or not "." in IP:
                    prog_index = prog_index + 1
                    self.printProgressBar(prog_index, len(self.lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
                    continue
                ###########      Handle API requests      ###########
                if flag_SSL_Bypass == "TRUE":
                    flag_ssl = False
                else:
                    flag_ssl = True
                # Handle AbuseIPDB API request
                try:
                    response_AbuseIPDB = requests.request(method="GET", url=self.AbuseIPDB_URL, verify=flag_ssl, headers={"accept": "application/json","key": AbuseIPDB_APIKEY},params={'ipAddress': IP, 'verbose': True})
                    data_AbuseIPDB = response_AbuseIPDB.json()
                except Exception as e :
                    self.labarradistato.emit("Error Code 5056 : invalid")
                    print("Error Code 5056 : invalid")
                    data_AbuseIPDB = 'N\\A'
                ###########      Parse Jsons      ###########
                # AbuseIPDB json parse attributes
                abip_json_getstr = data_AbuseIPDB['data']
                ab_score = str(abip_json_getstr.get("abuseConfidenceScore"))
                ###########      Output file      ###########
                # Write the output file
                data = [
                    IP,
                    str(abip_json_getstr.get("countryCode")),
                    str(abip_json_getstr.get("domain")),
                    str(abip_json_getstr.get("isp")),
                    str(abip_json_getstr.get("usageType")),
                    str(abip_json_getstr.get("lastReportedAt")),
                    ab_score+"%",
                ]
                prog_index = prog_index + 1
                self.printProgressBar(prog_index, len(self.lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
                countryList.append(data[1])
                for i in range(7):
                    self.tablesetter.emit(row,i,QTableWidgetItem(data[i]))
                filedata.append(data)
                row = row+1
            self.passthedata.emit(filedata, countryList)
            self.labarradistato.emit("Execution completed.")
        except Exception as e :
            self.labarradistato.emit("Error Code 5001: Something went wrong!")
            print("Error Code 5001: Something went wrong: " + str(e))

    # Print iterations progress
    def printProgressBar (self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        percent = int(percent[:-2])
        self.percentage.emit(percent)

    def setLines(self, given_iplist) :
        self.lines = given_iplist

    # Launch the script
    def run(self):
        try:
            self.main()
            self.finished.emit()
            print("INFO: Troppip completed.")
        except Exception as e:
            print('Error Code 4004: ' + str(e))
            self.labarradistato.emit('Error Code 4004: ' + str(e))
            self.finished.emit()
