# Nmap Scanner
Nmap(Network Mapper) is a security scanner, used to discover hosts and services on a computer network, thereby building a map of the network. To accomplish its goal, Nmap sends specially crafted packets to the target host(s) and then analyzes their responses.

## Prerequisites

This requires installing nmap in our local machine.
1. If you're using Linux, then use:
```
sudo apt-get install nmap
```
This is for Ubuntu.  

2. If you're using Windows, then download nmap from this [link](https://nmap.org/download.html).


```
pip install python-nmap
```

## Understanding the code

![image](https://raw.githubusercontent.com/HarshCasper/Rotten-Scripts/09359d3c6bc96388240f48469e90c7897cdc56a6/NMap%20Scanner/carbon.png)

```
>>> import nmap
```
If you're familiar with Python, you will know this line of code, that it imports the modules, here we've imported nmap module to our Python script. Then we initialise the Nmap PortScanner to scan the ports on our local network.

```
>>> nmScan.scan('127.0.0.1', '21-443')
```
This line of code will return a dictionary of the scan, which is executed on localhost i.e. 127.0.0.1, for port numbers 21 to 443.
An alternative way to scan is that, you can also provide the IP address of any remote server as well, to scan the available ports.

```
>>> nmScan['127.0.0.1'].hostname()
```
To scan the hostname of our laptop, we can use this.