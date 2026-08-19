import openpyxl
import keyboard 
from plyer import notification
import time

path = r'C:\Users\fipha001\OneDrive - Osloskolen\10d\rekke opp hånda.xlsx'

wb = openpyxl.load_workbook(path)
sheet = wb.active
antall = sheet.cell(row = 7, column = 3)

def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r'C:\Users\fipha001\OneDrive - Osloskolen\bilder\banana joe.ico',
        timeout=5,
    ) 

def pluss_value():
    antall.value += 1
    print(antall.value)
    notifyme('Rekke Opp hånda counter', f'Antall: {antall.value}')
    wb.save(path)
    
def minus_value():
    antall.value -= 1
    print(antall.value)
    notifyme('Rekke Opp hånda counter', f'Antall: {antall.value}')
    wb.save(path)
    
keyboard.add_hotkey('ctrl + shift + 1', pluss_value)
keyboard.add_hotkey('ctrl + shift + 2', minus_value)

inside = True
while inside:
    try:
        time.sleep(100)
        inside = True
    except:
        inside = True
inside = True
