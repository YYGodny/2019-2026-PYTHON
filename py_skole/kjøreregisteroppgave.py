import datetime
import random

def finnemax(liste):
    return max(set(liste), key=liste.count)

class kjøretøy:
    def __init__(self, rn, merke, modell, eier):
        self.rn = rn
        self.merke = merke
        self.modell = modell
        self.eier = eier

class bkjøretøy(kjøretøy):
    def __init__(self, rn, merke, modell, eier, drivstoff, tid = []):
        super().__init__(rn, merke, modell, eier)
        self.drivstoff = drivstoff
        self.kategori = 'bensin'
        self.tid = tid

class vkjøretøy(kjøretøy):
    def __init__(self, rn, merke, modell, eier, tid = []):
        super().__init__(rn, merke, modell, eier)
        self.kategori = 'elektrisk'
        self.tid = tid

class register:
    def __init__(self):
        self.innhold = {}

    def leggtil(self, kjøretøy):
        if kjøretøy.tid == []:
            kjøretøy.tid.append(datetime.date.today())
            kjøretøy.tid.append(datetime.datetime.now().time().strftime('%H:%M'))
        self.innhold[kjøretøy.rn] = {kjøretøy:[kjøretøy.tid[0], kjøretøy.tid[1]]}
        
    def dato(self, time=False):
        
        dager = [y[0] for i in self.innhold.values() for y in i.values()]
        mestdag = finnemax(dager)
        if time == False:
            return mestdag
        if time == True:
            mesttid = [y[1] for i in self.innhold.values() for y in i.values() if y[0] == mestdag]
            return finnemax(mesttid)

    def sjekkkjøretøy(self):
        kjøretøy = [y.kategori for i in self.innhold.values() for y in i.keys()]
        #if (x:=[kjøretøy.count(i) for i in set(kjøretøy)]) != set(x): print('like mange biler av de fleste biler')
        mestkjøretøy = finnemax(kjøretøy)
        kjøretøymerke = [y.merke for i in self.innhold.values() for y in i.keys()]
        mestkjøretøymerke = finnemax(kjøretøymerke)
        return mestkjøretøy, mestkjøretøymerke


##b1 = bkjøretøy('2134', 'toyota', '58g', 'hamod', 'bensin')
##b2 = bkjøretøy('45682134', 'ford', '50g', 'mahmod', 'diesel')
##b3 = vkjøretøy('7644', 'lambo', '7g', 'aro')
reg1 = register()

for i in range(100):
    b = bkjøretøy(random.randint(100, 1000), random.choice(['lambo', 'ford', 'toyota', 'nissan']), f'{random.randint(1, 100)}g', random.choice(['hamod', 'aro', 'filip', 'oliver']), random.choice(['bensin', 'diesel']), [datetime.date.today(), f'11:10:{random.randint(1, 10)}'])
    v = vkjøretøy(random.randint(100, 1000), random.choice(['lambo', 'ford', 'toyota', 'nissan']), f'{random.randint(1, 100)}g', random.choice(['hamod', 'aro', 'filip', 'oliver']), [datetime.date.today(), f'11:10:{random.randint(1, 10)}'])
    reg1.leggtil(random.choice([b, v]))
