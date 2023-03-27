import random
#socket is the library that is used to create the server.
import socket
"""next i need to create the object in the socket which is going to be
working as a server"""
serverSocket = socket.socket()
""" binding the server socket with the IP and Port number,can take the port 
number between 0 to 65000"""

ip      = "127.0.0.1"
port    = 35491
serverSocket.bind((ip, port))
print("Server socket bound with with ip {} port {}".format(ip, port))
#serversocket.listen will now ready to accept  the communication from clients
serverSocket.listen()
while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    randomvalue=random.randint(0,5)
    print("Accepted {} connections so far".format(randomvalue))
