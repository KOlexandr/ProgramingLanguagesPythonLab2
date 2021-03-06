from socket import *
from Tools.Scripts.ftpmirror import raw_input

HOST = str(raw_input("Please, input hostName:")).replace("\n", "")
PORT = str(raw_input("Please, input port:")).replace("\n", "")

if not HOST:
    HOST = "localhost"
if not PORT:
    PORT = 21567
else:
    PORT = int(PORT)

BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDRESS)

while True:
    data = str(raw_input('> ')).replace("\n", "")
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data = tcpCliSock.recv(BUFFER_SIZE)
    if not data:
        break
    print(data.decode("utf_8"))

tcpCliSock.close()
