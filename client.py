import socket
import os
from dotenv import load_dotenv

load_dotenv()
# noinspection SpellCheckingInspection
SERVER_MYDDNS_IP = os.getenv("SERVER_MYDDNS_IP")
# noinspection SpellCheckingInspection
SERVER_MYDDNS_PORT = int(os.getenv("SERVER_MYDDNS_PORT"))
CLIENT_DOMAIN = os.getenv("CLIENT_DOMAIN")


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_MYDDNS_IP, SERVER_MYDDNS_PORT))
        client_socket.send(CLIENT_DOMAIN.encode("utf-8"))


if __name__ == '__main__':
    run()
