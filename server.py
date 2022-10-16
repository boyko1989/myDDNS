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
            # print(resolve_string)

            with open('db/lst', 'r+', encoding='utf-8') as lst:
# 1. Условие: если нет доменного имени в списке, то записываем строку
                not_for_write = 0

                for line in lst:
                    ln = line.replace('\n', '')
                    ln = ln.split(sep=' ')
                    if line.find(domain) > 0 and ln[1] == addr[0]:
                        line.replace(line, '')
                        lst.write(resolve_string)
                    elif line.find(domain) > 0 and ln[1] != addr[0]:
                        not_for_write += 1


                if not_for_write == 0:
                    lst.write(resolve_string)
                # elif
# 2. Условие: если имя есть, и IP другой, то перезаписываем строку
                pass



if __name__ == '__main__':
    run()
