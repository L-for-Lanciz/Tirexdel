# Tirexdel
![auicon](https://user-images.githubusercontent.com/74201903/230610673-cc5053d1-edaf-4130-8a81-a0498ac2eedd.png) <br />
&nbsp;

Tirexdel is an opensource Intelligence (OSINT) security tool aimed to gather the major quantity and quality of OSINT information for the evalution of artifacts and indicators of compromise.
&nbsp;

&nbsp;

## Tirexdel Download
You just need the zipped executable. Don't consider it professional coding, but hey, it works!  

[Tirexdel v1.0.0 download](https://github.com/L-for-Lanciz/Tirexdel/releases/tag/v1.0.0)  

PE of the program with all the dependencies included, at its latest release!  
The GUI is based on PyQt6 (great love PyQt team! (even if you are a little buggy but never mind)).  
The executable has been packed with UPX. <br />
&nbsp;

## Execution
**1. Unzip your new favourite shiny dinosaur.**  

**2. Run the PE 'Tirexdel v_x.y_.exe'**  

**3. Configure your API Settings. Go to _"Settings"_ and:**  
  
&nbsp;&nbsp;&nbsp;&nbsp;Under _**"Preferences"**_:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• _Download Path_: paste the path in which you want to save your outputs. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• _SSL Cert Bypass_: set it to TRUE if you have issues with proxy. Let it to FALSE otherwise. <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• _IP-Address Layout_: layout for the 'IP Address' section. Set it to NEW, it's much cooler. <br />
   
&nbsp;&nbsp;&nbsp;&nbsp;Under _**"API Keys Settings"**_:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set your API keys to make your t-rex dancing.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Important**: VirusTotal and AbuseIPDB are mandatory. Every other API is just optional but recommended.  

**4. There you go! Execute your queries.**  
  
&nbsp;&nbsp;&nbsp;&nbsp;• **IP Address**: execute queries over IP addresses over all the OSINT sources listed below (if API keys are provided).  
&nbsp;&nbsp;&nbsp;&nbsp;• **Troppip**: execute queries on IP addresses only with AbuseIPDB. That's for huge lists of IP addresses or for a quick and dirty check.  
&nbsp;&nbsp;&nbsp;&nbsp;• **Domain/URL**: execute queries on domains and URLs. VirusTotal is implemented for data and reputation, Urlscan to gather screenshots. Plus an AlienVault feature.  
&nbsp;&nbsp;&nbsp;&nbsp;• **File Hash**: execute queries on MD5, SHA1 and SHA256. Only VirusTotal is implemented at the moment, plus an AlienVault feature.  
  
&nbsp;&nbsp;&nbsp;&nbsp;• **Triage Matrix**: an easy way to assess new vulnerabilities.  
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
&nbsp;&nbsp;&nbsp;&nbsp;Urlscan <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;&nbsp;&nbsp;&nbsp;Whoisjson <br />
**File Hash**: <br />
&nbsp;&nbsp;&nbsp;&nbsp;VirusTotal <br />
&nbsp;&nbsp;&nbsp;&nbsp;AlienVault <br />
&nbsp;

## How it works
To explore all the Tirexdel's functionalities and features, you can consult the official [WIKI](https://github.com/L-for-Lanciz/Tirexdel/blob/main/Wiki.md). <br />
&nbsp;

## Author
Project founder: <br />
Lorenzo Langeli [(LinkedIn)](https://it.linkedin.com/in/lorenzolangeli) <br />
&nbsp;

## Demos
### IP Address
https://github.com/L-for-Lanciz/Tirexdel/assets/74201903/df4d3e33-2b09-438b-8fd8-a4e35b933a02


### File Hash
https://github.com/L-for-Lanciz/Tirexdel/assets/74201903/fbd371d4-7b3a-4f72-b955-4cc430e686e1


