__author__ = 'KOL'

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

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDRESS)

while True:
    data = str(raw_input('> ')).replace("\n", "")
    if not data:
        break
    client.send(data.encode('utf-8'))
    data = client.recv(BUFFER_SIZE)
    if not data:
        break
    answer = str(data.decode("utf_8")).split("|")
    if len(answer) == 2:
        info = (answer[0], answer[1])
        print("server answer: " + str(info))
    else:
        print("server answer: " + answer[0])

client.close()
