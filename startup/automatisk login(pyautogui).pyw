import pyautogui
import time

bilde=None

while bilde is None:
    bilde = pyautogui.locateOnScreen('C:/Users/fipha001/OneDrive - Oslo Kommune Utdanningsetaten/py/Skjermbilde (11).png', confidence=0.6)
if bilde != None:
    x, y = pyautogui.center(bilde)
y -= 50
pyautogui.click(x, y)
pyautogui.typewrite('fipha001')
pyautogui.typewrite(['tab'])
