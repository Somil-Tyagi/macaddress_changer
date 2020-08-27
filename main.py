#!/usr/bin/env python3
import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Adding interface to change its Mac Address')
    parser.add_option('-m', '--mac', dest='mac_add', help='Enter Your New Mac Address')
    (value, arguments) = parser.parse_args()

    if not value.interface:
        parser.error("please specify interface, use --help for more information")

    if not value.mac_add:
        parser.error("please specify new mac address, use --help for more information")

    return value


def mac_change(interface, mac_add):
    print(f'[+] Changing The Interface {interface} to new mac address {mac_add}')
    subprocess.call('ifconfig ' + interface + ' down', shell=True)
    subprocess.call('ifconfig ' + interface + ' hw ether ' + mac_add, shell=True)
    subprocess.call('ifconfig ' + interface + ' up ', shell=True)


options = get_arguments()

mac_change(options.interface, options.mac_add)
