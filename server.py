import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("89.108.88.174", 12345))

server.listen()

while True:
    user, address = server.accept()

    user.send(input().encode("utf-8"))

    data = user.recv(1024)
    print(data.decode("utf-8"))

