import socket
import time
import os
from tqdm import tqdm
import _thread

BUFFER = 4096

HOST = '127.0.0.1'
PORT_R = 9090
# PORT_S = 8080

serv_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_skt.bind((HOST, PORT_R))
serv_skt.listen(1)
print("waiting for a client...")

connection, address = serv_skt.accept()

# welcome_message = "Welcome to " + HOST + " at " + str(PORT_R)

# welcome_message = welcome_message.encode('utf-8')
# connection.send(welcome_message)

received = connection.recv(BUFFER).decode()

filename, filesize = received.split("thewall")

filename = os.path.basename(filename)

filesize = int(filesize)
progress = tqdm(range(filesize), f"{filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "wb") as file:
    while True:
        data = connection.recv(BUFFER)
        if not data:    
            break
        file.write(data)
        progress.update(len(data))
connection.close()
serv_skt.close()