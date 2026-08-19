import keyboard
while True:
    a = False
    while keyboard.is_pressed('shift'):
        a = True
        if keyboard.is_pressed('page up'): keyboard.write('Y')
    if keyboard.is_pressed('page up') and a == False: keyboard.write('y')
    
