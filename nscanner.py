#!/usr/bin/python3
#vim: set fileencoding=<UTF-8>

from hostscanner import gethosts, hostinfo
from sys import argv
import os

def main():
    if len(argv) == 3:
        iface = argv[1]
        fast = argv[2]
        hosts = gethosts(iface)
        baseip, netips = hosts
        options = (True, False)
        for ip in netips:
            if fast in options:
                hostinfo(('.'.join((baseip, str(ip)), fast)))
            else:
                hostinfo('.'.join((baseip, str(ip))))

    elif len(argv) == 2:
        iface = argv[1]
        hosts = gethosts(iface)
        baseip, netips = hosts
        for ip in netips:
            hostinfo('.'.join((baseip, str(ip))))
    else:
        iface = str(input('Enter Interface: '))
        hosts = gethosts(iface)
        baseip, netips = hosts
        for ip in netips:
            hostinfo('.'.join((baseip, str(ip))))

if __name__ == '__main__':
    if os.geteuid() != 0:
        print('This scripts needs to be run as root')
    else:
        main()
