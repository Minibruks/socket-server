import socket
import errno
import time


def server(ip, port, connection_type='tcp'):
    if connection_type == 'tcp':
        serv_socket = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
        serv_socket.bind((ip, int(port)))
        serv_socket.listen(10)

        while True:
            client_socket, client_address = serv_socket.accept()
            print('Connected by', client_address)

            time.sleep(1)
            data = (str(client_address[0]) + ':' + str(client_address[1])).encode()

            client_socket.sendall(data)

            client_socket.close()
    else:
        serv_socket = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM, proto=0)
        serv_socket.bind((ip, int(port)))

        while True:
            client_socket, client_address = serv_socket.recvfrom(1024)
            print('Connected by', client_address)

            time.sleep(1)
            data = (str(client_address[0]) + ':' + str(client_address[1])).encode()

            serv_socket.sendto(data, client_address)
