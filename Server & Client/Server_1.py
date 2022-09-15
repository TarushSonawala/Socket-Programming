from codecs import utf_8_encode
import sys
# first of all import the socket library
import socket
# next create a socket object
s = socket.socket()
print("Socket successfully created")
# reserve a port on your computer in MY
# case it is _____ but it can be anything
port = 8090
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print("socket binded to %s" % (port))
# Put the socket into listening mode
s.listen(5)
print("socket is listening")
# a forever loop until we interrupt it or
# an error occurs
while True:
    # Establish connection with client.
    c, addr = s.accept()
    """accept() -> (socket object, address info)

    Wait for an incoming connection.  Return a new socket
    representing the connection, and the address of the client.
    For IP sockets, the address info is a pair (hostaddr, port).
    """
    print('Got connection from', addr)

    # send a thank you message to the client. encoding to send byte type.
    #c.send('9'.encode())  
    a=("Hey guys this is meow")
    #b=a.encode('utf-8')
    #c.send(len(a).to_bytes(2, byteorder='big'))
    c.send(a.encode())

    # Close the connection with the client





"""
A server has a bind() method which binds it to a specific IP and port so that it can listen to 
incoming requests on that IP and port. A server has a listen() method which puts the server into 
listening mode. This allows the server to listen to incoming connections. And last a server has
an accept() and close() method. The accept method initiates a connection with the client and
the close method closes the connection with the client. 
"""