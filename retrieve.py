#!/usr/bin/python3
#vim: set fileencoding=<utf-8>

import socket
import os

def receive(conn):
	downloads='Downloads'
	downfolder=os.path.join(os.getcwd(),downloads)
	if not os.path.exists(downfolder):
		os.mkdir(downfolder)
	direc='home'
	while True:
		conn.send(direc.encode('ascii'))
		fileinfo=conn.recv(1024)
		fileinfo=fileinfo.decode('ascii')
		fileinfo=fileinfo.split('\n')
		filetype=fileinfo[0]
		name=fileinfo[1]

		if filetype=='folder':
			print(name)
			filelist=conn.recv(1024)
			filelist=filelist.decode('ascii')
			filelist=filelist.split('\n')
			filelist.insert(0,'..')
			filelist.append('home')

			for file in filelist:
				print('[%d] /%s'%(filelist.index(file)+1,file))
			query=int(input('>>'))
			query-=1
			direc=(filelist[query])

		else:
			filename=os.path.join(downfolder,name)
			ask=input('Do you want to download file?(y/n):')

			if ask=='y':
				with open(filename,'ab') as file:
					while True:
						data=conn.recv(1024)
						if b'no data' in data:
							break
						file.write(data)
			print('Download complete')
			print('-------------------------')
			direc='home'

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',1995))
server.listen(5)
print('Waiting for connection')

while True:
	conn,addr=server.accept()
	print('Connection from',addr[0],'::',addr[1])

	receive(conn)
