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
        data = client_socket.recv(1024)
        print(addr[0], data.decode("utf-8"))
        print()

        client_socket.close()


if __name__ == '__main__':
    run()
