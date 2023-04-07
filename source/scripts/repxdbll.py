#!/usr/bin/env python3

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QTableWidgetItem

from configparser import ConfigParser
import requests
import base64
from shodan import Shodan
from OTXv2 import OTXv2, IndicatorTypes

import src.utils.tirexfactor as txf

class Repxdbll(QObject):
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
    VirusTotal_URL = "https://www.virustotal.com/api/v3/ip_addresses/"
    GreyNoise_URL = "https://api.greynoise.io/v3/community/"
    Pulsedive_URL = "https://pulsedive.com/api/info.php?indicator="
    Shodan_URL = "https://api.shodan.io/shodan/host/"
    XForce_URL = "https://api.xforce.ibmcloud.com:443"
    Meta_URL = "https://api.metadefender.com/v4/ip/"
    Otx_URL = "https://otx.alienvault.com/api/v1/indicators/IPv4/"

    # Define "main" function
    def main(self):
        # Print for UX
        print('INFO: Welcome to RepXdb by L7!\nINFO: Start fetching data...')
        # API KEYs
        self.cfg.read('config/config.ini')
        AbuseIPDB_APIKEY = self.cfg.get('settings', 'abuseipdb_apikey')
        VirusTotal_APIKEY = self.cfg.get('settings', 'virustotal_apikey')
        Shodan_APIKEY = self.cfg.get('settings', 'shodan_apikey')
        Pulsedive_APIKEY = self.cfg.get('settings', 'pulsedive_apikey')
        XForce_APIKEY = self.cfg.get('settings', 'xforce_apikey')
        Meta_APIKEY = self.cfg.get('settings', 'meta_apikey')
        # XForce Token
        token_bytes = XForce_APIKEY.encode("ascii")
        base64_bytes = base64.b64encode(token_bytes)
        token = base64_bytes.decode("ascii")
        # check for mandatory
        if AbuseIPDB_APIKEY=='None' :
            self.labarradistato.emit("Error: Missing ABUSEIPDB API.")
            self.finished.emit()
            return
        if VirusTotal_APIKEY=='None' :
            self.labarradistato.emit("Error: Missing VIRUSTOTAL API.")
            self.finished.emit()
            return

        self.lines = self.lines.split("\n")

        # Set parameters for XLSX
        row = 0
        prog_index = 0
        filedata = []
        countryList = []

        bool_layt = self.cfg.get('settings', 'ip_layout')
        if bool_layt == "OLD":
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
                    if bool_layt == "OLD":
                        self.tablesetter.emit(row, 0, "#PASS")
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
                # Handle VirusTotal API request
                try:
                    headers_VirusTotal = {"Accept": "application/json", "x-apikey": VirusTotal_APIKEY}
                    response_VirusTotal = requests.request("GET", self.VirusTotal_URL+IP, verify=flag_ssl, headers= headers_VirusTotal)
                    data_VirusTotal = response_VirusTotal.json()
                except :
                    self.labarradistato.emit("Error Code 5057 : invalid")
                    print("Error Code 5057 : invalid")
                    data_VirusTotal = 'N\\A'
                # Handle GreyNoise API request
                try:
                    headers_GreyNoise = {"Accept": "application/json"}
                    response_GreyNoise = requests.request("GET", self.GreyNoise_URL+IP, verify=flag_ssl, headers=headers_GreyNoise)
                    data_GreyNoise = response_GreyNoise.json()
                except Exception as e :
                    self.labarradistato.emit("Error Code 5058 : invalid")
                    print("Error Code 5058 : invalid")
                    data_GreyNoise = 'N\\A'
                # Handle Pulsedive API request
                try:
                    headers_Pulsedive= {"Accept": "application/json"}
                    response_Pulsedive = requests.request("GET", self.Pulsedive_URL+IP+"&pretty=1&key="+Pulsedive_APIKEY, verify=flag_ssl, headers=headers_Pulsedive)
                    data_Pulsedive = response_Pulsedive.json()
                except Exception as e :
                    self.labarradistato.emit("Error Code 5059 : invalid")
                    print("Error Code 5059 : invalid")
                    data_Pulsedive = 'N\\A'
                # Handle Shodan API request
                try:
                    headers_Shodan = {"Accept": "application/json"}
                    response_Shodan = requests.request("GET",  self.Shodan_URL+IP+"?key="+Shodan_APIKEY, verify=flag_ssl, headers=headers_Shodan)
                    response_Shodan = response_Shodan.json()
                    #json.dumps(dictionary, indent = 4)
                except Exception as e:
                    self.labarradistato.emit("Error Code 5003 : invalid")
                    print("Error Code 5003 : invalid; "+str(e))
                    response_Shodan = 'N\\A'
                # Handle IBM XForce API request
                try:
                    headers_XForce = {'Authorization': "Basic " + token, 'Accept': 'application/json'}
                    response_XForce = requests.get(self.XForce_URL+"/ipr/"+IP, params='', verify=flag_ssl, headers=headers_XForce, timeout=20)
                    response_XForce = response_XForce.json()
                except Exception as e :
                    self.labarradistato.emit("Error Code 5061 : invalid")
                    print("Error Code 5061 : invalid")
                    response_XForce = 'N\\A'
                # Handle Meta API Request
                try:
                    headers_Meta = { "apikey": Meta_APIKEY }
                    response_Meta = requests.request("GET", self.Meta_URL+IP, headers=headers_Meta, verify=flag_ssl)
                    response_Meta = response_Meta.json()
                except Exception as e :
                    self.labarradistato.emit("Error Code 5060 : invalid")
                    print("Error Code 5060 : invalid")
                    response_Meta = 'N\\A'
                # Handle OTX API Request
                try:
                    headers_Alvtx = {"Accept": "application/json"}
                    response_Alvtx = requests.request("GET", self.Otx_URL+IP+'/url_list', verify=flag_ssl, headers=headers_Alvtx)
                    response_Alvtx = response_Alvtx.json()
                    otx_urls = str(response_Alvtx.get('full_size'))
                except Exception as e :
                    self.labarradistato.emit("Error Code 5062 : invalid")
                    print("Error Code 5062 : invalid "+str(e))
                    otx_urls = '0'
                ###########      Parse Jsons      ###########
                # AbuseIPDB json parse attributes
                abip_json_getstr = data_AbuseIPDB['data']
                ab_score = str(abip_json_getstr.get("abuseConfidenceScore"))
                # VirusTotal json parse attributes
                try:
                    vt_json_getstr = data_VirusTotal['data'].get('attributes')
                    vt_mal_score = str(vt_json_getstr.get('last_analysis_stats').get("malicious"))
                    vt_susp_score = str(vt_json_getstr.get('last_analysis_stats').get("suspicious"))
                    vt_undet_score = str(vt_json_getstr.get('last_analysis_stats').get("undetected"))
                    vt_hless_score = str(vt_json_getstr.get('last_analysis_stats').get("harmless"))
                    vt_comm_score = str(vt_json_getstr.get('reputation'))
                    vt_tot_score = int(vt_mal_score) + int(vt_susp_score) + int(vt_undet_score) + int(vt_hless_score)
                except:
                    self.labarradistato.emit("Error Code 5004 : invalid")
                    print("Error Code 5004 : invalid")
                    data_VirusTotal = "API out of limit"
                # GreyNoise json parse attributes
                try:
                    gn_reputation = str(data_GreyNoise['classification'])
                except:
                    gn_reputation = 'N\\A'
                # Pulsedive json parse attributes
                try:
                    pd_risk_rep = data_Pulsedive['risk']
                except:
                    pd_risk_rep = "N\\A"
                # Shodan json parse attributes
                try:
                    sh_open_ports = str(response_Shodan.get('ports', 'N\\A'))
                    for item in response_Shodan['data'] :
                        try :
                            base = item.get("cobalt_strike_beacon")
                            base = base.get('x64')
                            geturi = base.get('http-get.uri')
                            posturi = base.get('http-post.uri')
                            watermark = base.get('watermark')
                            sh_products = "http-get.uri: "+ geturi + "\nhttp-post.uri: " + posturi + "\nwatermark: " + str(watermark)
                            break
                        except :
                            sh_products = "N\\A"
                except:
                    sh_open_ports = "N\\A"
                    sh_products = "N\\A"
                    print("Error Code 5007 : invalid")
                # XForce json parse attributes
                try:
                    xforce_score = str(response_XForce['history'].pop()['score'])
                except:
                    xforce_score = "N\\A"
                # Meta json parse attributes
                try:
                    meta_risk = str(response_Meta['lookup_results'].get('detected_by'))
                except:
                    meta_risk = "N\\A"

                ###########      Output file      ###########
                # Write the output file
                # data = [IP, Country, Domain,ISP, Usage, Abuse, VT, X4se, Meta, GrNs, PulDv, VTCom, Shod]
                data = [
                    IP,
                    str(vt_json_getstr.get("country")),
                    str(abip_json_getstr.get("domain")),
                    str(abip_json_getstr.get("isp")),
                    str(abip_json_getstr.get("usageType")),
                    ab_score+"%",
                    vt_mal_score + "/" + str(vt_tot_score),
                    xforce_score,
                    meta_risk,
                    gn_reputation,
                    pd_risk_rep,
                    vt_comm_score,
                    sh_open_ports,
                    sh_products,
                    otx_urls
                ]

                prog_index = prog_index + 1
                self.printProgressBar(prog_index, len(self.lines), prefix = 'Progress:', suffix = 'Complete', length = 50)
                countryList.append(data[1])
                data.insert(5, txf.tirexfactor(data, Pulsedive_APIKEY))
                if bool_layt == "OLD":
                    for i in range(16):
                        self.tablesetter.emit(row,i,QTableWidgetItem(data[i]))
                else:
                    self.tablesetter.emit(0,0,data)
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
            print("INFO: Repxdbl7 completed.")
        except Exception as e:
            print('Error Code 4004: ' + str(e))
            self.labarradistato.emit('Error Code 4004: ' + str(e))
            self.finished.emit()
