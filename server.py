import socket
import os
from dotenv import load_dotenv

# 128.69.78.197 home.boykos.ru
load_dotenv()

# noinspection SpellCheckingInspection
SERVER_MYDDNS_IP = os.getenv("SERVER_MYDDNS_IP")
# noinspection SpellCheckingInspection
SERVER_MYDDNS_PORT = int(os.getenv("SERVER_MYDDNS_PORT"))

INFILE = "db/lst"
OUTFILE = "db/lst.tmp"


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

            with open(INFILE, 'r', encoding='utf-8') as infile, open(OUTFILE, 'w+', encoding='utf-8') as outfile:

                for line in infile:
                    ln = line.replace('\n', '').split(sep=' ')

                    if (ln[0] != addr[0]) and (ln[1] != domain):
                        print('проходная запись')
                        lin = ln[0] + ln[1]
                        outfile.write(lin)
                        break

                    elif (ln[0] != addr[0]) and (ln[1] == domain):
                        print('Поменялся IP-адрес')
                        outfile.write(resolve_string)
                        break

                    elif (ln[0] == addr[0]) and (ln[1] == domain):
                        print('Запись имеется')
                        outfile.write(resolve_string)

        os.remove(INFILE)
        os.rename(OUTFILE, INFILE)


if __name__ == '__main__':
    run()
