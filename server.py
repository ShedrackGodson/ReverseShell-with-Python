# A Socket?: Is a one endpoint of a two-way communication between two computers that are running on the same network.
# An Endpoint?: Is a combination of an IP address and a Port number of which the programs are running.


import sys
import socket

# Create a socket
def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("SOcket creation error: "+str(msg))

# Binding a socket and listen a connection
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the port: "+str(port))

        s.bind((host,port))
        s.listen(1)
        
    except socket.error as msg:
        print("Socket binding errror: "+str(msg)+"\n"+"Retrying...")
        bind_socket()

# Socket accept
def socket_accept():
    conn, address = s.accept()
    print("A connection has been established succesfully!"+"\n"+"IP: "+address[0]+"\n"+"Port: "+str(address[1]))
    send_commands(conn)
    conn.close()

# Send commands function
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "exit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv((1024), "utf-8"))
            print(client_response, end="")

# Defining the main function
def main():
    create_socket()
    bind_socket()
    socket_accept()


main()














