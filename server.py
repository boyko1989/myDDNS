import socket
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_MYDDNS_IP = os.getenv("SERVER_MYDDNS_IP")
SERVER_MYDDNS_PORT = int(os.getenv("SERVER_MYDDNS_PORT"))


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_MYDDNS_IP, SERVER_MYDDNS_PORT))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)
        #        print()
        print(addr[0], addr[1])

        client_socket.sendall('CLIENT_DOMAIN'.encode())
        client_socket.close()


if __name__ == '__main__':
    run()
