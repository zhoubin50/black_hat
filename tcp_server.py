#!/usr/bin/env python
import socket
import threading

host="0.0.0.0"
port=8888

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print "[*] listen on %s:%d"% (host,port)
def handle_client(client_socket):
    request=client_socket.recv(1024)
    print "[*] received: %s"% request
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr=server.accept()
    print "[*] accept connection from:%s:%d"% (addr[0],addr[1])
    client_handler=threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
