from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print "waiting for a connection..."
    tcpCliSock, addr = tcpSerSock.accept()
    print "connected to...: ", addr

    while True:
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        tcpCliSock.send("[%s] %s"% (ctime(), data))
    tcpCliSock.close()
tcpSerSock.close()
