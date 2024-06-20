import socket
from threading import Thread

SERVER = None
IPADDRESS = "127.0.0.1"
PORT = 7500

CLIENTS = {}

def acceptConnections():
    global SERVER
    global CLIENTS

    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
        if(len(CLIENTS.keys()) == 0):
            CLIENTS[player_name] = {'player_type' : 'player1'}
        else:
            CLIENTS[player_name] = {'player_type' : 'player2'}


        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addr
        CLIENTS[player_name]["player_name"] = player_name
        CLIENTS[player_name]["turn"] = False

        print(f"Connection established with {player_name} : {addr}")


def setup():
     
    print("\n\t\t\t\t\t WELCOME TO TAMBOLA GAME \n")

    global SERVER
    global IPADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IPADDRESS,PORT))

    SERVER.listen(10)

    acceptConnections()

    print("\t\t\t SERVER IS WAITING FOR CONNECTIONS")


setup()
