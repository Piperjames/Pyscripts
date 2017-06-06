#!/usr/bin/python3
#vim: set fileencoding=<UTF-8>

import socket
def getip():
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
        s.connect(('<broadcast>',0))

        return(s.getsockname()[0])

if __name__ == '__main__':
        print(getip())
