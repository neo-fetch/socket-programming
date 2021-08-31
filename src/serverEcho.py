# import socket

# HOST = '127.0.0.1'
# PORT = 9090

# serv_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serv_skt.bind((HOST, PORT))
# serv_skt.listen(1)

# print("waiting for a client...")
# connection, address = serv_skt.accept()

# welcome_message = "Welcome to " + HOST + " at " + str(PORT)

# welcome_message = welcome_message.encode('utf-8')
# connection.send(welcome_message)

# print("Connection successful: connected to ", address)

# while True:
#     data = connection.recv(1024).decode('utf-8')
#     if not data: break
#     print("Recieved: ", data)
#     #connection.sendall(data)
# connection.close()

# For peer to peer communication uncomment the code below:

import socket
import time
from tqdm import tqdm
import _thread

HOST = '127.0.0.1'
PORT_R = 9090
PORT_S = 8080

def client():
    for i in tqdm(range(5), desc = 'You have 5 seconds to run the other peer program...'):
        time.sleep(1)    
    client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_skt.connect((HOST,PORT_S)) # change HOST to the IP of the server you want to send text to
    while True:
        msg = input("\n>")
        msg=msg.encode("utf-8")
        client_skt.sendall(msg)

    
def server():
    serv_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_skt.bind((HOST, PORT_R))
    serv_skt.listen(1)
    print("waiting for a client...")
    connection, address = serv_skt.accept()

    welcome_message = "Welcome to " + HOST + " at " + str(PORT_R)

    welcome_message = welcome_message.encode('utf-8')
    connection.send(welcome_message)

    print("Connection successful: connected to ", address,"\n>")

    while True:
        # print("Waiting for response...")
        data = connection.recv(1024).decode('utf-8')
        if not data: break
        print("Friend: ", data, "\n>")



try:
   _thread.start_new_thread( server, ( ) )
   _thread.start_new_thread( client, ( ) )
except:
   print ("Error: unable to start thread")



while 1:
    pass
# msg=client_skt.recv(1024)
# msg=msg.decode('utf-8')
# print(msg)




