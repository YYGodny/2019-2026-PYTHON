import socket


def server_program():
    # get the hostname
    host = '10.71.169.9'
    #host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    a = 0
    while a != 2:
        # configure how many client the server can listen simultaneously
        server_socket.listen(3)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        if a == 0:
            player1 = conn
        if a == 1:
            player2 = conn
        a += 1
    ask = 'stein, saks eller papir?'
    player1.send(ask.encode())
    player2.send(ask.encode())
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
  
        data = player1.recv(1024).decode()
        data2 = player2.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from player1: " + str(data))
        print('from player2: ' + str(data2))

        vinner = 'du vant!'
        taper = 'du tapte :('
        uavgjort = 'begge er tapere!'
        skam = 'skam deg, den som sente feil! >:('
        
        if data == 'saks' and data2 == 'stein':
            player2.send(vinner.encode())
            player1.send(taper.encode())
        elif data == 'saks' and data2 == 'papir':
            player1.send(vinner.encode())
            player2.send(taper.encode())
        elif data == 'stein' and data2 == 'papir':
            player2.send(vinner.encode())
            player1.send(taper.encode())
        elif data == 'stein' and data2 == 'saks':
            player2.send(taper.encode())
            player1.send(vinner.encode())
        elif data == 'papir' and data2 == 'saks':
            player2.send(vinner.encode())
            player1.send(taper.encode())
        elif data == 'papir' and data2 == 'stein':
            player2.send(taper.encode())
            player1.send(vinner.encode())
        elif data == data2:
            player2.send(uavgjort.encode())
            player1.send(uavgjort.encode())
        else:
            player2.send(skam.encode())
            player1.send(skam.encode())
            
        
        
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
