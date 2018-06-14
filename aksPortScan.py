#!/usr/bin/env python
#Akshay Singh
#Basic port scan that uses nmap python library

import optparse
import nmap
import sys

def nmapScan(userHost,userPort): #to start nmap port scan
    try:
        nmScanner = nmap.PortScanner()
        nmScanner.scan(userHost, userPort)
        portState = nmScanner[userHost]['tcp'][int(userPort)]['state']
        portVersion = nmScanner[userHost]['tcp'][int(userPort)]['version']
        portName = nmScanner[userHost]['tcp'][int(userPort)]['name']
        portExtraInfo = nmScanner[userHost]['tcp'][int(userPort)]['extrainfo']
        portProduct = nmScanner[userHost]['tcp'][int(userPort)]['product']
        print("Scanning Port: " + userPort)
        print("[+] State: " + portState + " | Name: "+portName+" | Version: "+portVersion+" | Extra Info: "+portExtraInfo + " | Product: "+portProduct )
    except:
        print("Error: Try again, make sure the host is active", sys.exc_info()[0])
        sys.exit(0)

def main(): #to set up parser and call nmapScan()
    parser = optparse.OptionParser('usage -H '+ '<target Host> -p <target Port>')
    parser.add_option('-H', dest='userHost', type='string', help='specify target host')
    parser.add_option('-p', dest='userPort', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    userHost = options.userHost
    userPort = str(options.userPort).split(',')
    if(userHost == None) | (userPort[0] == None):
        print(parser.usage)
        exit(0)
    for p in userPort:
        nmapScan(userHost,p)

if __name__=="__main__":
    main()


