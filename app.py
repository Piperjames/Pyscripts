#!/usr/bin/python3

import cherrypy
import os
from listhosts import gethosts

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
            hostlist += '<li>'+('.'.join((baseip,str(ip))))+'</li>'
        return(hostlist)

if __name__=='__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 1995
    cherrypy.quickstart(PenSuite(), config={
        '/static':
        {'tools.staticdir.on': True,
         'tools.staticdir.dir': os.path.join(current_dir,"static")
         }
        })
