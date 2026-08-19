import random

class Lag:
    def __init__(self, land):
        self.land = land
        self.poeng = 0
        self.scoret = 0
        self.målsluppetinn = 0
        self.kamper = []
        
    def oversikt(self):
        print(f'Poeng: {self.poeng} \nScoret: {self.scoret} \nMål sluppet inn: {self.målsluppetinn} \nkamper: {self.kamper}')

    def update(self, scoret, målsluppetinn):
        self.scoret += scoret
        self.målsluppetinn += målsluppetinn
        
        if scoret == målsluppetinn:
            self.kamper.append('uavgjort')
            self.poeng += 1
        elif scoret > målsluppetinn:
            self.kamper.append('seier')
            self.poeng += 3
        else:
            self.kamper.append('tap')

        
class Kamp:
    def __init__(self, lag1, lag2):
        self.lag1 = lag1
        self.lag2 = lag2
        self.lag1scoret = random.randint(0, 7)
        self.lag2scoret = random.randint(0, 7)
        lag1.update(self.lag1scoret, self.lag2scoret)
        lag2.update(self.lag2scoret, self.lag1scoret)
        
    def resultat(self):
        print('Kamp!')
        print(f'{self.lag1.land} scorte {self.lag1scoret} mål!\n{self.lag2.land} scorte {self.lag2scoret} mål!')
            
class Gruppe:
    def __init__(self, lag1, lag2, lag3, lag4):
        self.lagliste = [lag1, lag2, lag3, lag4]
        self.kamper = []

    def spillkamper(self):
        for index, item in enumerate(self.lagliste):
            if index < len(self.lagliste):
                for i in self.lagliste[index+1::]:
                    kamp = Kamp(item, i)
                    self.kamper.append(kamp)
                    kamp.resultat()
                    
    def resultat(self):
        tabell = [(i.land, i.poeng, i.scoret - i.målsluppetinn) for i in self.lagliste]
        tabell.sort(key=lambda x: (x[1], x[2]))
        print(tabell)
        

norge = Lag('Norge')
frankrike = Lag('Frankrike')
tyskland = Lag('Tyskland')
england = Lag('England')

gruppe1 = Gruppe(norge, frankrike, tyskland, england)
gruppe1.spillkamper()
gruppe1.resultat()
        
    
