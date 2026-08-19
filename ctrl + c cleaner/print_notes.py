import pyperclip
import keyboard

def print_play():
    s = pyperclip.paste()
    with open(r'C:\Users\fipha001\OneDrive - Osloskolen\py\ctrl + c cleaner\play.txt', 'w') as file:
        s = s.split(' ')
        note = ''
        for i in s:
            note = i
            if i == '' or i == ' ':
                continue
            if '-' in i:
                n = i.split('-')
                for index, item in enumerate(n):
                    note = item
                    if '^' in item:
                        note = f'{item}5'
                        note = note.replace('^', '')
                    if '#' in item:
                        note = f'{item}s'
                        note = note.replace('#', '')
                    if '#' in item and '^' in item:
                        note = f'{item}s5'
                        note = note.replace('^', '')
                        note = note.replace('#', '')
                    file.write(f'play :{note}, release: 0.5\n')
                    if index != len(n)-1:
                        file.write('sleep(0.2)\n')
                    if index == len(n)-1:
                        file.write('sleep(0.5)\n')
                        
            else:
                note = i
                if '^' in i:
                    note = f'{i}5'
                    note = note.replace('^', '')
                if '#' in i:
                    note = f'{i}s'
                    note = note.replace('#', '')
                if '#' in i and '^' in i:
                    note = f'{i}s5'
                    note = note.replace('^', '')
                    note = note.replace('#', '')
                file.write(f'play :{note}, release: 0.5\n')
                file.write(f'sleep(0.5)\n')


keyboard.add_hotkey('ctrl + c', print_play)
