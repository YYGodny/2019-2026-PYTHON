import random
import time


kortfarge = ['yellow ', 'blue ', 'red ', 'green ']
korttall = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
lagt_på = []

class player:
    def __init__(self):
        self.cards = []
        self.count = 0
        for i in range(8):
            kort = random.choice(kortfarge), random.choice(korttall)
            kort = list(kort)
            kort = ''.join(kort)
            self.cards.append(kort)
    def show_cards(self):
        print(self.cards)
        
    def trekk_kort(self):
        for i in range(3):
            kort = random.choice(kortfarge), random.choice(korttall)
            kort = list(kort)
            kort = ''.join(kort)
            self.cards.append(kort)
        print('trakk tre kort!')
    def legg_på_kort(self, k):
        
        legg_på_bok = ''
        legg_på_tall = k[-1]
        for i in k:
            legg_på_bok += i
            if i == ' ':
                break
        legg_på_bok = legg_på_bok.replace(' ', '')
        
        if lagt_på == []:
            lagt_på.append(k)
            for index, item in enumerate(self.cards):
                if item == k:
                    self.cards.pop(index)
                    break
            print(f'lagt på {k}!')
            
        elif legg_på_bok not in lagt_på[-1] and legg_på_tall not in lagt_på[-1]:
            print('du skrev noe feil og vi hopper over deg')
            
        elif legg_på_bok in lagt_på[-1] or legg_på_tall in lagt_på[-1]:
            for index, item in enumerate(self.cards):
                if item == k:
                    self.cards.pop(index)
                    break
            lagt_på.append(k)
            print(f'lagt på {k}!')
    def py_legg_på_kort(self):
        while True:
            pk = random.choice(self.cards)
            legg_på_bok = ''
            legg_på_tall = pk[-1]
            for i in pk:
                legg_på_bok += i
                if i == ' ':
                    break
            legg_på_bok = legg_på_bok.replace(' ', '')
            if legg_på_bok in lagt_på[-1] or legg_på_tall in lagt_på[-1]:
                print(f'python la på {pk}!')
                self.cards.remove(pk)
                lagt_på.append(pk)
                break
            elif self.count % 2 == 0:
                self.trekk_kort()
                break
            elif lagt_på[-1] not in self.cards:
                print('python må hoppe over')
                self.count += 1
                break
            else:
                continue

player1 = player()
python = player()

while True:
    print(f'dette er bonken: {lagt_på}')
    if player1.cards == []:
        print('du vant!')
        break
    if python.cards == []:
        print('python vant!')
        break
    print(f'dette er dine kort: {player1.cards}')
    x = input('legg på noe eller trekk kort: ')
    if 'trekk kort' in x:
        player1.trekk_kort()
        continue
    player1.legg_på_kort(x)
    time.sleep(1)
    python.py_legg_på_kort()
    time.sleep(1)
