#!/usr/bin/python3

import nmap
from sys import argv

def hostinfo(host, fast=False):
    nm = nmap.PortScanner()
    if fast:
        try:
            scanning = 'progress'
            slashes = ['\\','|','/','--','\\','|','/','--']
            nm.scan(hosts=host,arguments='-T4 -F',sudo=True)
            for slash in slashes:
                print('[%s] Scanning %s' %(slash, host))
            print('-'*30)
            print('Host : %s  State : %s'%(host,nm[host]['status']['state']))
            print('-'*30)
            if 'tcp' in nm[host].keys():
                print('PORT\tSTATE\tSERVICE')
                ports = nm[host]['tcp']
                for key in ports.keys():
                    print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']))
                print('*'*30,'\n')
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
            nm.scan(hosts=host,arguments='-T4 -A',sudo=True)
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
            print('*'*30,'\n')
        except KeyError:
            print('*'*30,'\n')
            


if __name__=='__main__':
    if len(sys.argv):
        host = sys.argv[1]
    else:
        host = input('Enter host to scan: ')
    hostinfo(host)

