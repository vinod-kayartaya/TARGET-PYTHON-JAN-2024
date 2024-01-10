from socket import socket, AF_INET, SOCK_STREAM
import time
from threading import Thread


def client_handler(cl_sock, cl_addr):
    print(f'got a client connection from {cl_addr}')
    user_name = cl_sock.recv(1024).decode('ascii')
    print(f'client identified as {user_name}')
    msg = f'Hello {user_name}. How are you?'
    cl_sock.send(msg.encode('ascii'))
    time.sleep(300)


if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.217.144', 1234)
    server_socket.bind(addr)
    server_socket.listen()
    print(f'server started at {addr}')

    while True:
        print('waiting for a client to connect...')
        cl_info = server_socket.accept()
        Thread(target=client_handler, args=cl_info).start()