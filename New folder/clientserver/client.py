import socket
socketObject = socket.socket()
#Now socket is created and it has to  working as a client
#now i will try to connect with the server side
socketObject.connect(("localhost", 35491))
print("Connected to localhost")

HTTPMessage = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
bytes       = str.encode(HTTPMessage)
socketObject.sendall(bytes)

while(True):
    data = socketObject.recv(1024)
    print(data)
    if(data==b''):
        print("Connection closed")
        break
socketObject.close()
