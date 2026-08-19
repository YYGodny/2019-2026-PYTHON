import socket
import time
import threading

s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 29040
s.connect((host, port))

print('skriv /Help hvis du trenger hjelp.')
s.send(socket.gethostname().encode())
def get_message():
    massage = True
    while massage:
        data = s.recv(1024).decode()
        if data.startswith('XQC123ASD'):
            s.send(data.encode())
            continue
        elif data == 'ABCEZ123':
            s.send(data.encode())
            continue
        elif data == 'ABCEZ1234':
            s.send(data.encode())
            continue
        print(data)

thread = threading.Thread(target=get_message)
thread.daemon = True
thread.start()
while True:
    x = input()
    s.send(x.encode())
    
