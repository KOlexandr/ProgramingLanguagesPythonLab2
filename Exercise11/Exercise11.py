__author__ = 'KOL'

from socket import *
from Tools.Scripts.ftpmirror import raw_input

BUFFER_SIZE = 102400

s = socket(AF_INET, SOCK_STREAM)
while True:
    try:
        link = str(raw_input("Please, input hostName http://")).replace("\n", "")
        file = open("Exercise11/ex11.html", "w")

        s.connect((link, 80))

        s.sendall(("GET http://" + link + " HTTP/1.0\n\n").encode('utf_8'))
        data = s.recv(BUFFER_SIZE)
        file.write(data.decode("cp1251"))
        file.close()
        break
    except error:
        print("Wrong link. Try again later :)")
        continue

s.close()
