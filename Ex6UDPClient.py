import socket

HOST = 'time.nist.gov'
PORT = socket.getservbyname('daytime', 'udp')

BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socketClient.connect(ADDRESS)

data = socketClient.recv(BUFFER_SIZE)
print(data.decode("utf_8"))

socketClient.close()