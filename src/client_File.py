import socket
import time
import os
import tqdm
import _thread


HOST = '127.0.0.1' # change this to the system ipv4 address where we should recieve messages from
PORT_S = 9090
# PORT_R = 8080
BUFFER = 4096

filename = 'clientEcho.py'
filesize = os.path.getsize(filename)

client_skt = socket.socket()

client_skt.connect((HOST, PORT_S))

client_skt.send(f"{filename}thewall{filesize}".encode())
progress = tqdm.tqdm(range(filesize), f"{filename}", unit="B", unit_scale=True, unit_divisor=1024)
with open(filename, "rb") as file:
    while True:

        data = file.read(BUFFER)
        if not data:
            break

        client_skt.sendall(data)
        progress.update(len(data))
client_skt.close()