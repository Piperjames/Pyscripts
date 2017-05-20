#!/usr/bin/python3

import nmap
from sys import argv

def hostinfo(host, fast=False):
    nm = nmap.PortScanner()
    file = open('scanresult.txt','at')
    if fast:
        try:
            scanning = 'progress'
            slashes = ['\\','|','/','--','\\','|','/','--']
            print('[_*_]Scanning {host}'.format(host=host))
            nm.scan(hosts=host,arguments='-T4 -F',sudo=True)
            for slash in slashes:
                print('[%s] Scanning %s' %(slash, host),file=file)
            print('-'*30,file=file)
            print('Host : %s  State : %s'%(host,nm[host]['status']['state']),file=file)
            print('-'*30)
            if 'tcp' in nm[host].keys():
                print('PORT\tSTATE\tSERVICE',file=file)
                ports = nm[host]['tcp']
                for key in ports.keys():
                    print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']),file=file)
                print('*'*30,'\n',file=file)
            else:
                mac = list(nm[host]['vendor'])
                mac = mac[0]
                vendor = nm[host]['vendor'][mac]
                print('Mac Address:\t%s'%mac,file=file)
                print('Vendor:\t\t%s'%vendor,file=file)
                print('\n',file=file)
            file.close()
            with open('scanresult.txt','rt') as file:
                return(file.read())
        except:
            return('no open ports')
            pass

    else:
        try:
            print('[_*_]Scanning {host}'.format(host=host))
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
    if len(argv)>1:
        host = argv[1]
    else:
        host = input('Enter host to scan: ')
    hostinfo(host)

