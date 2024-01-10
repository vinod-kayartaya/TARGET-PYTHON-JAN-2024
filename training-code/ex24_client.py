from socket import socket, AF_INET, SOCK_STREAM
if __name__ == '__main__':
    server_socket = socket(AF_INET, SOCK_STREAM)
    addr = ('192.168.217.144', 1234)
    print(f'connecting to the server at {addr}')
    server_socket.connect(addr)
    user_name = input('Who are you? ')
    server_socket.send(user_name.encode('ascii'))
    msg = server_socket.recv(1024).decode('ascii')
    print(f'SERVER: {msg}')
