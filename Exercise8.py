__author__ = 'KOL'

import threading
from socket import *
from Tools.Scripts.ftpmirror import raw_input

BUFFER_SIZE = 1024

HOSTServer = ''
PORTServer = str(raw_input("Please, input port of server(somebody):")).replace("\n", "")
if not PORTServer:
    PORTServer = 12345
else:
    PORTServer = int(PORTServer)
HOSTClient = "192.168.0.101"
PORTClient = str(raw_input("Please, input port of client(you):")).replace("\n", "")
if not PORTServer:
    PORTClient = 12346
else:
    PORTClient = int(PORTClient)
ADDRESSServer = (HOSTServer, PORTServer)
ADDRESSClient = (HOSTClient, PORTClient)


def send():
    client = socket(AF_INET, SOCK_STREAM)
    connected = False
    while not connected:
        try:
            client.connect(ADDRESSClient)
            connected = True
        except ConnectionRefusedError:
            pass
    while True:
        try:
            text = str(raw_input('i> ')).replace("\n", "")
            client.send(text.encode('utf_8'))
        except ConnectionResetError:
            break
    client.close()


def get_answer():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ADDRESSServer)
    server.listen(100)
    s, address = server.accept()
    while True:
        try:
            text = s.recv(BUFFER_SIZE)
            print("somebody>" + text.decode("utf_8"))
        except ConnectionResetError:
            break
    s.close()
    server.close()


i = threading.Thread(target=send)
somebody = threading.Thread(target=get_answer)

i.start()
somebody.start()