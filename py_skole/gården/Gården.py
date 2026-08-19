import time
import random
import threading
import pickle #for å lagre objektene enkelt
import functools

##########          Funksjoner          ##########

def åtd(å):
    return round(å*365)

def savegård():
    with open('savedfil.pkl', 'wb') as f: 
        pickle.dump(tuple([gårder[i] for i in gårder]), f)

def loadgård():
    with open('savedfil.pkl', 'rb') as f:
        loadedobjs = pickle.load(f)
        for i in loadedobjs:
            i.start()
            globals()[i.navn] = i
        print('loaded', loadedobjs)

def tryexcept(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print('noe feil skjedde')
            print('kanskje du glemte feltnavn?')
            print('kanskje du skrev dyret/avlingen feil?')
    return wrapper

def vær(self):
    t = random.randint(1, 40)
    if t == 1:
        print(f'Det regner på {self.navn}!')
        af = [i for i in self.felt if i.__class__.__name__ == 'Avlingsfelt']
        if not af:
            print('Gården har ingen avlinsfelt uansett!')
            return
        re = random.randint(0, len(af)+1) #en sjanse for å ikke påvirke noen avlingsfelt pga. "len(af)" ikke "len(af)-1"
        if re >= len(af):
            print('Ingen avlinger ble skadet av regnet!')
            return
        if all(i == [] for i in af[re].innhold.values()):
            print(f'Det var tordenvær på {af[re].navn}, men feltet har ingen avlinger uansett!')
            return
        sat = []
        while not sat:
            sat1 = random.choice(list(af[re].innhold.keys()))
            sat = af[re].innhold[sat1]
        sa = random.choice(sat)
        af[re].fjern(sa)
        print(f'Regnet ødela {sa.plante[0]} {sa.plante[1]}!')

##########          variabler          ##########

gårder = {}
visdyr = 'ingen'

##########          Gård         ##########

class Gård:
    def __init__(self, navn):
        self.navn = navn
        globals()[navn] = self
        self.felt = []
        self.produsert = []
        self.maxareal = 100
        self.areal = 0
        self.start()
        
    def start(self):
        thread = threading.Thread(target=self.hvertsekund, daemon=True)
        thread.start()
                   
    def hvertsekund(self):
        while True:
            time.sleep(0.5) #dager per sekund (endre denne for å gjøre prosesser raskere)
            for i in self.felt:
                i.oppdater()
            gårder[self] = self
            savegård()
            vær(self)#kommenter ut dette hvis du vil fjerne været

    def finnfelt(self, feltnavn):
        l = [i.navn for i in self.felt]
        if feltnavn not in l:
            print('Feltet finnes ikke')
            return False
        return self.felt[l.index(feltnavn)]
    
    def sjekkfelt(self, feltnavn, typefelt, p=True):
        if (felt:=self.finnfelt(feltnavn)):
            if typefelt == 'Avlingsfelt':
                if felt.__class__.__name__ == 'Avlingsfelt':
                    return felt
            if typefelt == 'Dyrefelt':
                if felt.__class__.__name__ == 'Dyrefelt':
                    return felt
            if p == True:
                print('Feil felt')
            return False

    @tryexcept    
    def oversikt(self, felt='alle'):
        print('--------------------------------------------')
        print(f'Arealet til gården: {self.areal}/{self.maxareal}!')
        print('--------------------------------------------')
        if self.felt:
            if felt == 'alle':
                for index, i in enumerate(self.felt):
                    if index > 0:
                        print('\n|--------------------------------------------|')
                    i.status()
            else:
                for index, i in enumerate(self.felt):
                    if index > 0:
                        print('\n|--------------------------------------------|')
                    if i.navn == felt:
                        i.status()
        else:
            print('Gården innholder ingenting')
            
    @tryexcept
    def vis(self, dyr='alle'):
        global visdyr
        if dyr in Dyr.dyreattributer.keys() or dyr in ['alle', 'ingen']:
            visdyr = dyr
            print(f'Viser {dyr}')
        else:
            print('Finnes ikke')
            
    @tryexcept        
    def leggtilfelt(self, felt):
        if felt.navn in [i.navn for i in self.felt]:
            print('Bruk et annet navn!')
            return
        if self.areal + felt.maxareal <= self.maxareal:
            self.felt.append(felt)
            self.areal += felt.maxareal
            print(f'Lagt til {felt.__class__.__name__}: {felt.navn}!')
        else:
            print(f'Du har ikke nok areal. Du har igjen: {self.maxareal - self.areal}kvadratmeter')

    @tryexcept
    def fjernfelt(self, feltnavn):
        if (felt:= self.finnfelt(feltnavn)):
            self.areal -= felt.maxareal
            self.felt.remove(felt)
            print(f'Fjernet {feltnavn}!')
    
    @tryexcept
    def leggtildyr(self, feltnavn, dyr):
        if dyr not in Dyr.dyreattributer:
            print(f'Dyret finnes ikke. Tilgjengelige dyr er: {[i for i in Dyr.dyreattributer]}')
            return
        if (x:= self.sjekkfelt(feltnavn, 'Dyrefelt')):
            print(x.adddyr(dyr))

    @tryexcept
    def leggtilavling(self, feltnavn, avling):
        if avling not in Avlinger.avlingattributer:
            print(f'Avlingen finnes ikke. Tilgjengelige avlinger er: {[i for i in Avlinger.avlingattributer]}')
            return
        if (x:= self.sjekkfelt(feltnavn, 'Avlingsfelt')):
            x.addplante(avling)

    @tryexcept
    def høst(self, feltnavn, plante='alle'):
        if (x:= self.sjekkfelt(feltnavn, 'Avlingsfelt')):
            x.høst(plante)

    @tryexcept
    def fjernalle(self, feltnavn, dea):
        if (x:= self.sjekkfelt(feltnavn, 'Dyrefelt', False)):
            x.slaktalle(dea)
        elif (x:= self.sjekkfelt(feltnavn, 'Avlingsfelt')):
            x.fjernalle(dea)

                    
##########          Felt          ##########
            
class Felt:
    def __init__(self, areal, navn):
        self.navn = navn
        self.maxareal = areal
        self.tilstand = []
        self.produsert = {}
        self.arealbrukt = 0
        
    def status(self):
        print(f'\n{self.navn}:')
        print(f'arealet brukt er: {self.arealbrukt}/{self.maxareal}')
        for i in self.innhold:
            print(f'{i} : {len(self.innhold[i])}')
        print('Produsert:')
        print('---------------------------')
        if not self.produsert:
            print('Ingenting er produsert ennå')
        for i in self.produsert:
            print(f'{i}: {self.produsert[i]}kg')
        print('---------------------------')
    def oppdater(self):
        for i in self.innhold:
            for y in self.innhold[i]:
                o = y.oppdater()
                if o:
                    if o[0] == 'føder':
                        for j in o[1]:
                            self.adddyr(j)
                    if o[0] == 'slaktes':
                        self.slaktdyr(o[1])
        
class Avlingsfelt(Felt):
    def __init__(self, areal, navn):
        super().__init__(areal, navn)
        self.innhold = {
            'hvete': [],
            'mais' : [],
            'ris' : [],
            'soya' : [],
            }
        
    def addplante(self, plante):
        if self.arealbrukt + Avlinger.avlingattributer[plante]['plass'] < self.maxareal:
            a = Avlinger(plante)
            self.innhold[plante].append(a)
            self.arealbrukt += a.plass
            print(f'{self.navn}: +1 {plante}')
        else:
            print('ikke nok plass')
            
    def sjekkklar(self, plante='alle'):
        klar = []
        for i in self.innhold:
            if plante == 'alle':
                for y in self.innhold[i]:
                    if y.status == 'klar for høsting':
                        klar.append(y)
            if i == plante:
                for y in self.innhold[i]:
                    if y.status == 'klar for høsting':
                        klar.append(y)
        return klar
    
    def status(self):
        super().status()
        [print(f'{y.plante[0]} {y.plante[1]} er {y.status}!') for i in self.innhold for y in self.innhold[i]]

                    
    def høst(self, plante):
        k = self.sjekkklar(plante)
        if k:
            for i in k:
                if i.plante[0] in self.produsert:
                    self.produsert[i.plante[0]] += i.høst()
                else:
                    self.produsert[i.plante[0]] = i.høst()
        else:
            print('kan ikke høstes')

    def fjern(self, avlingobjekt): #bare brukt til vær funksjon...
        self.innhold[avlingobjekt.plante[0]].remove(avlingobjekt)
        self.arealbrukt-= avlingobjekt.plass
        
    def fjernalle(self, avling):
        for i in self.innhold[avling]:
            self.arealbrukt -= i.plass
        self.innhold[avling] = []
        print(f'Fjernet alt {avling}!')
        
class Dyrefelt(Felt):
    def __init__(self, areal, navn):
        super().__init__(areal, navn)
        self.innhold = {
            'ku': [],
            'sau': [],
            'gris' : [],
            'høne' : [],
            }
        
    def adddyr(self, dyr):
        if self.arealbrukt + Dyr.dyreattributer[dyr]['plass'] < self.maxareal:
            d = Dyr(dyr)
            self.innhold[dyr].append(d)
            self.arealbrukt += d.plass
            return f'{self.navn}: +1 {dyr}'
            
    def slaktdyr(self, dyr):
        self.arealbrukt -= dyr.plass
        if dyr.dyr[0] in self.produsert:
            self.produsert[dyr.dyr[0]]['kjøtt'] += Dyr.dyreattributer[dyr.dyr[0]]['kjøtt']
        else:
            self.produsert[dyr.dyr[0]] = {'kjøtt': Dyr.dyreattributer[dyr.dyr[0]]['kjøtt']}
        self.innhold[dyr.dyr[0]].remove(dyr)
        
    def slaktalle(self, dyr):
        for i in self.innhold[dyr]:
            self.slaktdyr(i)
        print('Slaktet alle!')
        
##########          planter og dyr          ###########
        
class Avlinger:
    avlingid = 0
    statuser = ['plantet', 'under vekst', 'klar for høsting']
    avlingattributer = {
        'hvete': {'voksetid': 120, 'høsting': 0.6, 'plass': 2}, #dager, pr m^2, m^2
        'mais' : {'voksetid': 150, 'høsting': 1.2,'plass': 5},
        'ris' : {'voksetid': 60, 'høsting': 0.5,'plass': 2},
        'soya' : {'voksetid': 180, 'høsting': 0.3,'plass': 3},
        }
    def __init__(self, plante):
        Avlinger.avlingid += 1
        self.plante = (plante, Avlinger.avlingid)
        self.høstet = 0
        self.status = Avlinger.statuser[0]
        self.plass = Avlinger.avlingattributer[plante]['plass']
        self.alder = 0

    def info(self):
        #info om høstet osv.
        pass
    
    def oppdater(self):
        self.alder += 1 #dager
        if self.alder > 5:
            self.status = Avlinger.statuser[0]
        if self.alder >= Avlinger.avlingattributer[self.plante[0]]['voksetid']:
            self.status = Avlinger.statuser[2]
        else:
            self.status = Avlinger.statuser[1]
            
    def høst(self):
        self.status = Avlinger.statuser[0]
        self.alder = 0
        høstet = round(Avlinger.avlingattributer[self.plante[0]]['høsting']*Avlinger.avlingattributer[self.plante[0]]['plass'])
        self.høstet += høstet
        print(f'høstet {høstet}kg {self.plante[0]}!')
        return høstet
        
class Dyr:
    dyreattributer = {
            'ku': {'føder': '2år', 'slaktes' : '5år', 'plass': 2, 'kjøtt': 300},
            'høne': {'føder' : '126dager', 'slaktes' : '2år', 'plass': 0.5, 'kjøtt': 2.5},
            'gris' : {'føder' : '115dager', 'slaktes' : '0.5år', 'plass': 1, 'kjøtt': 115},
            'sau' : {'føder' : '150dager', 'slaktes' : '3år', 'plass': 1, 'kjøtt': 40}
            }
    dyreid = 0
    
    def __init__(self, dyr):
        Dyr.dyreid += 1
        self.dyr = (dyr, Dyr.dyreid)
        self.antallfødt = 0
        self.prosess = [Dyr.dyreattributer[dyr]['føder'], Dyr.dyreattributer[dyr]['slaktes']]
        self.status = ''
        self.alder = 0
        self.plass = Dyr.dyreattributer[dyr]['plass']
        
    def fød(self):
        return [self.dyr[0] for i in range(random.randint(1, 2))]
            

    def info(self):
        #info om dyrfødt osv.
        pass

    def vis(self, status, *barn):
        if visdyr == 'alle' or self.dyr[0] == visdyr:
            if status == 'føder':
                print(f'{self.dyr[0]} {self.dyr[1]} føder {len(barn[0])} barn!')
            if status == 'slaktes':
                print(f'{self.dyr[0]} {self.dyr[1]} slaktes')
        
    def oppdater(self):
        self.alder += 1 #dager
        for index, i in enumerate(self.prosess):
            p = False
            if 'dager' in i:
                if int(i.split('dager')[0]) == self.alder:
                    p = True
                        
            if 'år' in i:
                if round(åtd(float(i.split('år')[0]))) == self.alder:
                    p = True
                    
            if p == True:
                if index == 0:
                    self.status = 'føder'
                    barn = self.fød()
                    self.vis(self.status, barn)
                    return ['føder', barn]
                elif index == 1:
                    self.status = 'slaktes'
                    self.vis('slaktes')
                    return ['slaktes', self]
                    
##########          Testing          ##########

print('=====================================')
print('Du må bruke metodene til gården for å gjøre ting:\noversikt(felt)\nvis(dyr)\nleggtilfelt(feltobjekt)/fjernfelt(feltnavn)\nleggtildyr(feltnavn, dyr)/leggtilavling(feltnavn, avling)\nhøst(avlingsfelt, avling)\nfjernalle(feltnavn, dyr/avling)')
print('=====================================')
           
##loadgård() #kommenter ut denne, eller det under

gård1 = Gård('gård1')
gård1.leggtilfelt(Dyrefelt(25, 'dyrefelt1'))
gård1.leggtilfelt(Avlingsfelt(25, 'avlingsfelt1'))
##gård1.leggtilfelt(Avlingsfelt(25, 'avlingsfelt2'))
gård1.leggtildyr('dyrefelt1', 'ku')
gård1.leggtildyr('dyrefelt1', 'gris')
gård1.leggtildyr('dyrefelt1', 'sau')
gård1.leggtildyr('dyrefelt1', 'høne')
gård1.leggtilavling('avlingsfelt1', 'hvete')
gård1.leggtilavling('avlingsfelt1', 'mais')
gård1.leggtilavling('avlingsfelt1', 'ris')
gård1.leggtilavling('avlingsfelt1', 'soya')
##gård2 = Gård('gård2')
#kan legge til flere gårder

###### legg til ######

#info om hvor mye plass hver avling/dyr bruker
#sjanse for at dyr blir syke?
#dyr kan produsere melk, egg, osv.?
#info om hvor mange dyr som er blitt født på et felt

