import socket
import sys

# Creating a Socket
def create_Socket():
    try:
        global host
        global port 
        global sct 
        host = ""
        port = 9999
        sct = socket.socket()

    except socket.error as msg:
        print("Socket creation error: "+str(msg))

