#! /usr/bin/python3

file = open('result.txt','at')
print('hello',file=file)
print('hi',file=file)
print('what',file=file)
print('Goodbye',file=file)
file.close()
