#!/usr/bin/python3

import socket
import re
import sys
from subprocess import Popen,PIPE

def gethosts(interface):
	cmd ='arp-scan -interface='+interface+' --localnet'
	main = Popen(cmd,shell=True,stderr=PIPE,stdout=PIPE)
	scanhosts = main.stdout.read()+main.stderr.read()
	scanhosts = str(scanhosts)
	hosts=re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',scanhosts)
	if hosts:
		netip = '.'.join(hosts[0].split('.')[:-1])
		netids = []
		for host in hosts:
			netid = host.split('.')[-1]
			netid = int(netid)
			netids.append(netid)
		netids.sort()
		hosts = (netip, netids)
		return(hosts)
	else:
		return('No hosts found')


if __name__=='__main__':
	if len(sys.argv)>1:
                iface = str(sys.argv[1])
	else:
		iface = input('Interface: ')
	hosts = gethosts(iface)
	if 'No hosts found' in hosts:
		print(hosts)
	else:
		baseip, netips = hosts
		for ip in netips:
			print('.'.join((baseip, str(ip))))
