import socket

s=socket.socket()

s.bind(('0.0.0.0',8090))
s.listen(5)

while True:

    print("Hey")
    client,address = s.accept()
    while True:
        content = client.recv(1024)
        
        if len(content) == 0:
            break
        else:
            print(content)
    
    print("Meow From Trace PC")
    client.close()
    