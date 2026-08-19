import os
import shutil
import time
import pathlib

path = r'C:\Users\fipha001\OneDrive - Oslo Kommune Utdanningsetaten'
d_path = r'C:\Users\fipha001\OneDrive - Oslo Kommune Utdanningsetaten\8d'

os.chdir(path)

directories = os.listdir(path)[1::1]

'''
with os.scandir(path) as dirs:
    for entry in dirs:
        print(entry.name)
'''
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
                print(f'Moved {file}!')
        time.sleep(8)
        print('Gått en time!')
    except:
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
        s = True
