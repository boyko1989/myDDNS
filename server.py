import socket
import os
from dotenv import load_dotenv

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

#            f = open(OUTFILE, "w")
#            f.close()

            with open(INFILE, encoding='utf-8') as infile, open(OUTFILE, 'w', encoding='utf-8') as outfile:

                for line in infile:
                    ln = line.replace('\n', '').split(sep=' ')
                    print(type(ln), 'Тип') # <class '_io.TextIOWrapper'> Тип

                    print(ln[0], '----', ln[1])

                    # if ln[0] != domain and ln[0] != addr[0]:
                    #     print('Новая запись')
                    #     outfile.write(resolve_string)
                    # 
                    # elif ln[1] == domain and ln[0] == addr[0]:
                    #     print('Запись имеется:', line)
                    #     outfile.write(resolve_string)
                    #
                    # elif ln[1] == domain and ln[0] != addr[0]:
                    #     print('Поменялся IP-адрес')
                    #     outfile.write(resolve_string)

    #        os.remove(INFILE)
            os.rename(OUTFILE, 'db/real.txt')


if __name__ == '__main__':
    run()
