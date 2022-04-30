import socket


def client(ip, port, connection_type='tcp'):
    if connection_type == 'tcp':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, int(port)))
        data = client_socket.recv(1024)
    elif connection_type == 'udp':
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.sendto(''.encode(), (ip, int(port)))
        data = client_socket.recv(1024)
    else:
        print('Undefined connection type')
        return None
    client_socket.close()
    print(data.decode())
