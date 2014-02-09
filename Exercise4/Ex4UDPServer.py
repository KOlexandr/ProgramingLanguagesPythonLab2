from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDRESS)

while True:
    print('waiting for message...')
    data, address = udpSerSock.recvfrom(BUFFER_SIZE)
    answer = '[%s] %s' % (ctime(), data.decode("utf_8"))
    udpSerSock.sendto(answer.encode("utf_8"), address)
    print('...received from and returned to:', address)

udpSerSock.close()