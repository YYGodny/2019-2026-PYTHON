import socket
import sys
import threading
import transfer

HOST = socket.gethostbyname(socket.gethostname())
PORT = 32444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Du er kobla til: {addr}.')
        while True:
            skriv = input('Hva vil du si: ')
            if skriv == 'close':
                sys.exit()
            elif 'transfer' in skriv:
                transfer.transfer()
            elif 'update=' in skriv:
                path = skriv.split('update=')[1]
                with open(path, 'r') as f:
                    ssSkriv = f.read()
                    conn.send('update='.encode())
                    conn.sendall(bytes(ssSkriv, encoding='utf-8'))
                continue
                
            conn.sendall(bytes(skriv, encoding='utf-8'))
