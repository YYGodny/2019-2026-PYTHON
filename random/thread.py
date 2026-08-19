import threading
import time

def hei(hvem):
    print(f'hei {hvem}')

thread = threading.Thread(target=hei, args=('Filip',))

print('hei')
thread.start()

a = 1
if a == 1:
    print(' :sup')

    
