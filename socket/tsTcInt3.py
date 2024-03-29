#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author:rxl
'''
Python3 socket客户端
'''

from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = input('> ')
	if not data:
		break
	tcpCliSock.send(data.encode())
	data = tcpCliSock.recv(BUFSIZ)
	if not data:
		break
	print(data.decode())
tcpCliSock.close()