import socket
from sqlite3 import connect
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET is the Internet address family for IPv4. 
#SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport messages in the network.
print("Socket successfully created")
port = 8090
s.bind(('', port))
print("socket binded to %s" % (port))
s.listen(5)
print("socket is listening")
clientsocket, address = s.accept()
print('Got connection from', address)

while True:

    msg=input("send message to client:")
    clientsocket.send(msg.encode())
    print("Waiting For Response")
    client_msg=clientsocket.recv(1024)
    print("Message from Client: ", client_msg.decode())
    

