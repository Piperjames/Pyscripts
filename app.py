#!/usr/bin/python3

import cherrypy
import os
from listhosts import gethosts
<<<<<<< HEAD
from scanhosts import hostinfo
=======
<<<<<<< HEAD
from scanhosts import hostinfo
=======
>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67

current_dir = os.path.dirname(os.path.abspath(__file__))

class PenSuite(object):
    def __init__(self):
        file = open('index.html','rt')
        data = file.read()
        
        self.content = data

    @cherrypy.expose
    def index(self):
        return(self.content)
    
    @cherrypy.tools.expires(secs=0, force=True)
    @cherrypy.expose
    def netlist(self,inet):
        hosts = gethosts(inet)
        baseip, netips = hosts
        hostlist = ''
        for ip in netips:
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
            hostlist += '<li class="toscan">'+('.'.join((baseip,str(ip))))+'</li>'
        return(hostlist)

    @cherrypy.tools.expires(secs=0, force=True)
    @cherrypy.expose
    def hostdetails(self, host):
        pass

<<<<<<< HEAD
=======
=======
            hostlist += '<li>'+('.'.join((baseip,str(ip))))+'</li>'
        return(hostlist)

>>>>>>> f1ce60a788156a189832a523ebf723823a1bac8a
>>>>>>> 22f366793deab89a708ca4f45c315f383d4b0a67
if __name__=='__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 1995
    cherrypy.quickstart(PenSuite(), config={
        '/static':
        {'tools.staticdir.on': True,
         'tools.staticdir.dir': os.path.join(current_dir,"static")
         }
        })
