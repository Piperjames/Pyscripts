#! /usr/bin/python3

from listhosts import gethosts
from scanhosts import hostinfo
import optparse
import os

def isIP(host):
    if not "/" in host and not host.isalnum():
        if len(host.split(".")) == 4:
            return(True)
        else:
            return(False)

def main():
    parser = optparse.OptionParser('usage%prog -h|-c <host|cidr> -f <True|False>')
    parser.add_option('-H', dest='Host', type='string',\
            help='specify target host')
    parser.add_option('-c', dest='CIDR', type='string',\
            help='specify cidr')
    parser.add_option('-f', dest='Speed', type='string', default=False,\
            help='specify scan level')
    (options,args) = parser.parse_args()
    host = options.Host
    CIDR = options.CIDR
    speed = options.Speed

    if (host == None) and (CIDR == None):
        print('[-] Specify a host or cidr to scan')
        exit(0)

    if host and not CIDR:
        if isIP(host):
            hostinfo(host, speed)
        else:
            print('[-] Specify a correct host')
            exit(0)

    elif CIDR and not host:
        hosts = gethosts(CIDR)
        baseip, netips = hosts
        for ip in netips:
            hostinfo('.'.join((baseip, str(ip))),speed)

if __name__=="__main__":
    if os.geteuid() != 0:
        print('This script needs to be run as root')
    else:
        main()
