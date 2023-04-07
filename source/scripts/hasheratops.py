#!/usr/bin/env python3

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QTableWidgetItem

from configparser import ConfigParser
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class Hasheratops(QObject):
    finished = pyqtSignal()
    percentage = pyqtSignal(int)
    tablesetter = pyqtSignal(int, int, object)
    labarradistato = pyqtSignal(str)
    perlatabella = pyqtSignal(int, int, int)
    passthedata = pyqtSignal(list, list)

    cfg = ConfigParser()
    cfg.read('config/config.ini')

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    VirusTotal_URL= "https://www.virustotal.com/api/v3/files/"

    lines=None

    # Define "main" function
    def main(self):
        # Print for UX
        print('\nWelcome to RepXdb by L7!\nStart fetching data...\n')

        VirusTotal_APIKEY = self.cfg.get('settings', 'virustotal_apikey')
        flag_SSL_Bypass = self.cfg.get('settings', 'ssl_cert')
        lines = self.lines.split("\n")
        row = 0
        prog_index = 0
        filedata = []

        self.perlatabella.emit(1,len(lines),6)
        self.printProgressBar(0, len(lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
        # Peform API request for every hash in input /w for loop
        for line in lines:
            # Delete excessive blanks
            line = line.strip()
            line = line.replace('\n', '')
            shatype = len(line)
            if (shatype !=32) and (shatype !=40) and (shatype !=64):
                self.tablesetter.emit(row, 0, "#PASS")
                prog_index = prog_index + 1
                self.printProgressBar(prog_index, len(lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
                continue

            # Handle VirusTotal API request
            if flag_SSL_Bypass == "TRUE" :
                flag_ssl = False
            else :
                flag_ssl = True
            headers_VirusTotal = {"Accept": "application/json", "x-apikey": VirusTotal_APIKEY}
            response_VirusTotal = requests.request("GET", self.VirusTotal_URL+line, verify=flag_ssl, headers= headers_VirusTotal)
            data_VirusTotal = response_VirusTotal.json()
            
            # VirusTotal json parse attributes
            try:
                vt_json_getstr = data_VirusTotal['data'].get('attributes')
                vt_mal_score = str(vt_json_getstr.get('last_analysis_stats').get("malicious"))
                vt_susp_score = str(vt_json_getstr.get('last_analysis_stats').get("suspicious"))
                vt_undet_score = str(vt_json_getstr.get('last_analysis_stats').get("undetected"))
                vt_hless_score = str(vt_json_getstr.get('last_analysis_stats').get("harmless"))
                vt_comm_score = str(vt_json_getstr.get('reputation'))
                vt_tot_score = int(vt_mal_score) + int(vt_susp_score) + int(vt_undet_score) + int(vt_hless_score)
                vt_signatureinfo = vt_json_getstr.get('signature_info')
                try:
                    vt_signverif = str(vt_signatureinfo.get('verified'))
                    if vt_signverif == 'None' :
                        vt_signverif = 'NOT signed'
                    vt_signature = str(vt_signatureinfo.get('product')) + ' : ' + vt_signverif
                    vt_signer = str(vt_signatureinfo.get('signers'))
                    vt_signer = vt_signer.split(';')
                    vt_signer = vt_signer[0]
                    vt_signdescr = str(vt_signatureinfo.get('description')) + ' : v.' + str(vt_signatureinfo.get('file version'))
                except:
                    vt_signer = 'N\\A'
                    vt_signature = 'N\\A'
                    vt_signdescr = 'N\\A'
            
                try:
                    data = [
                        line,
                        vt_mal_score+"/"+str(vt_tot_score),
                        vt_comm_score,
                        vt_signature,
                        vt_signer,
                        vt_signdescr
                    ]
                except Exception as e:
                    print(e)
                    data = [ line, 'N\A', 'N\A', 'N\A', 'N\A', 'N\A' ]

            except Exception as e:
                print(e)
                try:
                    tris = data_VirusTotal['error'].get('code')
                    if tris == "NotFoundError":
                        data = [ line, 'FileNotFound', 'FileNotFound', 'FileNotFound', 'FileNotFound', 'FileNotFound' ]
                    else:
                        data = [ line, 'Error', 'Error', 'Error', 'Error', 'Error' ]
                except:
                    data = [ line, 'Error', 'Error', 'Error', 'Error', 'Error' ]

            prog_index = prog_index + 1
            self.printProgressBar(prog_index, len(lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
            for i in range(6) :
                self.tablesetter.emit(row,i,QTableWidgetItem(data[i]))
            row = row + 1
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
            print('Error Code 8004: ' + str(e))
            self.labarradistato.emit('Error Code 8004: ' + str(e))
            self.finished.emit()
