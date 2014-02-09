__author__ = 'KOL'

from socket import *
from Tools.Scripts.ftpmirror import raw_input

HOSTServer = ''
PORTServer = 12346
HOSTClient = "localhost"
PORTClient = 12345
ADDRESSServer = (HOSTServer, PORTServer)
ADDRESSClient = (HOSTClient, PORTClient)

BUFFER_SIZE = 1024

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESSServer)
server.listen(100)

client = socket(AF_INET, SOCK_STREAM)
connected = False
while not connected:
    try:
        client.connect(ADDRESSClient)
        connected = True
    except ConnectionRefusedError:
        pass

tcpCliSock, address = server.accept()
while True:
    try:
        data = str(raw_input('i> ')).replace("\n", "")
        client.send(data.encode('utf_8'))

        data = tcpCliSock.recv(BUFFER_SIZE)
        print("somebody>" + data.decode("utf_8"))
    except ConnectionResetError:
        break

tcpCliSock.close()
client.close()
server.close()