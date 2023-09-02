# Tirexdel
![auicon](https://user-images.githubusercontent.com/74201903/230610673-cc5053d1-edaf-4130-8a81-a0498ac2eedd.png)
&nbsp;

&nbsp;

Tirexdel is an opensource Intelligence (OSINT) security tool aimed to gather the major quantity and quality of OSINT information for the evalution of artifacts and indicators of compromise.
&nbsp;

&nbsp;

## Source
You can find the source code of the tool. Don't consider it professional coding, but hey, it works!  
The tool is still under development (more or less active).
&nbsp;

## Tirexdel Download
You just need the zipped executable. The source code is available but you don't need it to run the program.

[Tirexdel 2.8 download](https://github.com/L-for-Lanciz/Tirexdel/releases/download/v2.8.0/Tirexdel.2.8.zip)  

PE of the program with all the dependencies included, at its latest release!  
The GUI is based on PyQt6 (great love PyQt team! (even if you are a little buggy but never mind)).  
The executable has been packed with UPX.
&nbsp;

## Execution
**1. Unzip your new favourite shiny dinosaur.**  
**2. Run the PE 'Tirexdel 2.'x'.exe'**  
**3. Configure your API Settings. Go to Settings and:**  
  
&nbsp;&nbsp;&nbsp;&nbsp;Under "Preferences":  
- Download Path: paste the path in which you want to save your outputs.
- SSL Cert Bypass: set it to TRUE if you have issues with proxy. Let it to FALSE otherwise.
- IP-Address Layout: layout for the 'IP Address' section. Set it to NEW, it's much cooler.
   
&nbsp;&nbsp;&nbsp;&nbsp;Under "API Keys Settings":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set your API keys to make your t-rex dancing.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Important: VirusTotal and AbuseIPDB are mandatory. Every other API is just optional but recommended.  

**4. There you go! Execute your queries.**  
  
&nbsp;&nbsp;&nbsp;&nbsp;**IP Address**: execute queries over IP addresses over all the listed (below) OSINT sources (if API keys are provided).  
&nbsp;&nbsp;&nbsp;&nbsp;**Troppip**: execute queries on IP addresses only with the use of AbuseIPDB. That's for huge lists of IP addresses.  
&nbsp;&nbsp;&nbsp;&nbsp;**Domain/URL**: execute queries on domains and URLs. Only VirusTotal is implemented at the moment, plus an AlienVault feature.  
&nbsp;&nbsp;&nbsp;&nbsp;**File Hash**: execute queries on MD5, SHA1 and SHA256. Only VirusTotal is implemented at the moment, plus an AlienVault feature.  
  
&nbsp;&nbsp;&nbsp;&nbsp;**Triage Matrix**: an easy way to assess new vulnerabilities.  
&nbsp;

## OSINT Sources
**IP Address**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;AbuseIPDB <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;&nbsp;&nbsp;&nbsp;Shodan <br />
&nbsp;&nbsp;&nbsp;&nbsp;IBM XForce <br />
&nbsp;&nbsp;&nbsp;&nbsp;MetaDefender <br />
&nbsp;&nbsp;&nbsp;&nbsp;GreyNoise <br />
&nbsp;&nbsp;&nbsp;&nbsp;PulseDive <br />
**Troppip**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;AbuseIPDB <br />
**Domain/URL**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
**File Hash**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;

## How it works
### IP Address Section
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

Lastly, a [whitelist](https://github.com/L-for-Lanciz/Tirexdel/blob/main/whitelist.ini) is applied for well known ISPs, to make you aware that the IoC may be a false positive. <br />
IP Addresses that match the whitelist are labeled as "FPALERT". <br />

&nbsp;

## Author
Project founder: <br />
Lorenzo Langeli [(LinkedIn)](https://it.linkedin.com/in/lorenzolangeli)
&nbsp;

&nbsp;

## Demos
### IP Address
https://github.com/L-for-Lanciz/Tirexdel/assets/74201903/38da642a-e3f2-4db0-ac0b-2afb03bd19d6

### File Hash
https://github.com/L-for-Lanciz/Tirexdel/assets/74201903/6cff234b-560b-42af-a1e1-cfa3147d4038
