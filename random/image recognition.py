import pyautogui
import time

while True:
    if pyautogui.locateOnScreen('Skjermbilde.png', confidence=0.8) != None:
        print('yes')
        time.sleep(.5)
    else:
        print('no')
        time.sleep(.5)

    
