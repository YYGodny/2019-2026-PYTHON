import os
import shutil
import time
import pathlib
import keyboard
from tkinter import *
from plyer import notification

path = r'C:\Users\fipha001\OneDrive - Oslo Kommune Utdanningsetaten'
d_path = r'C:\Users\fipha001\OneDrive - Oslo Kommune Utdanningsetaten\9d'

os.chdir(path)

directories = os.listdir(path)[1::1]

'''
with os.scandir(path) as dirs:
    for entry in dirs:
        print(entry.name)
'''

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r'C:\Users\fipha001\Pictures\banana joe.ico',
        timeout=10,
    )

notification1 = True

    
def notification2():
    def nei():
        global notification1
        notification1 = False
        output.delete(0.0, END)
        output.insert(END, f'Notification er {notification1}')
        
    def ja():
        global notification1
        notification1 = True
        output.delete(0.0, END)
        output.insert(END, f'Notification er {notification1}')
        
    window = Tk()
    window.title('File Cleaner Notification')
    
    Label (window, text='Notification Ja/Nei?', font='none 12 bold').grid(row=0, column=0)

    output = Text(window, width=21, height=2, wrap=WORD, background='white')
    output.grid(row=2, column=0)

    Button(window, text='Ja', command=ja, height=1, width=23).grid(row=1, column=0)
    Button(window, text='Nei', command=nei, height=1, width=23).grid(row=1, column=1)
    
    window.mainloop()

q = 0
entry1 = ''
def duplicate(file):
    global q
    ftype = pathlib.Path(file).suffix
    def rename():
        global q, entry1
        q += 1
        if q == 1:
            text1.set('Hva vil du den skal hete?')
            entry1 = Entry(window, width=10)
            entry1.grid(row=1, column=2)
        if q == 2:
            h = entry1.get()
            print(h)
            os.rename(file, f'{d_path}\\{h}{ftype}')
            print('Renamed!')
            notifyme('Renamed!', f'Renamed {file}')
            q = 0
            window.destroy()
    def slett():
        def ja1():
            os.remove(file)
            print('Removed!')
            notifyme('Removed!', f'Removed {file}')
            window.destroy()
        def nei2():
            print('K')
            window.destroy()
        def nei1():
            text1.set('Vil du rename den?')
            button1 = Button(window, text='Nei', command=nei2, height=1, width=23).grid(row=1, column=0)
            button2 = Button(window, text='Ja', command=rename, height=1, width=23).grid(row=1, column=1)
        text1.set('Vil du slette den?')
        button1 = Button(window, text='Nei', command=nei1, height=1, width=23).grid(row=1, column=0)
        button2 = Button(window, text='Ja', command=ja1, height=1, width=23).grid(row=1, column=1)
    window = Tk()
    text1 = StringVar()
    text1.set(f'Fant duplicate, ok? "{file}')
    window.title('DUPLICATE')
    Label (window, textvariable=text1, font='none 12 bold').grid(row=0, column=0)
    button1 = Button(window, text='K', command=slett, height=1, width=23).grid(row=1, column=0)
    window.mainloop()
    
keyboard.add_hotkey('ctrl + alt + 1', notification2)


s = True
while s:
    try:
        os.chdir(path)
        directories = os.listdir(path)[1::1]
        print('Leter...')
        for file in directories:
            if os.path.isfile(file):
                if file == 'desktop.ini':
                    continue
                shutil.move(file, d_path)
                if notification1 == True:
                    notifyme('File', f'Moved {file}!')
                    print(f'Moved {file}!')
                else:
                    continue
        time.sleep(5)
        print('Gått en halv time! Og jeg har kjekket mappen!')
    except PermissionError:
        time.sleep(5)
        s = True
    except:
        if notification1 == True:
            duplicate(file)
            '''
            print('Fant duplicate!')
            ftype = pathlib.Path(file).suffix
            print(file)
            x = input('Greit?')
            x = input('Vil du slette den?')
            if x == 'ja':
                os.remove(file)
                print('Removed!')
            elif x == 'nei':
                x = input('Vil du rename den?')
                if x == 'ja':
                    h = input('hva vil du den skal hete?')
                    os.rename(file, f'{d_path}\\{h}{ftype}')
                    print('File renamed!')
                elif x == 'nei':
                    print('k')
            '''
            s = True
        else:
            time.sleep(5)
            s = True
