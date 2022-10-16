import socket
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_MYDDNS_IP = os.getenv("SERVER_MYDDNS_IP")
SERVER_MYDDNS_PORT = int(os.getenv("SERVER_MYDDNS_PORT"))

def run():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_MYDDNS_IP, SERVER_MYDDNS_PORT))

    while True:
        data = client.recv(1024)
        print(data.decode("utf-8"))

        # client.send(input().encode("utf-8"))

if __name__ == '__main__':
    run()