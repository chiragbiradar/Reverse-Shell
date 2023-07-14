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

# Binding the sockets and listening for connections
def bind_socket():
    try:
        global host
        global port
        global sct

        print("Socket creation error: "+str(port))

        sct.bind((host,port))
        sct.listen(5)

    except socket.error as msg:
        print("Socket Binding errror: " + str(msg) + "\n" + "Retrying...")
        bind_socket()

# Establishing connection with a client 
def socket_accept():
    conn,address = sct.accept()
    print("Connection has been Established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    send_command(conn)
    conn.close()

def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            sct.close()
            sys.exit()
        if str.encode