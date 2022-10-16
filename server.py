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

            with open(INFILE, encoding='utf-8') as infile, open(OUTFILE, 'w', encoding='utf-8') as outfile:
                not_for_write = 0

                for line in infile:
                    ln = line.replace('\n', '').split(sep=' ')
                    # print(type(lst), 'Тип') # <class '_io.TextIOWrapper'> Тип

                    if line.find(domain) > 0 and ln[1] != addr[0]:
                        not_for_write += 0
                        print('У домена:', domain, 'поменялся IP на', addr[0])
                        outfile.write(resolve_string)

                    elif line.find(domain) > 0 and ln[1] == addr[0]:
                        not_for_write += 1
                        print('Запись имеется:', resolve_string)
                        break

                    elif line.find(domain) < 0:
                        not_for_write += 0
                        outfile.write(line)

                # if not_for_write == 0:
                #     lst.write(resolve_string)
            os.remove(INFILE)
            os.rename(OUTFILE, INFILE)


if __name__ == '__main__':
    run()
