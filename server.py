import socket
import errno
import time

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_socket.bind(('', 53210))
serv_socket.listen(10)

while True:
    client_socket, client_address = serv_socket.accept()
    print('Connected by', client_address)

    time.sleep(1)
    data = (str(client_address[0]) + ':' + str(client_address[1])).encode()

    client_socket.sendall(data)

    client_socket.close()
