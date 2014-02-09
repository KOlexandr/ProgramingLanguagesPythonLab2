from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDRESS)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, address = tcpSerSock.accept()
    print('...connected from:', address)

    while True:
        data = tcpCliSock.recv(BUFFER_SIZE)
        if not data:
            break
        answer = '[%s] %s' % (ctime(), data.decode("utf_8"))
        tcpCliSock.send(answer.encode("utf_8"))

    tcpCliSock.close()
tcpSerSock.close()
