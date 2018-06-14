# aksPortScan
Basic Port Scan using python nmap library

How to use:

(1) Make sure python2 installed in your system.

(2) Install python-nmap

    pip install python-nmap or go to http://xael.org/norman/python/python-nmap/ (install for python2)

(2) Command -  python aksPortScan.py -H "IP of the Host" -p "Ports to scan(separated by comma)"

    Example - python aksPortScan.py -H 127.0.0.1 -p 21,22,443,80
    
    You can also give chmod u+x permission to run without typing python - ./aksPortScan.py
    
Versions:

v1(Current)

v1.1(under development)    
