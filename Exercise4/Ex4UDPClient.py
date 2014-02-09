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

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data.encode('utf-8'), ADDRESS)
    data, ADDRESS = udpCliSock.recvfrom(BUFFER_SIZE)
    if not data:
        break
    print(data.decode("utf_8"))

udpCliSock.close()
