#!/usr/bin/env python3

import xlsxwriter
from configparser import ConfigParser
import time

def exportToXl(data, typeofquery) :
    cfg = ConfigParser()
    cfg.read('config/config.ini')
    # Create XLSX header
    rand = str(round(time.time() * 1000))
    export_file = '/txd_results_' + rand[-7:-1] + '.xlsx'
    workbook = xlsxwriter.Workbook(cfg.get('settings','downloadto')+export_file)
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})
    r=1
    if typeofquery == 1:
        #IP Worksheet
        worksheet.write('A1', 'IP address', bold)
        worksheet.write('B1', 'Country', bold)
        worksheet.write('C1', 'Domain', bold)
        worksheet.write('D1', 'ISP', bold)
        worksheet.write('E1', 'UsageType', bold)
        worksheet.write('F1', 'Tirexfactor', bold)
        worksheet.write('G1', 'AbuseIPDB', bold)
        worksheet.write('H1', 'VirusTotal', bold)
        worksheet.write('I1', 'IBM XForce', bold)
        worksheet.write('J1', 'MetaDefender', bold)
        worksheet.write('K1', 'GreyNoise', bold)
        worksheet.write('L1', 'Pulsedive', bold)
        worksheet.write('M1', 'VTCommunity', bold)
        worksheet.write('N1', 'Shodan openPorts', bold)
        worksheet.write('O1', 'Shodan CSBeacon', bold)
        worksheet.write('P1', 'Hosted URLs', bold)
        #iteration
        for single in data :
            for j in range(5) :
               worksheet.write(r, j, single[j])
            formatCellsIP(workbook,worksheet,r,single[5],single[6],single[7],single[8],single[9],single[10],single[11],single[12])
            worksheet.write(r, 13, single[13])
            worksheet.write(r, 14, single[14])
            worksheet.write(r, 15, single[15])
            r = r+1
    elif typeofquery == 2:
        #URL Worksheet
        worksheet.write('A1', 'URL', bold)
        worksheet.write('B1', 'Reputation', bold)
        worksheet.write('C1', 'Community', bold)
        worksheet.write('D1', 'Times submitted', bold)
        worksheet.write('E1', 'Passive DNS', bold)
        worksheet.write('F1', 'Kaspersky', bold)
        worksheet.write('G1', 'BitDefender', bold)
        worksheet.write('H1', 'Sophos', bold)
        #iteration
        for single in data :
            worksheet.write(r, 0, single[0])
            worksheet.write(r, 3, single[3])
            worksheet.write(r, 4, single[4])
            worksheet.write(r, 5, single[5])
            worksheet.write(r, 6, single[6])
            worksheet.write(r, 7, single[7])
            formatCellsURLs(workbook,worksheet,r,single[1],single[2])
            r = r+1
    elif typeofquery == 3:
        #Hash Worksheet
        worksheet.write('A1', 'File Hash', bold)
        worksheet.write('B1', 'Reputation', bold)
        worksheet.write('C1', 'Community', bold)
        worksheet.write('D1', 'Product', bold)
        worksheet.write('E1', 'Signer', bold)
        worksheet.write('F1', 'Description', bold)
        #iteration
        for single in data :
            worksheet.write(r, 0, single[0])
            worksheet.write(r, 3, single[3])
            worksheet.write(r, 4, single[4])
            worksheet.write(r, 5, single[5])
            formatCellsURLs(workbook,worksheet,r,single[1],single[2])
            r = r+1
    elif typeofquery == 4:
        #IP Worksheet
        worksheet.write('A1', 'IP address', bold)
        worksheet.write('B1', 'Country', bold)
        worksheet.write('C1', 'Domain', bold)
        worksheet.write('D1', 'ISP', bold)
        worksheet.write('E1', 'UsageType', bold)
        worksheet.write('F1', 'LastReported', bold)
        worksheet.write('G1', 'AbuseIPDB', bold)
        #iteration
        for single in data:
            for j in range(6):
               worksheet.write(r, j, single[j])
            formatCellsTip(workbook,worksheet,r,single[6])
            r = r+1
    workbook.close()
    return True

# Define function to format cells according to data
def formatCellsIP(workbook,worksheet,row,txf,f,g,h,i,j,k,l) :
    # set cell formats
    cf_TL0 = workbook.add_format({'bold':True, 'bg_color':'#34eb49'})
    cf_TL1 = workbook.add_format({'bold':True, 'bg_color':'#e3fc03'})
    cf_TL2 = workbook.add_format({'bold':True, 'bg_color':'#ebd834'})
    cf_TL3 = workbook.add_format({'bold':True, 'bg_color':'#ebae34'})
    cf_TL4 = workbook.add_format({'bold':True, 'bg_color':'#c42727'})
    cf_TL5 = workbook.add_format({'bold':True, 'bg_color':'#800000'})
    # format data to perform checks
    ff = int(f.replace('%',''))
    gg = g.split("/", 1)
    gg = int(gg[0])
    l = int(l)
    # tirexfactor rep
    if 'Threat' in txf :
        worksheet.write(row, 5, txf, cf_TL5)
    elif 'Malicious' in txf :
        worksheet.write(row, 5, txf, cf_TL4)
    elif 'Risky' in txf :
        worksheet.write(row, 5, txf, cf_TL3)
    elif 'Suspicious' in txf :
        worksheet.write(row, 5, txf, cf_TL2)
    else :
        worksheet.write(row, 5, txf, cf_TL0)
    # abuse reputation
    if ff >= 90 :
        worksheet.write(row, 6, f, cf_TL5)
    elif ff >= 70 :
        worksheet.write(row, 6, f, cf_TL4)
    elif ff >= 50 :
        worksheet.write(row, 6, f, cf_TL3)
    elif ff > 25 :
        worksheet.write(row, 6, f, cf_TL2)
    elif ff > 0 :
        worksheet.write(row, 6, f, cf_TL1)
    else :
        worksheet.write(row, 6, f, cf_TL0)
    # virustotal reputation
    if gg >= 10 :
        worksheet.write(row, 7, g, cf_TL5)
    elif gg >= 6 :
        worksheet.write(row, 7, g, cf_TL4)
    elif gg >= 4 :
        worksheet.write(row, 7, g, cf_TL3)
    elif gg >= 1 :
        worksheet.write(row, 7, g, cf_TL2)
    else :
        worksheet.write(row, 7, g, cf_TL0)
    # vtcommunity reputation
    if l <= -14 :
        worksheet.write(row, 12, l, cf_TL5)
    elif l <= -10 :
        worksheet.write(row, 12, l, cf_TL4)
    elif l <= -6 :
        worksheet.write(row, 12, l, cf_TL3)
    elif l <= -3 :
        worksheet.write(row, 12, l, cf_TL2)
    elif l < 0 :
        worksheet.write(row, 12, l, cf_TL1)
    else :
        worksheet.write(row, 12, l, cf_TL0)
    # greynoise reputation
    if j == 'malicious' :
        worksheet.write(row, 10, j, cf_TL4)
    else :
        worksheet.write(row, 10, j, cf_TL0)
    # pulsedive reputation
    if k == 'low' :
        worksheet.write(row, 11, k, cf_TL2)
    elif k == 'medium' :
        worksheet.write(row, 11, k, cf_TL3)
    elif k == 'high' :
        worksheet.write(row, 11, k, cf_TL4)
    else :
        worksheet.write(row, 11, k, cf_TL0)
    # xforce reputation
    try :
        h = float(h)
        hh = str(h)+'/10'
        if h >= 8 :
            worksheet.write(row, 8, hh, cf_TL5)
        elif h >= 6 :
            worksheet.write(row, 8, hh, cf_TL4)
        elif h >= 4:
            worksheet.write(row, 8, hh, cf_TL3)
        elif h >= 2:
            worksheet.write(row, 8, hh, cf_TL2)
        else :
            worksheet.write(row, 8, hh, cf_TL0)
    except :
        worksheet.write(row, 8, 'N\\A')
    # metadefender risk
    try :
        i = int(i)
        if i >= 7 :
            worksheet.write(row, 9, i, cf_TL5)
        elif i >= 4 :
            worksheet.write(row, 9, i, cf_TL4)
        elif i >= 2 :
            worksheet.write(row, 9, i, cf_TL3)
        elif i == 1 :
            worksheet.write(row, 9, i, cf_TL2)
        else :
            worksheet.write(row, 9, i, cf_TL0)
    except :
        worksheet.write(row, 9, 'N\\A')

def formatCellsHashes(workbook,worksheet,row,g,h) :
    # if results are N\A don't execute
    if g=='N\A' and h=='N\A':
        worksheet.write(row,1,'N\A')
        worksheet.write(row, 2, 'N\A')
        return
    # set cell formats
    cf_TL0 = workbook.add_format({'bold':True, 'bg_color':'#34eb49'})
    cf_TL1 = workbook.add_format({'bold':True, 'bg_color':'#e3fc03'})
    cf_TL2 = workbook.add_format({'bold':True, 'bg_color':'#ebd834'})
    cf_TL3 = workbook.add_format({'bold':True, 'bg_color':'#ebae34'})
    cf_TL4 = workbook.add_format({'bold':True, 'bg_color':'#c42727'})
    cf_TL5 = workbook.add_format({'bold':True, 'bg_color':'#800000'})
    # format data to perform checks
    gg = g.split("/", 1)
    gg = int(gg[0])
    h = int(h)
    # virustotal reputation
    if gg >= 10 :
        worksheet.write(row, 1, g, cf_TL5)
    elif gg >= 6 :
        worksheet.write(row, 1, g, cf_TL4)
    elif gg >= 4 :
        worksheet.write(row, 1, g, cf_TL3)
    elif gg >= 1 :
        worksheet.write(row, 1, g, cf_TL2)
    else :
        worksheet.write(row, 1, g, cf_TL0)
    # vtcommunity reputation
    if h <= -14 :
        worksheet.write(row, 2, h, cf_TL5)
    elif h <= -10 :
        worksheet.write(row, 2, h, cf_TL4)
    elif h <= -6 :
        worksheet.write(row, 2, h, cf_TL3)
    elif h <= -3 :
        worksheet.write(row, 2, h, cf_TL2)
    elif h < 0 :
        worksheet.write(row, 2, h, cf_TL1)
    else :
        worksheet.write(row, 2, h, cf_TL0)

def formatCellsURLs(workbook,worksheet,row,g,h) :
    # if results are N\A don't execute
    if g=='N\A' and h=='N\A':
        worksheet.write(row,1,'N\A')
        worksheet.write(row, 2, 'N\A')
        return
    # set cell formats
    cf_TL0 = workbook.add_format({'bold':True, 'bg_color':'#34eb49'})
    cf_TL1 = workbook.add_format({'bold':True, 'bg_color':'#e3fc03'})
    cf_TL2 = workbook.add_format({'bold':True, 'bg_color':'#ebd834'})
    cf_TL3 = workbook.add_format({'bold':True, 'bg_color':'#ebae34'})
    cf_TL4 = workbook.add_format({'bold':True, 'bg_color':'#c42727'})
    cf_TL5 = workbook.add_format({'bold':True, 'bg_color':'#800000'})
    # format data to perform checks
    gg = g.split("/", 1)
    gg = int(gg[0])
    h = int(h)
    # virustotal reputation
    if gg >= 10 :
        worksheet.write(row, 1, g, cf_TL5)
    elif gg >= 6 :
        worksheet.write(row, 1, g, cf_TL4)
    elif gg >= 4 :
        worksheet.write(row, 1, g, cf_TL3)
    elif gg >= 1 :
        worksheet.write(row, 1, g, cf_TL2)
    else :
        worksheet.write(row, 1, g, cf_TL0)
    # vtcommunity reputation
    if h <= -14 :
        worksheet.write(row, 2, h, cf_TL5)
    elif h <= -10 :
        worksheet.write(row, 2, h, cf_TL4)
    elif h <= -6 :
        worksheet.write(row, 2, h, cf_TL3)
    elif h <= -3 :
        worksheet.write(row, 2, h, cf_TL2)
    elif h < 0 :
        worksheet.write(row, 2, h, cf_TL1)
    else :
        worksheet.write(row, 2, h, cf_TL0)

# Define function to format cells according to data
def formatCellsTip(workbook,worksheet,row,f) :
    # set cell formats
    cf_TL0 = workbook.add_format({'bold':True, 'bg_color':'#34eb49'})
    cf_TL1 = workbook.add_format({'bold':True, 'bg_color':'#e3fc03'})
    cf_TL2 = workbook.add_format({'bold':True, 'bg_color':'#ebd834'})
    cf_TL3 = workbook.add_format({'bold':True, 'bg_color':'#ebae34'})
    cf_TL4 = workbook.add_format({'bold':True, 'bg_color':'#c42727'})
    cf_TL5 = workbook.add_format({'bold':True, 'bg_color':'#800000'})
    # format data to perform checks
    ff = int(f.replace('%',''))
    # abuse reputation
    if ff >= 90 :
        worksheet.write(row, 6, f, cf_TL5)
    elif ff >= 70 :
        worksheet.write(row, 6, f, cf_TL4)
    elif ff >= 50 :
        worksheet.write(row, 6, f, cf_TL3)
    elif ff > 25 :
        worksheet.write(row, 6, f, cf_TL2)
    elif ff > 0 :
        worksheet.write(row, 6, f, cf_TL1)
    else :
        worksheet.write(row, 6, f, cf_TL0)
