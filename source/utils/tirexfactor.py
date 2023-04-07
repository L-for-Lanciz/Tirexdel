#!/usr/bin/env python3

def tirexfactor(data, pdkey) :
    #assign
    abuseipdb = data[5]
    virustotal = data[6]
    xforce = data[7]
    meta = data[8]
    greynoise = data[9]
    pulsedive = data[10]
    vtcommunity = data[11]
    divideFactor = 0

    #reformat
    try :
        abuseipdb = int(abuseipdb.replace('%',''))
        divideFactor = divideFactor+0.8
    except :
        abuseipdb = 0
        print('Error Code 71001')
    try :
        virustotal_tmp = virustotal.split('/')
        virustotal = virustotal_tmp[0]
        divideFactor = divideFactor+1
    except :
        virustotal = 0
        print('Error Code 71001')
    try :
        vtcommunity = int(vtcommunity)*0.3
        divideFactor = divideFactor+0.3
    except :
        vtcommunity = 0
        print('Error Code 71001')
    try :
        xforce = (int(xforce)-1)*11
        divideFactor = divideFactor+0.7
    except :
        xforce = 0
        print('Error Code 71001')
    try :
        meta = int(meta)*10
        divideFactor = divideFactor+0.8
    except :
        meta = 0
        print('Error Code 71001')
    if greynoise.lower() == 'malicious' :
        greynoise = 40
    else :
        greynoise = 0
    divideFactor = divideFactor+0.4
    try :
        if pulsedive.lower() == 'high' :
            pulsedive = 40
        elif pulsedive.lower() == 'medium' :
            pulsedive = 20
        elif pulsedive.lower() == 'low' :
            pulsedive = 10
        else :
            pulsedive = 0
        if len(pdkey) > 60 :
            divideFactor = divideFactor+0.4
    except :
        print('Error Code 71001')
        pulsedive = 0

        '''
        Average algorythm
        - AbuseIPDB : 0.8           - VirusTotal : 1.0
        - VTCommunity : 0.3         - Pulsedive : 0.4
        - Greynoise : 0.4           - IBM XForce : 0.7
        - MetaDefender : 0.8
        '''

    tirexfactor = float(abuseipdb)*0.8 + int(virustotal)*11 - float(vtcommunity) + int(greynoise) + int(pulsedive) + xforce*0.7 + meta*0.8
    tirexfactor = round(tirexfactor/divideFactor, 2)
    if tirexfactor > 100 :
        tirexfactor = 100
        reputation = 'Threat'
    elif tirexfactor > 75 :
        reputation = 'Threat'
    elif tirexfactor > 50 :
        reputation = 'Malicious'
    elif tirexfactor > 20 :
        reputation = 'Risky'
    elif tirexfactor > 0 :
        reputation = 'Suspicious'
    elif tirexfactor <= 0 :
        reputation = 'Clean'
        tirexfactor = 0

    #fixed whitelists
    # if google/mcsft/amazon/etc. + add ⚠
    with open('config/whitelist.ini') as f:      # potrebbe rompersi con lista lunga (quanto?)
        if data[3] in f.read() :
            tirexfactor = "⚠FPAlert" + ' [' + str(tirexfactor) + '%]'
        else :
            tirexfactor = reputation + ' [' + str(tirexfactor) + '%]'
    #custom blacklists
    # if russian/chinese/etc.
    return tirexfactor
