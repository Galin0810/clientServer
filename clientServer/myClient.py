import socket
chatsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9865
chatsocket.connect((host, port))
n=str(input("Who are you: "))
chatsocket.send(n.encode())
a=chatsocket.recv(1024)
print(a.decode())
chatsocket.close()
