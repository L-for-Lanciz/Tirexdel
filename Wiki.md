# How it works - Tirexdel Wiki

## IP Address
**Scope**: section to perform OSINT queries on IP addresses. <br />

Use the textbox to provide your input: you can pass a list of IP Addresses separated by a new line. <br />
Once you provide input data, that can even be defanged since Tirexdel will automatically handle brackets and parenthesis, you can launch the script by clicking on the search button. <br />

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


The Tirexfactor comes labeled according to the given threat of the IoC as: <br />

- Clean: (0%) no malicious activities have been detected for the given artifact. <br />
- Suspicious: (1-20%) some suspicious activity has been observed for the given artifact. <br />
- Risky: (21-50%) there are good chances that malicious activities have been performed from the given artifact. <br />
- Malicious: (51-75%) malicious activities have been for sure detected for the given artifact. <br />
- Threat: (76-100%) the artifact is known to be malicious. No doubts at all. <br />

Other information which are collected but not used to compute the arithmetic mean are: <br />
- from **AlienVault**: you can find a number which represents the number of **URLs observed** at the given IP address. This is really helpful to identify addresses used for web hosting, which can be considered as low confidence indicators.
- from **Shodan**: you can find two different information. The first one is about **Open Ports** exposed, as simply as that. The second one, is a deepening on **Cobalt Strike C2 hosting**. In case one should be hosted at the given IP address, related information will be provided together with core details about its configuration.

Lastly, a [whitelist](https://github.com/L-for-Lanciz/Tirexdel/blob/main/whitelist.ini) is applied for well known ISPs, to make you aware that the IoC may be a false positive. <br />
IP Addresses that match the whitelist are labeled as "FPALERT". <br />

Once the script has ended, you will be able to download an XLSX export by the proper button. <br />
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
**Scope**: section to perform OSINT queries over bulks of IP addresses, in particular if you need speed or if you have limited APIs. <br />

Once you provide your input, that can even be defanged since Tirexdel will automatically handle brackets and parenthesis, you can launch the script by clicking on the search button. <br />
Within this section, Tirexdel will query only AbuseIPDB, for a fast and light feedback. <br />
Once the script has ended, you will be able to download an XLSX export with the same information given in the table by the proper button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;AbuseIPDB <br />

&nbsp;

## Domain/URL
**Scope**: section to perform OSINT queries on Domains and URLs. <br />

Once you provide your input, that can even be defanged since Tirexdel will automatically handle hXXp, brackets and parenthesis, you can launch the script by clicking on the search button. <br />

The script will call VirusTotal Api and provide related reputation information for your input data. <br />

Another key functionality provided in this section is the "screenshot" option. <br />
This feature can be activated/disabled through its dedicated button located at the right of the search button. As you can guess, this <br />
If activated, the script will obtain - from Urlscan - a screenshot of every URL or Domain given as input and will be automatically stored in the "/screenshot" folder. <br />

Eventually, this section supports even AlienVault: by selecting one indicator from the table, you can use the AlienVault button to spawn a window with the relative artifact's page. <br />

Once the script has ended, you will be able to download an XLSX export by the proper button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;Urlscan <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;

&nbsp;

## File Hash
**Scope**: section to perform OSINT queries on File Hashes <br />

The script will call VirusTotal API and provide related reputation information for your input data. <br />
Once you provide your input, that can even be defanged since Tirexdel will automatically handle hXXp, brackets and parenthesis, you can launch the script by clicking on the search button. <br />
All the information retrieved is shown within the GUI in a table. <br />

Eventually, this section supports even AlienVault: by selecting one indicator from the table, you can use the AlienVault button to spawn a window with the relative artifact's page. <br />

Once the script has ended, you will be able to download an XLSX export by the proper button. <br />
&nbsp;

#### OSINT Sources
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;
