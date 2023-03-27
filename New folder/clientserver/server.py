import random
import socket
# Create a server socket
serverSocket = socket.socket()
print("Server socket created")
# Associate the server socket with the IP and Port
ip      = "127.0.0.1"
port    = 35491
serverSocket.bind((ip, port))
print("Server socket bound with with ip {} port {}".format(ip, port))
# Make the server listen for incoming connections
serverSocket.listen()
# Server incoming connections "one by one"
while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    randomvalue=random.randint(0,5)
    print("Accepted {} connections so far".format(randomvalue))
    # read from client connection
