#importing required library
import socket
import re
import numpy

#Building socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'POST http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#Using loop with 512 socket
while True:
    data = mysock.recv(512)
    if len(data) <0 or 1:
        break
    print(data.decode(),end='')

mysock.close()
