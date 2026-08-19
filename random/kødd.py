import webbrowser
import time
import random

while True:
    sites = random.choice(['googe.com', 'mastercode.online', 'youtube.com', 'weather.gov'])
    visit = 'http://{}'.format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)
