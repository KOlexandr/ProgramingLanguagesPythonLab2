__author__ = 'KOL'

from socket import *

base = {"daytime": ("time.windows.com", 13), "habr": ("habrahabr.ru", 80)}

HOST = ''
PORT = 21567
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('waiting for connection...')
    send, address = server.accept()
    print('...connected from:', address)

    while True:
        data = send.recv(BUFFER_SIZE)
        if not data:
            break
        inData = str(data.decode("utf_8")).replace("\n", "").split("|")
        if inData[0] == "add_service" and len(inData) == 4:
            base[inData[1]] = (inData[2], int(inData[3]))
            answer = "added"
            print("added: " + str(base[inData[1]]))
        elif inData[0] == "get_service" and len(inData) == 2:
            try:
                info = base[inData[1]]
                answer = info[0] + "|" + str(info[1])
                print("sent: " + str(info))
            except KeyError:
                answer = "service not found"
                print(answer + ": " + inData[1])
        else:
            print("unknown command:" + str(inData[0]))
            answer = "unknown command"
        send.send(answer.encode("utf_8"))

    send.close()
server.close()
