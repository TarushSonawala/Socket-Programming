import socket
from sqlite3 import connect
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
    

