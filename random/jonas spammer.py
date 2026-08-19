import pyautogui as gui
import time
import keyboard

while True:
    bilde = gui.locateOnScreen('C:/Users/fipha001/Pictures/Screenshots/jonas.png', confidence=0.7)
    if bilde != None:
        tekst = gui.locateOnScreen('C:/Users/fipha001/Pictures/Screenshots/Skjermbilde (13).png', confidence=0.6)
        if tekst != None:
            x, y = gui.center(tekst)
            gui.click(x, y)
            gui.typewrite('hei')
            gui.typewrite(['enter'])
            if keyboard.is_pressed('q'):
                break
