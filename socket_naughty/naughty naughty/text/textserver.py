import socket
import time
import threading
#meldinger, notification, spam recognition, venner,

clients_conn = []
clients_addr = []
clients_pcnn = []
clients_port = []
clients_navn = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 29040
s.bind((host, port))

s.listen()

def show_online(x, c, a):
    c.send(f'ONLINE: '.encode())
    for index, name in enumerate(clients_navn):
        if index == x:
            continue
        c.send(f'{name}\n'.encode())

        
def handle_client(conn, addr, pcnn, port):
    while True:
        try:
            print(f'{addr} har connectet til serveren')
            #sjekker og appender ip addresser
            with open('clientsregistered.txt', 'r+') as f:
                file = f.readlines()

                for index, item in enumerate(file):
                    file[index] = item[:-1]
                    
                print(file)
                if len(file) > 0:
                    infile = False
                    for line in file:
                        if pcnn in line:
                            clients_navn.append(line.split(pcnn)[1][1::1])
                            egen_navn = line.split(pcnn)[1][1::1]
                            conn.send(f'hei {line.split(pcnn)[1][1::1]}'.encode())
                            print('in file')
                            infile = True
                    if infile != True:
                        conn.send('Hva heter du?'.encode())
                        data = conn.recv(1024).decode()
                        clients_navn.append(data)
                        f.write(f'\n{pcnn}={data}\n')
                    
                else:
                    conn.send('Hva heter du?'.encode())
                    data = conn.recv(1024).decode()
                    clients_navn.append(data)
                    f.write(f'{pcnn}={data}\n')
                    print('skrevet ny client!')
                print(clients_navn)
                
            #får navn index
            for index, item in enumerate(clients_addr):
                if item == addr:
                    navn_index = index
            #skjekker om det er duplicate clients
            '''
            if egen_navn in clients_navn:
                raise ConnectionResetError
            '''
            meldinger1 = True
            a = 0

            #meldinger       
            while meldinger1:
                if len(clients_navn) > 1:
                    show_online(navn_index, conn, addr)
                    meldinger2 = True
                    while meldinger2:
                        data = conn.recv(1024).decode()
                        if data.startswith('/') and len(data) > 2:
                            if 'so' == data[1:3].lower():
                                show_online(navn_index, conn, addr)
                                continue
                            elif 'help' == data[1:5].lower():
                                conn.send('skriv:\n/so hvis du vil se hvem som er online\n/m [navn] hvis du vil chatte med noen\n/stop hvis du vil stoppe å snakke med noen'.encode())
                                continue
                            elif 'm' == data[1].lower():
                                data = data.replace(' ', '')
                                data = data.replace('/m', '')
                                if data in clients_navn:
                                    for index, item in enumerate(clients_navn):
                                        if item == data:
                                            kamerat = index
                                    clients_conn[kamerat].send(f'{clients_navn[navn_index]} vil snakke med deg...\nJa/Nei\nOBS! DU MÅ SKRIVE JA ELLER NEI TO GANGER!'.encode())
                                    time.sleep(.5)
                                    m = True
                                    while m:
                                        data = clients_conn[kamerat].recv(1024).decode()
                                        if data.lower() == 'ja':
                                            conn.send(f'Du chatter med {clients_navn[kamerat]} :)'.encode())
                                            clients_conn[kamerat].send(f'XQC123ASD {navn_index}'.encode())
                                            q = True
                                            while q:
                                                data = conn.recv(1024).decode()
                                                if data.replace(' ', '').lower() == '/stop':
                                                    conn.send('ok'.encode())
                                                    clients_conn[kamerat].send('ingen liker deg :)'.encode())
                                                    clients_conn[kamerat].send('ABCEZ123'.encode())
                                                    q = False
                                                if data.startswith('ABCEZ1234'):
                                                    q = False
                                                if data.replace(' ', '').lower() == '/stop':
                                                    break
                                                clients_conn[kamerat].send(data.encode())
                                            m = False
                                        elif data.lower() == 'nei':
                                            conn.send('han vil ikke :('.encode())
                                            m = False
                                        else:
                                            clients_conn[kamerat].send('du skrev noe feil'.encode())
                                continue
                            
                            else:
                                continue
                            
                        
                    
                        elif data.startswith('XQC123ASD'):
                            kamerat2 = data.split('XQC123ASD ')[1]
                            kamerat2 = int(kamerat2)
                            while True:
                                data = conn.recv(1024).decode()
                                if data.replace(' ', '').lower() == '/stop':
                                    conn.send('ok'.encode())
                                    clients_conn[kamerat2].send('ingen liker deg :)'.encode())
                                    clients_conn[kamerat2].send('ABCEZ1234'.encode())
                                    break
                                if data.startswith('ABCEZ123'):
                                    break
                                clients_conn[kamerat2].send(data.encode())
                    
                        print(data)
                        if '/stop' in data:
                            continue
                        
                        if 'ABCEZ123' not in data:
                            for i in clients_conn:
                                if i != conn:
                                    i.send(data.encode())
                        
                        else:
                            continue
                            
                else:
                    if a == 0:
                        conn.send('venter på en person...'.encode())
                    a += 1
        except ConnectionResetError:
            clients_conn.remove(conn)
            clients_addr.remove(addr)
            clients_pcnn.remove(pcnn)
            clients_port.remove(port)
            clients_navn.remove(egen_navn)
            break
        except:
            break

chatting = True

while chatting:
    conn, addr = s.accept()
    data = conn.recv(1024).decode()
    clients_pcnn.append(data)
    clients_port.append(addr[1])
    port = addr[1]
    addr = addr[0]
    clients_conn.append(conn)
    clients_addr.append(addr)
    thread = threading.Thread(target=handle_client, args=(conn, addr, data, port))
    thread.daemon = True
    thread.start()

