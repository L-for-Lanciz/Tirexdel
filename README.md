# Tirexdel
![auicon](https://user-images.githubusercontent.com/74201903/230610673-cc5053d1-edaf-4130-8a81-a0498ac2eedd.png) <br />
&nbsp;

Tirexdel is an open source Intelligence (OSINT) security tool aimed to gather the major quantity and quality of OSINT information for the evalution of artifacts and indicators of compromise.
&nbsp;

&nbsp;

## Tirexdel in a Nutshell
**Automated OSINT analysis for indicators of compromise (IoCs), divided into:** <br />
&nbsp;&nbsp;&nbsp;&nbsp;• IP address: *[IP Address]* module for a deep analysis; [Troppip] module for speed analysis. <br />
&nbsp;&nbsp;&nbsp;&nbsp;• Domains/URLs: *[Domain/URL]* module. <br />
&nbsp;&nbsp;&nbsp;&nbsp;• File Hashes: *[File Hashes]* module for MD5, SHA1, SHA256. <br />
**Automated E-Mail analysis using OSINT and heuristic techniques**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;• *[Mailoctopus]* module <br />

&nbsp;

## Tirexdel Download
Here you can find the latest release. Have a nice time with your T-Rex.  

[Tirexdel v1.1.1 download](https://github.com/L-for-Lanciz/Tirexdel/releases/download/v1.1.1/Tirexdel.v1.1.1.zip)  

PE of the program with all the dependencies included, at its latest release!  
The GUI is based on PyQt6 (great love PyQt team! (even if you are a little buggy but never mind)). <br />
&nbsp;

## Execution
**1. Unzip your new favourite shiny dinosaur.**  

**2. Run the PE 'Tirexdel v_x.y_.exe'**  

**3. Configure your API Settings. Go to _"Settings"_ and:**  
  
&nbsp;&nbsp;&nbsp;&nbsp;Under _**"Preferences"**_:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• _Download Path_: paste the path in which you want to save your outputs. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• _SSL Cert Bypass_: set it to TRUE if you have issues with proxy. Let it to FALSE otherwise. <br />
   
&nbsp;&nbsp;&nbsp;&nbsp;Under _**"API Keys Settings"**_:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set your API keys to make your t-rex dancing.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Important**: VirusTotal and AbuseIPDB are mandatory. Every other API is just optional but recommended.  

**4. There you go! Execute your queries.**  
  
&nbsp;&nbsp;&nbsp;&nbsp;• **IP Address**: execute queries over IP addresses over all the OSINT sources listed below (if API keys are provided).  
&nbsp;&nbsp;&nbsp;&nbsp;• **Troppip**: execute queries on IP addresses only with AbuseIPDB. That's for huge lists of IP addresses or for a quick and dirty check.  
&nbsp;&nbsp;&nbsp;&nbsp;• **Domain/URL**: execute queries on domains and URLs. VirusTotal is implemented for data and reputation, Urlscan to gather screenshots. Plus an AlienVault feature.  
&nbsp;&nbsp;&nbsp;&nbsp;• **File Hash**: execute queries on MD5, SHA1 and SHA256. Only VirusTotal is implemented at the moment, plus an AlienVault feature.  
  
&nbsp;&nbsp;&nbsp;&nbsp;• **Mailoctopus**: a fully automated heuristic and OSINT E-Mail analysis module.  
&nbsp;

## OSINT Sources
**IP Address**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;*VirusTotal* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*AbuseIPDB* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*AlienVault* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*Shodan* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*IBM XForce* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*MetaDefender* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*GreyNoise* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*PulseDive* <br />
**Troppip**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;*AbuseIPDB* <br />
**Domain/URL**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;*VirusTotal* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*Urlscan* <br />
&nbsp;&nbsp;&nbsp;&nbsp;*APILayer Whois* <br />
**File Hash**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;*VirusTotal* <br />
&nbsp;

## How it works
To explore all the Tirexdel's functionalities and features, you can consult the official [Documentation](https://github.com/L-for-Lanciz/Tirexdel/blob/main/Documentation.md). <br />
&nbsp;

## Author
Project founder: <br />
Lorenzo Langeli [(LinkedIn)](https://it.linkedin.com/in/lorenzolangeli) <br />
&nbsp;

## Demo
[![Watch the video](https://img.youtube.com/vi/nF_0SmXdWaM/maxresdefault.jpg)](https://youtu.be/nF_0SmXdWaM)
