#!/usr/bin/python3

import nmap
from sys import argv

def hostinfo(host, fast=False):
    nm = nmap.PortScanner()
    file = open('scanresult.txt','at')
    if fast:
        try:
            file = open('scanresult.txt','w+')
            scanning = 'progress'
            slashes = ['\\','|','/','--','\\','|','/','--']
            print('[_*_]Scanning {host}'.format(host=host))
            nm.scan(hosts=host,arguments='-T4 -F',sudo=True)
            for slash in slashes:
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
                print('[%s] Scanning %s' %(slash, host),end='\n',file=file)
            print('-'*30,end='\n',file=file)
            print('Host : %s  State : %s'%(host,nm[host]['status']['state']),end='\n',file=file)
            print('-'*30,end='\n',file=file)
<<<<<<< HEAD
            if 'tcp' in nm[host].keys():
                print('PORT\tSTATE\tSERVICE',end='\n',file=file)
                ports = nm[host]['tcp']
                for key in ports.keys():
                    print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']),end='\n',file=file)
                print('*'*30,end='\n',file=file)
=======
            if 'tcp' in nm[host].keys():
                print('PORT\tSTATE\tSERVICE',end='\n',file=file)
                ports = nm[host]['tcp']
                for key in ports.keys():
                    print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']),end='\n',file=file)
                print('*'*30,end='\n',file=file)
=======
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
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
            else:
                mac = list(nm[host]['vendor'])
                mac = mac[0]
                vendor = nm[host]['vendor'][mac]
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
                print('Mac Address:\t%s'%mac,end='\n',file=file)
                print('Vendor:\t\t%s'%vendor,end='\n',file=file)
                print('\n',end='\n',file=file)
            file.close()
<<<<<<< HEAD
=======
=======
                print('Mac Address:\t%s'%mac,file=file)
                print('Vendor:\t\t%s'%vendor,file=file)
                print('\n',file=file)
            file.close()
            with open('scanresult.txt','rt') as file:
                return(file.read())
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
        except:
            return('no open ports')
            pass

    else:
        try:
<<<<<<< HEAD
            file = open('scanresult.txt','w+')
=======
<<<<<<< HEAD
            file = open('scanresult.txt','w+')
=======
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
            print('[_*_]Scanning {host}'.format(host=host))
            nm.scan(hosts=host,arguments='-T4 -A',sudo=True)
            print('-'*30,end='\n',file=file)
            print('Host : %s  State : %s'%(host,nm[host]['status']['state']),end='\n',file=file)
            print('-'*30,end='\n',file=file)
            print('PORT\tSTATE\tSERVICE',end='\n',file=file)
            ports = nm[host]['tcp']
            for key in ports.keys():
                print('%s\t%s\t%s'%(key,ports[key]['state'],ports[key]['name']),end='\n',file=file)
            print('\nOS DETAILS',end='\n',file=file)
            osdetails = nm[host]['hostscript'][1]['output']
            osdetails = osdetails.lstrip('\n')
            mac = nm[host]['addresses']['mac']
            vendor = nm[host]['vendor'][mac]
            print(osdetails,end='\n',file=file)
            print('MAC Address : %s'%mac,end='\n',file=file)
            print('Vendor : %s'%vendor,end='\n',file=file)
            print('*'*30,'\n',end='\n',file=file)
            file.close()
        except KeyError:
            print('*'*30,'\n')
            


if __name__=='__main__':
    if len(argv)>1:
        host = argv[1]
    else:
        host = input('Enter host to scan: ')
    hostinfo(host)

