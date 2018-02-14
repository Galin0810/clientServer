import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9865

serversocket.bind((host, port))
serversocket.listen(8)
while True:
    clientsocket,addr=serversocket.accept()
    a=clientsocket.recv(1024)
    print("Connect:",a.decode(),addr)

    h = "Hello, " + str(a.decode())
    clientsocket.send(h.encode())
    clientsocket.close()
