import pyperclip
import string
import keyboard

def clean():
    nummer = string.digits + string.punctuation
    s = pyperclip.paste()

    s = s.replace(' ', ',')
    s = s.split(' ')
    
    for i in s[0]:
        if i in nummer:
            s[0] = s[0].replace(i, ',')
        if i == '\n' or i == '\r' or i == '\t':
            s[0] = s[0].replace(i, ',')

    s[0] = s[0].split(',')
    navn = []

    for item in s[0]:
        if [letter in string.ascii_letters for letter in item]:
            navn.append(item)

    with open(r'C:\Users\fipha001\OneDrive - Osloskolen\py\ctrl + c cleaner\cleaned.txt', 'w') as file:
        for i in navn:
            file.write(f'{i},\n')

keyboard.add_hotkey('ctrl + c', clean)
