#!/usr/bin/env python

import socket

host="www.baidu.com"
port=80

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
client.send("GET / HTTP/1.1\r\nHost:baidu.com\r\n\r\n")
response=client.recv(4096)
print response
