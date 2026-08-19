import socket
import sys
import threading
import transfer

HOST = socket.gethostname()
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Du er kobla til: {addr}.')
        while True:
            skriv = input('Hva vil du si:')
            conn.sendall(bytes(skriv, encoding='utf-8'))
            if skriv == 'close':
                sys.exit()
            elif 'transfer' in skriv:
                 transfer.transfer()
