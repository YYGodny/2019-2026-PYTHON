import socket


def client_program():
    host = '10.71.169.9'
    #host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    
    #message = input(" -> ")  # take input
    #message.lower().strip() != 'bye'
    while True:
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
        client_socket.send(message.encode()) #send message
        
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
