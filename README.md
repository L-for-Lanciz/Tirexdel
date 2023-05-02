# Tirexdel
**Tirexdel** OSINT: an open source project aimed to obtain the major quantity of OSINT possible for Indicator of Compromises.

![auicon](https://user-images.githubusercontent.com/74201903/230610673-cc5053d1-edaf-4130-8a81-a0498ac2eedd.png)


## Source
You can find the source code of the tool. Don't consider it professional coding. Barely consider it coding. But hey, it works!

## Tirexdel 2.8.7z

[Tirexdel 2.8.7z download](https://drive.google.com/file/d/1ZfmO-cYx2FpKe694wF3FoveW2xCSW1LV/view?usp=sharing)  

PE of the program with all the dependencies included, at its latest release!  
The GUI is based on PyQt6 (great love PyQt team! (even if you are a little buggy but never mind)).  

### Download
You just need the zipped folder (drive link just up there!).  
The source code is available but you don't need to download it to run the program.  

### Execution
1. Unzip your new favourite shiny t-rex.  
2. Run the PE 'Tirexdel 2.'x'.exe'  
3. Configure your API Settings. Go to Settings and:  
  
&nbsp;&nbsp;&nbsp;&nbsp;Under "Preferences":  
- Download Path: paste the path in which you want to save your outputs.
- SSL Cert Bypass: set it to TRUE if you have issues with proxy. Let it to FALSE otherwise.
- IP-Address Layout: layout for the 'IP Address' section. Set it to NEW, it's much cooler.
   
&nbsp;&nbsp;&nbsp;&nbsp;Under "API Keys Settings":  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set your API keys to make your t-rex dancing.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Important: VirusTotal and AbuseIPDB are mandatory. Every other api it's just optional but recommended.  

4. There you go! Execute your queries.  
  
&nbsp;&nbsp;&nbsp;&nbsp;**IP Address**: execute queries on IPs over all the listed OSINT sources (if API keys are provided).  
&nbsp;&nbsp;&nbsp;&nbsp;**Troppip**: execute queries on IPs only with the use of AbuseIPDB. That's for huge lists of IP addresses.  
&nbsp;&nbsp;&nbsp;&nbsp;**Domain/URL**: execute queries on domains and URLs. Only VirusTotal is supported at the moment.  
&nbsp;&nbsp;&nbsp;&nbsp;**File Hash**: execute queries on MD5, SHA1 and SHA256. Only VirusTotal is supported at the moment.  
  
&nbsp;&nbsp;&nbsp;&nbsp;**Triage Matrix**: an easy and basic way to assess new vulnerabilities.  
