# -*- coding: utf-8 -*-

import socket


def main():
    # server = socket.create_server(('127.0.0.1', 8000))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8000))
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.listen(10)
    # while True:
    client_socket, address = server.accept()
    print(server.accept())
    received_data = client_socket.recv(1024).decode('utf-8')
    print('get data from socket: ', received_data)
    response = 'HTTP/1.1 200 OK\nContent-type: text/html; charset=utf-8\n\n'
    with open('packages.txt', 'w') as packs:
        for pack in packs:
            response += pack.strip() + '<br />>'
    client_socket.send(response.encode('utf-8'))
    client_socket.shutdown(socket.SHUT_RDWR)
    server.shutdown(socket.SHUT_RDWR)
    server.close()


if __name__ == "__main__":
    main()
