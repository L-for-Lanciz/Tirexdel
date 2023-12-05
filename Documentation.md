# Tirexdel Documentation
## IP Address
**Scope**: section for performing OSINT queries on IP addresses. <br />

Use the textbox to provide your input: you can pass a list of IP Addresses separated by a new line. <br />
Once you provide some input data, that can even be defanged since Tirexdel will automatically handle brackets and parenthesis, you can launch the script by clicking on the search button. <br />

The score from every Vendor is visible for each artifact. Plus, Tirexdel generates a Tirexfactor, which has to be considered as a weighted arithmetic mean. <br />

Every vendor has a different weight in the Tirexfactor final output. <br />
Here is an approximation*: <br />

- AbuseIPDB : 0.8
- VirusTotal : 1.1
- VTCommunity : 0.3
- Pulsedive : 0.4
- Greynoise : 0.4
- IBM XForce : 0.7
- MetaDefender : 0.8

*This is due to the fact that every Firm has its different scale. Data must be first normalized. <br />
The above weights have then been assigned according to the Author's experience with the reliability of the information gathered. <br />


The Tirexfactor comes labeled according to the given threat level of the IoC, as: <br />

- Clean: (0%) no malicious activities have been detected for the given artifact. <br />
- Suspicious: (1-20%) some suspicious activity has been observed for the given artifact. <br />
- Risky: (21-50%) possible malicious activities have been performed from the given artifact. <br />
- Malicious: (51-75%) malicious activities have been for sure detected for the given artifact. <br />
- Threat: (76-100%) the artifact is known to be malicious. No doubts at all. <br />

Other information which are collected but not used to compute the arithmetic mean are: <br />
- from **AlienVault**: you can find a number which represents the number of **URLs observed** at the given IP address. This is really helpful to identify addresses used for web hosting, which can be considered as low confidence indicators.
- from **Shodan**: you can find two different information. The first one is about **Open Ports** exposed, as simply as that. The second one, is a deepening on **Cobalt Strike C2 hosting**. In case one should be hosted at the given IP address, related information will be provided together with core details about its configuration.

Lastly, a [whitelist](https://github.com/L-for-Lanciz/Tirexdel/blob/main/whitelist.ini) is applied for well known ISPs, to make you aware that the IoC may be a false positive. <br />
IP Addresses that match the whitelist are labeled as "FPALERT". <br />

Once the script has ended, you will be able to download an XLSX export through the dedicated button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;AbuseIPDB <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;&nbsp;&nbsp;&nbsp;Shodan <br />
&nbsp;&nbsp;&nbsp;&nbsp;IBM XForce <br />
&nbsp;&nbsp;&nbsp;&nbsp;MetaDefender <br />
&nbsp;&nbsp;&nbsp;&nbsp;GreyNoise <br />
&nbsp;&nbsp;&nbsp;&nbsp;PulseDive <br />

&nbsp;

## Troppip
**Scope**: section for performing OSINT queries over bulks of IP addresses, in particular if you need speed or if you haven't configured all the APIs. <br />

Once you provide your input, that can even be defanged since Tirexdel will automatically handle brackets and parenthesis, you can launch the script by clicking on the search button. <br />
Within this section, Tirexdel will query only *AbuseIPDB*, for a fast and light feedback. <br />
Once the script has ended, you will be able to download an XLSX export, with the same information shown in the table, through the dedicated button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;AbuseIPDB <br />

&nbsp;

## Domain/URL
**Scope**: section for performing OSINT queries on Domains and URLs. <br />

Once you provide your input, that can even be defanged since Tirexdel will automatically handle hXXp, brackets and parenthesis, you can launch the script by clicking on the search button. <br />

The script will call VirusTotal Api and provide related reputation information for the input data. <br />
If an API key is provided, it will also fetch Whois data from Whoisjson. <br />

Another key functionality provided in this section is the "screenshot" option. <br />
This feature can be activated/disabled through its dedicated button located at the right of the search button. As you can guess, this <br />
If activated, the script will obtain - from Urlscan - a screenshot of every URL or Domain given as input and will be automatically stored in the "/screenshot" folder. <br />

Eventually, this section provides you a *"Auto submit unknowns"* button, that allows you to opt to automatically submit URLs that are actually unknown to VirusTotal, by actually requesting a live scan, as this is not the default behaviour. <br />
*Note: a deep scan that request both screenshot and auto-submit will take longer than a simple scan. That's why it's up to your choice: just be patient in case.*

Once the script has ended, you will be able to download an XLSX export through the dedicated button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;Urlscan <br />
&nbsp;&nbsp;&nbsp;&nbsp;APILayer Whois <br />
&nbsp;

## File Hash
**Scope**: section for performing OSINT queries on File Hashes <br />

The script will call VirusTotal API and provide related reputation information for the input data. <br />
Once you provide your input, that can even be defanged since Tirexdel will automatically handle hXXp, brackets and parenthesis, you can launch the script by clicking on the search button. <br />
All the information retrieved is shown within the GUI in a table. <br />

Eventually, this section supports even AlienVault: by selecting one indicator from the table, you can use the AlienVault button to spawn a window with the relative artifact's page. <br />

Once the script has ended, you will be able to download an XLSX export through the dedicated button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;

&nbsp;

## MailOctopus
**Scope**: section for performing a fully automated heuristic and OSINT analysis on input provided E-Mail. <br />

By providing an email as an input for the script, it will automatically procede with data exctraction and parsing of its details and network/host artifacts. <br />
In this first stage, all of the analysis is made client-side without any API activity. That means that you have no reason to worry about data privacy.
The email data will be disposed in three groups: left, central and right. <br />
&nbsp;

On the **left**, you will find the header of the email in 3 different views: <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'Significant header details'*. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'Parsed (all) headers details'*. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'Raw header'*. <br />
&nbsp;

At the **center**, you will find: <br />
&nbsp;&nbsp;&nbsp;&nbsp;the *'subject'* of the email. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'sender', 'from, 'cc', 'date'* details. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*three shield icons* one for each of 'DKIM', 'DMARC' and 'SPF' email security protocols. A green shield means that the signature is verified; the grey shield means that it was not possible to verify the signature (probably missing); the red shield means that the signature is NOT verified. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*Attachments* of the email, in case of any. <br />
&nbsp;

On the **right**, you will find the network artifacts extracted from the email, that include the ones found in the body, and the sender IP address and domain: <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'IP addresses found'* inside the email body; and the sender IP address from the header. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'Domains found'* inside the email body; and the sender domain from the header. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'URLs found'* inside the email body. <br />
&nbsp;&nbsp;&nbsp;&nbsp;*'Email addresses found'* inside the email body. <br />
&nbsp;

At the very top of the screen you have three main buttons: <br />
&nbsp;&nbsp;&nbsp;&nbsp;**'New analysis'** . <br />
&nbsp;&nbsp;&nbsp;&nbsp;**'Generate a PDF Report'** . <br />
&nbsp;&nbsp;&nbsp;&nbsp;**'OSINT analysis'**. <br />
&nbsp;
