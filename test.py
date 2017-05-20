#!/usr/bin/python3

file = open('scanresult.txt','w+')
print('hello',end='\n',file=file)
print('hi',end='\n',file=file)
print('who',end='\n',file=file)
print('which',end='\n',file=file)
me = 'amos'
nick = 'piper'
print(me,end='\n',file=file)
print('%s'%nick,end='\n',file=file)
file.close()
