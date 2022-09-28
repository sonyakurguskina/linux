from socket import *
import datetime as dt

server = socket(AF_INET, SOCK_STREAM)
port = 1303
server.bind(('', port))
current_dt = str(dt.datetime.now().strftime("%d.%m.%Y %H:%M")).encode('utf-8')

while True:
    server.listen()
    client, addr = server.accept()
    client.send(current_dt)
    client.close()