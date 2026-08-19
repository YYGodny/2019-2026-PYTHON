import socket
import os

def transfer():
    SERVER_HOST = socket.gethostname()
    SERVER_PORT = 43222
    BUFFER_SIZE = 4096
    SEPERATOR = '<SEPERATOR>'

    so = socket.socket()
    so.bind((SERVER_HOST, SERVER_PORT))
    so.listen(5)
    client_socket, address = so.accept()
    recived = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = recived.split(SEPERATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    
    with open(filename, 'wb') as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
            
    client_socket.close()
    so.close()

