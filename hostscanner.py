#!/usr/bin/python3

import socket
import re
import sys
from subprocess import Popen, PIPE
import nmap

def gethosts(interface):
    cmd = 'arp-scan -interface='+interface+' --localnet'
    prompt = Popen(cmd, shell=True, stderr=PIPE, stdout=PIPE)
    scanhosts = prompt.stdout.read()+prompt.stderr.read()
    scanhosts = str(scanhosts)
    hosts = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', scanhosts)
    if hosts:
        netip = '.'.join(hosts[0].split('.')[:-1])
        netids = []
        for host in hosts:
            netid = host.split('.')[-1]
            netid = int(netid)
            netids.append(netid)
        netids.sort()
        del netids[0]
        hosts = (netip, netids)
        return(hosts)
    else:
        return('No hosts found')


def hostinfo(host, fast=False):
    nm = nmap.PortScanner()
    if fast:
        try:
            nm.scan(hosts=host, arguments='-T4 -F', sudo=True)
            print('-'*30)
            print('Host : %s State : %s'%(host, nm[host]['status']['state']))
            print('-'*30)
            if 'tcp' in nm[host].keys():
                print('PORT\tSTATE\tSERVICE')
                ports = nm[host]['tcp']
                for key in ports.keys():
                    print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']))
                print('*'*30, '\n')
            else:
                mac = list(nm[host]['vendor'])
                mac = mac[0]
                vendor = nm[host]['vendor'][mac]
                print('Mac Address:\t%s'%mac)
                print('Vendor:\t\t%s'%vendor)
                print('\n')
        except:
            print('\n')
            pass
    else:
        try:
            nm.scan(hosts=host,arguments='-T4 -A', sudo=True)
            print('-'*30)
            print('Host : %s  State : %s'%(host,nm[host]['status']['state']))
            print('-'*30)
            print('PORT\tSTATE\tSERVICE')
            ports = nm[host]['tcp']
            for key in ports.keys():
                print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']))
            print('\nOS DETAILS')
            osdetails = nm[host]['hostscript'][1]['output']
            osdetails = osdetails.lstrip('\n')
            mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'][mac]
            print(osdetails)
            print('MAC Address : %s'%mac)
            print('Vendor : %s'%vendor)
            print('-'*30, '\n')
        except KeyError:
            print('*'*30, '\n')
