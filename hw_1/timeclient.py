from socket import *

client = socket(AF_INET, SOCK_STREAM)
port = 1303
message = 'write your ip address please: '
client.connect((str(input(message)), port))
current_dt = client.recv(1024).decode('utf-8')
print(current_dt)
client.close()