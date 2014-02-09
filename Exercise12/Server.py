import time

__author__ = 'KOL'

from socket import *

HOST = ''
PORT = 21567
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)


def sleep(time_sec):
    for i in range(0, time_sec):
        time.sleep(1)
        print(end=".")
    print()

while True:
    print('waiting for connection...')
    send, address = server.accept()
    print('...connected from:', address)

    while True:
        data = send.recv(BUFFER_SIZE)
        if not data:
            break
        client_request = data.decode("utf_8")
        print("client request: " + client_request)
        try:
            sleep(int(client_request))
            answer = "success"
        except ValueError:
            sleep(5)
            answer = "finished with errors"
        print(answer)
        send.send(answer.encode("utf_8"))

    send.close()
server.close()
