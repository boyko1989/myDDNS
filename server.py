import socket
import os
from dotenv import load_dotenv

load_dotenv()

# noinspection SpellCheckingInspection
SERVER_MYDDNS_IP = os.getenv("SERVER_MYDDNS_IP")
# noinspection SpellCheckingInspection
SERVER_MYDDNS_PORT = int(os.getenv("SERVER_MYDDNS_PORT"))


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((SERVER_MYDDNS_IP, SERVER_MYDDNS_PORT))

        server_socket.listen()

        while True:
            client, addr = server_socket.accept()
            data = client.recv(1024)
            domain = data.decode("utf-8")
            resolve_string = addr[0] + ' ' + domain + '\n'
            print(resolve_string)

            with open('db/lst', 'a+', encoding='utf-8') as lst:
        #        for line in lst:
        #            print("Строка", line)
        #        lst.read()
                lst.write(resolve_string)

if __name__ == '__main__':
    run()
