import random
import socket
serverSocket = socket.socket()
print("Server socket created")
ip      = "127.0.0.1"
port    = 35491
serverSocket.bind((ip, port))
print("Server socket bound with with ip {} port {}".format(ip, port))
serverSocket.listen()
while(True):
    (clientConnection, clientAddress) = serverSocket.accept()
    randomvalue=random.randint(0,5)
    print("Accepted {} connections so far".format(randomvalue))
