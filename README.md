# macaddress_changer
mac address_changer is a script designes to change your mac address of the machine, it will help you a lot of time in case you are a pentester :-)


JUST CLONE MY SCRIPT AND ITS AS SIMPLE AS THAT, YOU HAVE TO RUN IN PYTHON 3 , MAKE SURE YOU HAVE DOWNLOADED PYTHON3 PACKAGE AND RUN THE FOLLOWING COMMAND IN ORDER TO CHANGE THE MAC ADDRESS

python3 main.py -i "interface" -m "new_mac_address" 

Here i is the interface of which you have to change your mac address either it can be eth0 or wlan0 to know the interface , run the following command in the terminal
ifconfig

example for the following command 

python3 main.py -i eth0 -m 00:11:22:33:44:55
and thats it your new mac address will be 00:11:22:33:44:55

to know more about the script you can add help option like

python3 main.py -h or python3 main.py --help
