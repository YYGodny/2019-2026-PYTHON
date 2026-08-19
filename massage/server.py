import socket
import threading

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 7462
s.bind((host, port))

users = []
cusers = []

def send_everyone(x):
    h = [i.send(f'{x}'.encode()) for i in cusers]

def main(addr1, conn1):
    try:
        indx = 0
        while True:
            massage = conn1.recv(1024).decode()
            if massage in [str(i) for i in users]:
                for index, item in enumerate(users):
                    if massage in str(item):
                        indx = index
                print(f'Index: {indx}')    
                print('Ok!')
                contacting = True
                conn1.send(f'From Server: you are messaging {massage}'.encode())
                while contacting:
                    massage = conn1.recv(1024).decode()
                    if massage == '7283462103':
                        contacting = False
                        continue
                    cusers[indx].send(f'From {addr1}: {massage}'.encode())
                    print(f'contact {massage}')
            print(massage)
    except ConnectionResetError:
        users.remove(addr1)
        cusers.remove(conn1)
        #finn ut hvordan man stopper threads, for å ikke lage evig mange
        send_everyone(f'123487621 {addr1}')
        print(users)

while True:
    print(users)
    s.listen()
    conn, addr = s.accept()
    print(f'{addr} connected!')
    users.append(addr)
    cusers.append(conn)
    th = threading.Thread(target=main, args=(addr, conn))
    th.daemon = True
    th.start()
    for i in cusers:
        if i != conn:
            i.send(f'2018349872 {addr}'.encode())
        if i == conn:
            h = [i.send(f'2018349872 {x}'.encode()) for x in users if x != addr]
