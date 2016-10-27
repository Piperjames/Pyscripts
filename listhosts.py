#!/usr/bin/python3

import socket
from sys import argv
import nmap

def gethosts(inet):
    nm = nmap.PortScanner()
    scanr = nm.scan(hosts=inet, arguments='-sP', sudo=True)
    ips = list(scanr['scan'])
    hosts = []
    netids = []
    for host in ips:
        if (scanr['scan'][host]['status']['state'] == 'up'):
            hosts.append(host)
    if hosts:
        netip = '.'.join(hosts[0].split('.')[:-1])
        for host in hosts:
            netid = host.split('.')[-1]
            netid = int(netid)
            netids.append(netid)
        netids.sort()
        hosts = (netip, netids)
        return(hosts)
    else:
        return('No hosts found')

if __name__ == "__main__":
    if len(argv):
        iface = str(argv[1])
    else:
        iface = input('Interface: ')
    hosts = gethosts(iface)
    if 'No hosts found' in hosts:
        print(hosts)
        exit(0)
    else:
        baseip, netips = hosts
        for ip in netips:
            print('.'.join((baseip, str(ip))))

