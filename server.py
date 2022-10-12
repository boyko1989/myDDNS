import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("89.108.88.174", 12345))

server.listen()

while True:
    user, address = server.accsept()

    user.send("connect".encode("utf-8"))

