#!/usr/bin/env python3

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QTableWidgetItem
from configparser import ConfigParser

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import hashlib

class Urleodactyl(QObject):
    finished = pyqtSignal()
    percentage = pyqtSignal(int)
    tablesetter = pyqtSignal(int, int, object)
    labarradistato = pyqtSignal(str)
    perlatabella = pyqtSignal(int, int)
    passthedata = pyqtSignal(list, list)

    cfg = ConfigParser()
    cfg.read('config/config.ini')

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    VirusTotal_URL= "https://www.virustotal.com/api/v3/urls/"
    VirusTotal_Domain= "https://www.virustotal.com/api/v3/domains/"

    lines=None

    # Define "main" function
    def main(self):
        # Print for UX
        print('\nWelcome to RepXdb by L7!\nStart fetching data...\n')
        #configuration
        VirusTotal_APIKEY = self.cfg.get('settings', 'virustotal_apikey')
        flag_SSL_Bypass = self.cfg.get('settings', 'ssl_cert')
        lines = self.lines.split("\n")
        row = 0
        prog_index = 0
        filedata = []
        #set the table for data gui
        self.perlatabella.emit(len(lines),8)
        self.printProgressBar(0, len(lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
        #check if sslbypass is enabled
        if flag_SSL_Bypass == "TRUE" :
            flag_ssl = False
        else :
            flag_ssl = True
        # Peform API request for every hash in input /w for loop
        for line in lines:
            # Delete excessive blanks
            line = line.strip()
            line = line.replace('\n', '')
            line = line.replace('hxxp', 'http')
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.lower()
            if len(line) < (3) or not "." in line:
                self.tablesetter.emit(row, 0, "#PASS")
                prog_index = prog_index + 1
                self.printProgressBar(prog_index, len(lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
                continue
            hasthehttp = line[0:4]
            # Handle VirusTotal API request
            if hasthehttp != 'http':
                toBeResv=line
                headers_VirusTotal = {"Accept": "application/json", "x-apikey": VirusTotal_APIKEY}
                response_VirusTotal = requests.request("GET", self.VirusTotal_Domain+line, verify=flag_ssl, headers= headers_VirusTotal)
                data_VirusTotal = response_VirusTotal.json()
            else:
                _toBeResv=line.split('://')
                _toBeResv=_toBeResv[1].split('.')
                sizetbr=len(_toBeResv)
                toBeResv=_toBeResv[sizetbr-2]+"."+_toBeResv[sizetbr-1]
                hastheslash = line[-1]
                if hastheslash != '/':
                    line = line+'/'
                urlsha = hashlib.sha256(line.encode())
                headers_VirusTotal = {"Accept": "application/json", "x-apikey": VirusTotal_APIKEY}
                response_VirusTotal = requests.request("GET", self.VirusTotal_URL+urlsha.hexdigest(), verify=flag_ssl, headers= headers_VirusTotal)
                data_VirusTotal = response_VirusTotal.json()
            # VirusTotal json parse attributes
            vt_mal_score = vt_susp_score = vt_undet_score = vt_hless_score = vt_comm_score = vt_tot_score = vt_times_submitted = vt_kaspersky = vt_bitdef = vt_sohpos = rep_stat = 'N\\A'
            try:
                vt_json_getstr = data_VirusTotal['data'].get('attributes')
                vt_mal_score = str(vt_json_getstr.get('last_analysis_stats').get("malicious"))
                vt_susp_score = str(vt_json_getstr.get('last_analysis_stats').get("suspicious"))
                vt_undet_score = str(vt_json_getstr.get('last_analysis_stats').get("undetected"))
                vt_hless_score = str(vt_json_getstr.get('last_analysis_stats').get("harmless"))
                vt_comm_score = str(vt_json_getstr.get('reputation'))
                vt_tot_score = int(vt_mal_score) + int(vt_susp_score) + int(vt_undet_score) + int(vt_hless_score)
                vt_times_submitted = str(vt_json_getstr.get('times_submitted'))
                try:
                    vt_kaspersky = str(vt_json_getstr.get('last_analysis_results').get('Kaspersky').get('result'))
                    vt_bitdef = str(vt_json_getstr.get('last_analysis_results').get('BitDefender').get('result'))
                    vt_sohpos = str(vt_json_getstr.get('last_analysis_results').get('Sophos').get('result'))
                except Exception as e:
                    vt_kaspersky = 'N\\a'
                    vt_bitdef = 'N\\a'
                    vt_sohpos = 'N\\a'
                    self.labarradistato.emit("Error Code 9002: " + str(e))
            except Exception as e:
                self.labarradistato.emit("Error Code 9001: " + str(e))
            #DNS resolution
            resolved_IP = None
            try:
                headers_vtArecord = {"Accept": "application/json", "x-apikey": VirusTotal_APIKEY}
                response_vtArecord = requests.request("GET", self.VirusTotal_Domain+str(toBeResv)+"/resolutions?limit=1", verify=flag_ssl, headers= headers_vtArecord)
                data_vtArecord = response_vtArecord.json()
                resolved_IP = data_vtArecord['data']
                resolved_IP = resolved_IP[0].get('attributes').get('ip_address')
            except Exception as esces:
                print(esces)
                resolved_IP = 'N\\A'
            if (vt_mal_score == 'N\\A' or vt_tot_score == 'N\\A'):
                rep_stat = 'N\\A'
            else:
                rep_stat = str(vt_mal_score)+"/"+str(vt_tot_score)
            try:
                data = [
                    line,
                    rep_stat,
                    vt_comm_score,
                    vt_times_submitted,
                    resolved_IP,
                    vt_kaspersky,
                    vt_bitdef,
                    vt_sohpos
                ]
            except Exception as erc:
                print("empty data"+str(erc))
                data = [ line, 'N\\A', 'N\\A', 'N\\A', 'N\\A', 'N\\A', 'N\\A', 'N\\A' ]

            prog_index=prog_index+1
            self.printProgressBar(prog_index, len(lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
            for i in range(8) :
                self.tablesetter.emit(row,i,QTableWidgetItem(data[i]))
            row = row+1
            filedata.append(data)
        empty = []
        self.passthedata.emit(filedata, empty)
        self.labarradistato.emit("Execution completed.")

    # Print iterations progress
    def printProgressBar (self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        percent = int(percent[:-2])
        self.percentage.emit(percent)

    def setLines(self, given_hashlist) :
        self.lines = given_hashlist

    # Launch the script
    def run(self):
        try:
            self.main()
            self.finished.emit()
            print("INFO: Repxdbl7 completed.")
        except Exception as e:
            print('Error Code 9004: ' + str(e))
            self.labarradistato.emit('Error Code 9004: ' + str(e))
            self.finished.emit()
