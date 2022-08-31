import sys 
# Import socket module
import socket			

# Create a socket object
s = socket.socket()		

# Define the port on which you want to connect
port = 56285		

# connect to the server on local computer
s.connect(('192.168.178.91', port))

# receive data from the server and decode it to get the string.
print (s.recv(1024).decode())
# close the connection
s.close()	
	
