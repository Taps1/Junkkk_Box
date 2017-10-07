from socket import *
from time import ctime

HOST = ""
PORT = 21567
BUFFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSoc = socket(AF_INET, SOCK_DGRAM)
udpSerSoc.bind(ADDR)

while True:
    print "waiting for a message..."
    data, addr = udpSerSoc.recvfrom(BUFFSIZE)
    udpSerSoc.sendto("[%s] %s" % (ctime(), data), addr)
    print "received from and returned to ...", addr

udpSerSock.close()
