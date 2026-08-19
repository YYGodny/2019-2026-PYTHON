import socket
import threading
import tkinter as tk
from tkinter import ttk
import random
from functools import partial

s = socket.socket()
port = 7462
host = socket.gethostbyname(socket.gethostname())

s.connect((host, port))

textbox = ''
person = ''
root = tk.Tk()

def stop_messaging(x):
    s.send('7283462103'.encode())
    [online[i].pack() for i in online]
    person.destroy()

def message_person(x):
    global person
    [online[i].pack_forget() for i in online]
    print(f'messaging {x[1:]}')
    s.send(x[1:].encode())
    person = ttk.Button(root, text=f'Stop messaging', command=partial(stop_messaging, x))
    person.pack()

online = {}    
def receive():
    global online
    while True:
        x = s.recv(1024).decode()
    
        #receives addr from server and prints on screen
        if '2018349872' in x:
            j = x.split('2018349872')
            print(f'{j[1]} er online!')
            online[f'{j[1]}'] = ttk.Button(root, text=j, command=partial(message_person, f'{j[1]}'))
            online[f'{j[1]}'].pack()
            print(online)
            continue
        #removes addr from screen
        if '123487621' in x:
            j = x.split('123487621')
            print(f'{j[1]} er borte')
            online[f'{j[1]}'].destroy()
            del online[f'{j[1]}']
            continue

        textbox.config(state='normal')
        textbox.insert('end', f'{x}\n')
        textbox.config(state='disabled')
        print(f'from server: {x}')

def show_active():
    pass

def main():
    global root, textbox
    #screen
    root.title('Message')
    root.geometry('700x500+200+100')
    #send message
    message = tk.StringVar()
    messagebox = ttk.Entry(root, textvariable=message).pack()
    def send():
        print(message.get())
        s.send(message.get().encode())
    se = ttk.Button(root, text='Send', command=send)
    #se.bind('<Return>', send)
    se.focus()
    se.pack(expand=True)
    #scrollbar/textinput
    textbox = tk.Text(root, height=10)
    textbox.pack()   
    scrollbar = ttk.Scrollbar(
        root,
        orient='vertical',
        command=textbox.yview
        )
    scrollbar.pack()
    
    textbox['yscrollcommand'] = scrollbar.set
    root.mainloop()

th1 = threading.Thread(target=receive)
th1.daemon = True
th1.start()
main()
