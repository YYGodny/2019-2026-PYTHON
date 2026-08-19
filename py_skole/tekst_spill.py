import random
import time
import sys


#####################funksjoner#####################

def sprint(x, t=.04):#printer ut med litt tid i mellom
    for i in x[:len(x)-1]:
        print(end=i)
        time.sleep(t)
    print(x[-1])


def finn_monster(boss=False):
    sjanse = random.randint(1, 4)
    if sjanse != 4:#sjanse for å møte monster
        tenke = True
        while tenke:#valg om slåss eller ikke
            if player1.health > (player1.max_health/100)*90 and boss == False:#hvis du har over 90 prosent liv, og det ikke er boss
                tenke = False#må slåss
                kjempe = True
                continue
            x = input('Du fant et monster! vil du ha kamp!? (ja/nei): ')
            if x.lower() == 'nei':
                kjempe = False
                tenke = False
            elif x.lower() == 'ja':
                kjempe = True
                tenke = False
        if kjempe == True:
            if boss == True:
                m = monster(random.randint(levl.md[0][0],levl.md[0][1]), random.randint(levl.md[1][0], levl.md[1][1]), random.randint(levl.md[2][0], levl.md[2][1]), boss=True)#monster
            elif boss != True:
                m = monster(random.randint(levl.md[0][0],levl.md[0][1]), random.randint(levl.md[1][0], levl.md[1][1]), random.randint(levl.md[2][0], levl.md[2][1]))#monster
            m.battle()#slåss funksjon
    else:
        sprint(f'Du fant ingen monstre')#hvis man ikke finner monster
        
######################################################
        
######################klasser#########################

###sverd, rustning, skjold og drikker###
class ting: 
    def __init__(self):
        self.sverd = {
            'stein sverd' : [100, 10], #første element i listen er sjansen for å få tingen (ikke i prosent), andre element er attack/skade
            'gull sverd' : [55, 20],
            'diamant sverd': [22, 30],
        }
        self.rustning = {
            'plastikk hansker' : [100, 7],#første element i listen er sjansen for å få tingen (ikke i prosent), andre element er health
            'lær jakke' : [40, 20],
            'metall rustning' : [20, 35],
        }

        self.skjold = {
            'en stor stein' : [100, 15],#første element i listen er sjansen for å få tingen (ikke i prosent), andre element er ekstra health
            'en gull tallerken' : [30, 23],
        }
        self.drikke = {
            'en rød flaske' : [100, 15],#første element i listen er sjansen for å få tingen (ikke i prosent), andre element er ekstra health
            'en blå flaske' : [40, 25],
        }
        self.skade_drikke = {
            'en ond lilla flaske' : [100, 33],
            'den verste syren' : [30, 47],
        }

    def finn_loot(self, t='sverd og rustning', sjans=0):#funksjon for å finne sverd, rustning, skjold eller drikke
        d = []
        if sjans == 0:
            sjans = random.randint(1, 100)
        if sjans >= 45:#sjanse for å få noe
            if random.randint(1, 100) >= 50:#sjanse for om du skal få rustning eller sverd
                s = random.randint(1, 100)#sjanse for hva du skal få
                if t == 'sverd og rustning':
                    g = self.sverd.items()
                elif t == 'skjold og potion':
                    g = self.skjold.items()
                for i in g:
                    if s <= i[1][0]:
                        d = []
                        d.append(i[0])
                        d.append(i[1][1])
                return d
            else:
                if t == 'sverd og rustning':
                    g = self.rustning.items()
                elif t == 'skjold og potion':
                    g = self.drikke.items()
                    if player1.stage >= 3:
                        g = random.choice([self.drikke.items(), self.skade_drikke.items()])
                s = random.randint(1, 100)#sjanse for hva du skal få
                for i in g:
                    if s <= i[1][0]:
                        d = []
                        d.append(i[0])
                        d.append(i[1][1])
                return d
        else:
            return d


###spilleren###
class player: 
    def __init__(self):
        #stats
        self.max_health = 100
        self.health = 100
        self.attack = 5
        self.speed = 35
        self.sverd = ' '
        self.rustning = ' '
        self.skjold = ' '
        #andre egenskaper
        self.attacks_not_learned = {'kast sverd':[2, 15], 'to skadedrikker på en gang' : [2, 10], 'ultimat fart': [25, 70]}
        self.attacks = {'slå': [8, 5], 'sparke' :[3, 10]}#angrepene, med en liste som viser, først ekstra skade, så ekstra hastighet
        self.inventory = []
        self.monsters_defeated = 0
        self.boss_defeated = 0
        self.living = True
        self.stage = 1

    def show_inv(self):
        sprint('INVENTORY:\n')
        if self.inventory == []:
            print('TOMT')
            return
        for i in self.inventory:
            t = i[0]#navn på tingen
            t1 = i[1]#egenskapen
            if t in ting1.sverd:
                print(f'{t} +{t1} attack')
                continue
            if t in ting1.skade_drikke:
                print(f'{t} tar {t1} skade')
                continue
            elif t in ting1.rustning or ting1.skjold or ting1.drikke:
                print(f'{t} +{t1} health')
        print('\n')    

    def mist_sverd(self):
        for i in self.inventory:
            if self.sverd == i:
                self.attack -= i[1]
        self.inventory.remove(self.sverd)#fjerne fra inventory
        self.sverd = ' '
        return True
                      
    def kast_sverd(self, sverd):
        if self.sverd == ' ':#hvis du ikke bruker sverd
            return False
        return sverd[1]*2#skjekke om sverdet er inni inventory og gange angrepet med 2

    def kast_dobbel_drikke(self):
        antall = []#antall skade drikker inni ditt inventory
        for i in self.inventory:
            if i[0] in ting1.skade_drikke:
                antall.append(i)
        if len(antall) >= 2:
            self.inventory.remove(antall[0])
            self.inventory.remove(antall[1])
            return antall[0][1]+antall[1][1]
        else:
            return False
    
    def use(self, greie, in_battle=False): #funksjon for å bruke ting
        for i in self.inventory:#skjekker om det tingen finnes inni inventory
            if i[0] == greie:
                greie = i #lager en variabel til tingen man skal bruke
                print(greie)
        if greie[0] in ting1.sverd and in_battle == False:#hvis det er et sverd
            if self.sverd == ' ':#hvis man ikke bruker et sverd
                self.attack += greie[1]#adderer sverdet sitt attack med egen attack
                sprint(f'DU BRUKER: {greie[0]}!')#printer ut
                print(f'+{greie[1]} attack!')
                self.sverd = greie#gjør at man bruker et sverd
            elif self.sverd != ' ':#hvis man bruker et sverd
                self.attack -= self.sverd[1]#subtraherer det egen attack sin attack med gammelt sverd
                self.attack += greie[1]#adderer det nye sverdet sin attack med egen attack
                sprint(f'DU BRUKER: {greie[0]}!')#printer ut
                if self.attack -(self.attack - greie[1] + self.sverd[1]) < 0: #hvis det er minus tall
                    print(f'{self.attack -(self.attack - greie[1] + self.sverd[1])} attack!')
                    self.sverd = greie#bruker ny sverd
                else:
                    print(f'+{self.attack -(self.attack - greie[1] + self.sverd[1])} attack!')
                    self.sverd = greie#bruker ny sverd
        elif greie[0] in ting1.rustning and in_battle == False:#hvis det er en rustning
            if self.rustning == ' ':#hvis man ikke bruker en rustning
                self.health += greie[1]#adderer rustningen sin health, med egen health
                self.max_health += greie[1]#adderer rustningen sin health, med maks health
                sprint(f'DU BRUKER: {greie[0]}!')#printer ut
                print(f'+{greie[1]} health!')
                self.rustning = greie#bruker rustning
            elif self.rustning != ' ':#hvis man allerede bruker en rustning
                self.health -= self.rustning[1]#subtraherer egen health med gammel rustning
                self.health += greie[1]#legger på ny rustning sin health med egen health
                self.max_health -= self.rustning[1]#subtraherer egen maks health med gammel rustning
                self.max_health += greie[1]#legger på ny rustning sin health med egen maks health                
                sprint(f'DU BRUKER: {greie[0]}!')#printer ut
                if self.health - (self.health - greie[1] + self.rustning[1]) < 0:#hvis det er minus tall
                    print(f'{self.health - (self.health - greie[1] + self.rustning[1])} health!')
                    self.rustning = greie#bruker rustning
                else:
                    print(f'+{self.health - (self.health - greie[1] + self.rustning[1])} health!')
                    self.rustning = greie#bruker rustning
        elif greie[0] in ting1.skjold:#hvis det er skjold
            if in_battle == True:
                if self.skjold == ' ':#hvis man ikke bruker et skjold
                    sprint(f'DU BRUKER: {greie[0]}!')
                    print(f'+{greie[1]} health!')
                    self.skjold = greie#bruker skjold
                    self.inventory.remove(greie)#fjerner fra inventory
                elif self.skjold != ' ':#hvis man bruker et skjold 
                    sprint('Du bruker allerede et skjold som ikke er ødelagt')
            elif in_battle == False:
                sprint('Du kan bare bruke skjold når du er i kamp')
        elif greie[0] in ting1.drikke:#hvis det er drikke
            if self.health >= self.max_health:#hvis man har maks health
                sprint('Du har allerede maks health')
            else:
                if self.health + greie[1] > self.max_health:#hvis man får over max health av drikken
                    sprint(f'DU BRUKER: {greie[0]}')
                    print(f'+{greie[1]-((self.health + greie[1])- self.max_health)} health')
                    self.health = self.max_health
                    self.inventory.remove(greie)#fjerner fra inventory
                else:
                    self.health += greie[1]#addere egen health og drikken sin ekstra health
                    sprint(f'DU BRUKER: {greie[0]}')
                    print(f'+{greie[1]} health')
                    self.inventory.remove(greie)#fjerner fra inventory
        else:
            sprint('Det finnes ikke inni ditt inventory')

    def stats(self):
        print(f'health: {self.health}/{self.max_health}\nattack: {self.attack}\nspeed: {self.speed}\nsverd: {self.sverd[0]}\nrustning: {self.rustning[0]}')
        if self.skjold != ' ':
            print(f'skjold: {self.skjold[0]}, tåler {self.skjold[1]} skade!')
        else:
            print('skjold: ')
        print(f'monstre drept: {self.monsters_defeated}\nbosser drept: {self.boss_defeated}\nbane: {self.stage}')

    def boost(self, h, a, s):
        self.health += h
        self.max_health += h
        self.attack += a
        self.speed +=s
        print(f'+{h} health!\n+{a} attack!\n+{s} speed!')

###baner###
class level:
    def __init__(self):
        self.baner = {'et slott' : [['stort', 'fint', 'gammelt'], ['en stor spise hall', 'et gigantisk soverom', 'lageret med gull']], #bane og adjektiv og steder til banen
                      'et hus' : [['ødelagt', 'mørkt', 'livløst'], ['et gammelt soverom med ødalgte vinduer', 'kjøkkenet med kniver som har blod på', 'kjelleren med en død kropp']],
                      'et fjell' : [['åpent', 'lyst', 'grønt'], ['et stort tre', 'et hjørne med mange skarpe busker', 'et ødalgt kloster']],
                      'en grotte' : [['fuktig', 'stille', 'mørk'], ['et mørkt rom som ser ut som et fengsel', 'et dypt mørkt hull', 'et fuktig hjørne']],
                      'en himmel' : [['hvit', 'fredfull', 'lys'], ['et stort gult og hvit palass', 'de myke skyene', 'et hus som ligner på ditt']]
                      }
        self.md = [[70, 90], [2, 8], [5, 25]]#første element i listen er hvor mye health et monster kan ha. Andre element er hvor mye attack den kan ha. Siste er hvor mye speed.

    def bane(self, b):
        self.md = [(self.md[0][0]+(b*20), self.md[0][1]+(b*20)), (self.md[1][0]+(b*5), self.md[1][1]+(b*5)), (self.md[2][0]+(b*15), self.md[2][1]+(b*15))]#monstrene blir sterkere jo mer baner
        self.rom = random.choice(list(self.baner.items()))
        self.baner.pop(self.rom[0])
        self.ordkjønn = self.rom[0].split(' ')[0]#for å få "en" eller "et"
        self.substantiv = self.rom[0].split(' ')[1]#for å få rommet, uten "en" og "et"
        sprint(f'Du befinner deg i {self.ordkjønn} {self.rom[1][0][random.randint(0, 2)]} {self.substantiv}')
        sprint(f'Du må bekjempe 3 monstre og 1 boss for å komme til neste bane')
        in_level = True
        while in_level:
            if player1.living == False: sys.exit()#hvis man dør
            if player1.monsters_defeated >= 3 and player1.boss_defeated >= 1:#hvis man slår 3 monstre og 1 boss(deretter skal man komme til neste bane eller vinne spillet)
                time.sleep(2)
                player1.stage += 1#neste bane
                if player1.stage >= 5:#hvis man har klart siste bane
                    print('\n')
                    sprint('GRATULERER!!!')
                    sprint('DU HAR OVERLEVD ALLE BANENE!!!')
                    sys.exit()
                player1.attacks[list(player1.attacks_not_learned.items())[b-1][0]] = list(player1.attacks_not_learned.items())[b-1][1]#legge til nytt angrep
                sprint(f'DU LÆRTE ET NYTT ANGREP!: {list(player1.attacks_not_learned.items())[b-1][0]}')#printe at man lærte et nytt angrep
                player1.attacks_not_learned.pop(list(player1.attacks_not_learned.items())[b-1][0])#fjerne fra listen med angrep som man ikke har lært                    
                sprint('DU HAR KOMMET TIL NESTE BANE!!!')
                player1.monsters_defeated = 0
                player1.boss_defeated = 0
                in_level = False
                return
            x = input('Hva skal du gjøre: ')
            j = ''
            if 'bruk ' in x:
                ting = x.split('bruk ')
                if len(ting) < 1:
                    player1.use(ting[0])
                else:
                    player1.use(ting[1])
            if x == 'kast terning':#"kaster terningen"
                j = random.randint(1, 6)#får tilfeldig tall
            if 'kast terning ' in x:#hvis spilleren bruker kast terning + et tall de vil ha høyere sjanse til å få
                x = x.split('kast terning')[1]#tallet
                try:#tester om brukeren har skrevet noe feil
                    int(x)
                except:
                    continue
                if int(x) in range(1, 7):
                    sjansetall = random.randint(1, 3)#sjanse for å få det ønskede tallet
                    if sjansetall == 3:
                        j = int(x)
                    elif sjansetall != 3:
                        j = random.randint(1, 6)
            if j == 1:
                print(1)
                time.sleep(.5)
                #printer hvor du leter
                sprint(f'du går rundt i {self.rom[1][1][random.randint(0, 2)]}')
                sprint('...', .5)
                sjanse = random.randint(1, 100)
                #print(sjanse)
                if sjanse >=70:
                    sprint('Det var ingen monstre eller ting å finne, denne gangen')
                elif sjanse < 70 and sjanse > 30:
                    #finne ting
                    t = ting1.finn_loot()
                    if t == []:
                        sprint('Du fant ingenting')
                        continue
                    player1.inventory.append(t)
                    sprint(f'Du fikk {t[0]}!')
                elif sjanse < 30:
                    #finne monster
                    finn_monster()
                    
            if j == 2:
                print(2)
                finn_monster()
            if j == 3:
                print(3)
                sprint('Du prøver å finne et sverd eller rustning')
                sprint('...', .5)
                t = ting1.finn_loot()
                if t == []:
                    sprint('Du fant ingenting')
                    sprint('Kanskje neste gang?')
                    continue
                player1.inventory.append(t)
                sprint(f'Du fikk {t[0]}!')                
            if j == 4:
                print(4)
                sprint('Du drikker en trylle drikk!')
                player1.boost(random.randint(5, 10), random.randint(1, 5), random.randint(3, 8))
            if j == 5:
                print(5)
                sprint('Du leter etter et skjold eller en trylledrikk')
                sprint('...', .5)
                t = ting1.finn_loot('skjold og potion')
                if t == []:
                    sprint('Det er ikke din lykke dag')
                    sprint('Eller er det?')
                    continue
                player1.inventory.append(t)
                sprint(f'Du fant {t[0]}!')
            if j == 6:
                print(6)
                sprint('Du ser en boss!')
                sprint('...', .5)
                sb = random.randint(1, 2)
                if sb == 1:
                    finn_monster(True)
                else:
                    sprint('Den løp...')
            elif x == '/help':
                print(f'''
                    1.skriv "kast terning" for å:
                    \n1. gå rundt
                    \n2. prøve å finne et monster
                    \n3. prøve å finne rustning eller et sverd
                    \n4. få bedre stats
                    \n5. prøve å finne skjold eller en trylle drikk
                    \n6. liten sjanse for å finne en boss\n
                    (Du kan også skrive "kast terning (1-6)" for å få høyere sjanse for å få tallet du ønsker")\n
                    2.skriv "stats" for å finne ut dine stats\n
                    3.skriv "inventory" for å se på ditt inventory\n
                    4.skriv "bruk (ting)" for å bruke noe inni ditt inventory\n
                    '''
                    )
            elif x == 'stats':
                player1.stats()
            elif x == 'inventory':
                player1.show_inv()
            else:
                continue
            
###monster###
class monster:
    def __init__(self, health, attack, speed, monster=0, boss=False):
        if monster == 0: monster = random.randint(0, 4)#random monster, hvis man ikke har satt inn et annet argument i funksjonen
        self.boss = boss
        if self.boss == False:
            self.health = health
            self.attack = attack
            self.speed = speed
        elif self.boss == True:
            self.health = int(health*1.7)
            self.attack = int(attack*1.7)
            self.speed = int(speed*1.7)
        self.alive = True
        monsterer = {
            'en heks': ['bruker en trylleformel på deg', 'forvandler foten din til en sopp', 'kaster en sint svart katt på deg'],
            'en drage': ['spruter ild på deg', 'slår deg med den kraftfulle halen sin', 'kaster en stor stein på deg'],
            'en trollmann': ['skyter en magisk blå flamme mot deg', 'får det til å regne syre over deg', 'slår deg med staven sin'],
            'en dverg': ['gjør deg deprimert', 'kaster mange steiner på deg', 'hopper på hodet ditt og slår deg mange ganger i ansiktet'],
            'et troll': ['slår deg med en stor klubbe', 'slår et kraftig slag i magen din', 'hopper på foten din']
            }
        ekstra_adjektiv = ['kjempe stor', 'skummel', 'blodtørstig', 'klok']
        self.ea = random.choice(ekstra_adjektiv)#random ekstra adjektiv
        self.monster = list(monsterer.items())[monster]
        self.navn = self.monster[0].split(' ')[1]#monsteret (uten "et" eller "en")
        self.ordkjønn = self.monster[0].split(' ')[0]#får "en" eller "et"

    def battle(self):
        if self.boss == True:
            sprint('BOSS!')
            if self.ordkjønn == 'et': self.ea += 't'#legge på en 't' på slutten av adjektivet
            sprint(f'Du møter {self.ordkjønn} {self.ea} {self.navn}!!!')
        elif self.boss == False:
            sprint(f'Du møter {self.ordkjønn} {self.navn}')
        sprint('stats:')
        sprint(f'attack: {self.attack}')
        sprint(f'health: {self.health}')
        sprint(f'speed: {self.speed}')
        while self.alive:
            miste_sverd = False#om man har mistet sverdet sitt
            har_skade_drikke = False#om man bruker skadedrikke
            print(f'\nTING DU KAN GJØRE:')
            [print(f'Attack: {i}') for i in player1.attacks]#printer ut angrepene til player1
            [print(f'Attack: {i[0]}') for i in player1.inventory if i[0] in ting1.skade_drikke]#printer ut skadedrikkene til player1
            [print(f'Du kan bruke: {i[0]}') for i in player1.inventory if i[0] in ting1.skjold or i[0] in ting1.drikke]#printer drikker og skjold inni inventory
            x = input('\nhva skal du gjøre: ')
            ##hvis player1 vil bruke skjold eller drikke##
            if x in ting1.skjold or x in ting1.drikke or 'bruk ' in x:
                if 'bruk ' in x:#hvis brukeren har skrevet "bruk" foran 
                    ting = x.split('bruk ')
                    if len(ting) < 1:
                        player1.use(ting[0], in_battle=True)
                    else:
                        player1.use(ting[1], in_battle=True)
                elif x in ting1.skjold:#hvis det er skjold
                    player1.use(x, in_battle=True)
                elif x in ting1.drikke:#hvis det er drikke
                    player1.use(x, in_battle=True)
                continue
            ##hvis player1 bruker skade drikke##
            if x in ting1.skade_drikke:
                for i in player1.inventory:#skjekker om det er inni player1 sitt inventory
                    if i[0] == x:
                        har_skade_drikke = True
                        x = i[0]#lager en variabel med navnet til skadedrikken
                        x_skade = i[1]#lager en varibel med skaden til skadedrikken
                        player1.inventory.remove(i)
            ##attacks##
            if x in player1.attacks or har_skade_drikke == True:
                if har_skade_drikke == False:
                    ps = player1.speed + player1.attacks[x][1]#player sin total speed
                    pa = player1.attack + player1.attacks[x][0]#player sin total attack
                elif har_skade_drikke == True:
                    pa = x_skade
                    ps = player1.speed
                ms = self.attack + int((self.attack/100)*random.randint(-22, 22))#monsteret sin attack
                if x == 'to skadedrikker på en gang':#hvis player bruker angrepet "bruk to skadedrikker på en gang"
                    if player1.stage >= 3:
                        pa = player1.kast_dobbel_drikke()
                        if pa == False:
                            print('Du har ikke to skade drikker inni ditt inventory')
                            continue#starter loop om igjen
                            self.alive = True#starter loop om igjen
                    elif player1.stage < 3:
                        print('kan ikke bruke dette angrepet')
                        continue
                        self.alive = True
                if x == 'kast sverd':#hvis player bruker angrepet "kast sverd"
                    pa = player1.kast_sverd(player1.sverd)
                    if pa == False:
                        print('Du har ikke et sverd!')
                        continue#starter loop om igjen
                        self.alive = True#starter while loopen om igjen
                    sjanse_miste_sverd = random.randint(1, 3)
                    if sjanse_miste_sverd == 2:#sjanse for å miste sverdet
                        miste_sverd = player1.mist_sverd()
                if ps > self.speed:#hvis spilleren sin speed er høyere enn monsteret sin speed
                    #ditt angrep
                    sprint(f'Du brukte: {x}')
                    sprint(f'{self.navn}{self.ordkjønn} tok {pa} skade\n')
                    if miste_sverd == True:
                        sprint('DU MISTET SVERDET DITT')
                    self.health -= pa
                    if self.health <= 0:
                        if self.boss == True:
                            sprint(f'Du Drepte {self.navn} bossen!')
                            t = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra bossen
                            t1 = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra bossen
                            t2 = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra bossen
                            sprint(f'MONSTERET DROPPET:\n{t}\n{t1}\n{t2}')
                            player1.inventory.append(t)
                            player1.inventory.append(t1)
                            player1.inventory.append(t2)
                            self.alive = False
                            player1.boss_defeated += 1
                            return
                        elif self.boss == False:
                            sprint(f'DU DREPTE {self.navn}{self.ordkjønn}')
                            t = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra monsteret
                            sprint(f'MONSTERET DROPPET: {t}')
                            player1.inventory.append(t)
                            self.alive = False
                            player1.monsters_defeated += 1
                            return
                    sprint(f'{self.navn}{self.ordkjønn} har {self.health} liv igjen!\n')
                    #monsteret sitt angrep
                    sprint(f'{self.navn}{self.ordkjønn} {random.choice(self.monster[1])}')
                    if player1.skjold != ' ':
                        self.skad_skjold(ms)
                    elif player1.skjold == ' ':
                        sprint(f'Det tok {ms} skade!')
                        player1.health -= ms
                    if player1.health <= 0:
                        sprint('DU DØDE!')
                        player1.living = False
                        return
                        sys.exit()
                    sprint(f'Du har {player1.health}/{player1.max_health} igjen!')
                elif ps < self.speed: #hvis monsteret sin speed er høyere en spilleren sin speed
                    #monsteret sitt angrep
                    sprint(f'{self.navn}{self.ordkjønn} {random.choice(self.monster[1])}')
                    if player1.skjold != ' ':
                        self.skad_skjold(ms)
                    elif player1.skjold == ' ':
                        sprint(f'Det tok {ms} skade!')
                        player1.health -= ms
                    if player1.health <= 0:
                        sprint('DU DØDE')
                        player1.living = False
                        return
                        sys.exit()
                    sprint(f'Du har {player1.health}/{player1.max_health} igjen!')
                    print('\n')
                    #ditt angrep
                    sprint(f'Du brukte: {x}')
                    sprint(f'{self.navn}{self.ordkjønn} tok {pa} skade\n')
                    if miste_sverd == True:
                        sprint('DU MISTET SVERDET DITT')
                    self.health -= pa
                    if self.health <= 0:
                        if self.boss == True:
                            sprint(f'Du Drepte {self.navn} bossen!')
                            t = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra bossen
                            t1 = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra bossen
                            t2 = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra bossen
                            sprint(f'MONSTERET DROPPET:\n{t}\n{t1}\n{t2}')
                            player1.inventory.append(t)
                            player1.inventory.append(t1)
                            player1.inventory.append(t2)
                            self.alive = False
                            player1.boss_defeated += 1
                            return
                        elif self.boss == False:
                            sprint(f'DU DREPTE {self.navn}{self.ordkjønn}')
                            t = ting1.finn_loot(random.choice(['skjold og potion', 'sverd og rustning']), 100)#ting man får fra monsteret
                            sprint(f'MONSTERET DROPPET: {t}')
                            player1.inventory.append(t)
                            self.alive = False
                            player1.monsters_defeated += 1
                            return
                    sprint(f'{self.navn}{self.ordkjønn} har {self.health} liv igjen!\n')
                
            else:
                print('du skrev noe feil')
                
    def skad_skjold(self, skade):
        player1.skjold[1] -= skade
        if player1.skjold[1] == 0:#hvis skjoldet blir perfekt ødelagt, uten at det blir minus
            player1.skjold = ' '
            sprint('Skjoldet ditt ble ødelagt!')
        elif player1.skjold[1] < 0:#hvis skjoldet har minus ekstra health
            player1.skjold[1] *= -1 #for å gjøre det til positivt tall
            player1.health -= player1.skjold[1]
            sprint('Skjoldet ditt ble ødelagt!')
            sprint(f'Du tok {player1.skjold[1]} skade!')
            player1.skjold = ' '
        else:#hvis skjoldet ikke blir ødelagt
            sprint(f'skjoldet ditt tok {skade} skade')
            sprint(f'{player1.skjold[0]} tåler {player1.skjold[1]} skade!')

########################################################
            
#objekter
player1 = player()
levl = level()
ting1 = ting()

print('Skriv /help for å se hva du kan gjøre')
#game loop
while True:
    if player1.living == True:
        levl.bane(player1.stage)
