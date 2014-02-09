from socket import *
import os
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
        data = data.decode("utf_8").split(" ")
        if len(data) == 1:
            command = data[0]
            dir = None
        else:
            command = data[0]
            dir = data[1]
        if command == "date":
            answer = ctime()
        elif command == "os":
            answer = os.name
        elif command == "ls":
            if None != dir:
                try:
                    answer = os.listdir(dir)
                except FileNotFoundError:
                    answer = "This directory is not exists"
            else:
                answer = os.listdir()
        else:
            answer = "Undefined command"
        tcpCliSock.send(str(answer).encode("utf_8"))

    tcpCliSock.close()
tcpSerSock.close()
