import socket

# Create a socket and bind it to a port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8000))
sock.listen()

# Accept a connection
conn, addr = sock.accept()

# Enter an infinite loop to receive data from the client
while True:
    data = conn.recv(1024).decode()
    print(f"Received data: {data}")

# Close the socket
conn.close()
sock.close()
