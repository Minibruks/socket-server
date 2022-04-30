import socket


def client(ip, port, connection_type='tcp'):
    if connection_type == 'tcp':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))
        data = client_socket.recv(1024)
    else:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(''.encode(), (ip, int(port)))
        data = client_socket.recv(1024)
    client_socket.close()
    print(data.decode())
