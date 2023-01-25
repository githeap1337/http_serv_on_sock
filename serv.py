# -*- coding: utf-8 -*-

import socket


def main():
    # Create a TCP/IP socket
    # server = socket.create_server(('127.0.0.1', 8000))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding socket address and port
    server_address = ('127.0.0.1', 8000)
    server.bind(server_address)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Listen 1 incoming connection
    server.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        client_socket, address = server.accept()
        try:
            print('connection from: ', address)
            while True:
                received_data = client_socket.recv(1024).decode('utf-8')
                # print('get response:\n', received_data)
                if received_data:
                    response = b'HTTP/1.1 200 OK\nContent-type: text/html; charset=utf-8\n\n'
                    with open('packages.txt', 'r') as packs:
                        file_content = "<br />".join(packs.readlines())
                    client_socket.sendall(response + file_content.encode('utf-8'))
                else:
                    break
        finally:
            # client_socket.shutdown(socket.SHUT_RDWR)
            client_socket.close()
            # server.shutdown(socket.SHUT_RDWR)
            # server.close()


if __name__ == "__main__":
    main()
