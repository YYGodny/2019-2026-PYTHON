"""
Du skal nå lage en adjektivhistorie

Her er historien du skal lage adjektiver til

Det var en #adj1# januardag at elevene på den #adj2# skolen skulle lære seg å bruke python.
#navn# var den første til å #verb1# etter å ha forsøkt seg på den #adj3# koden som den #adj# læreren
hadde gitt alle de #adj4# elevene. Læreren #verb# og #verb2# over at elevene ikke klarte å være stille.

Oppgave 1)
Lag variabler som deretter skal fylles inn i teksten når den printes ut.

Oppgave 2)
Lag programmet slik at brukeren av programmet skriver selv inn adjektiver / navn / verb,
som deretter blir skrevet ut i den flotte adjektivhistorien.

Oppgave 3)
Utvid historien slik at den blir litt lengre og ha med noen flere adjektiver/navn/verb.

"""



ordene, rekkefølge = [], ['adj', 'adj', 'adj', 'adj', 'adj', 'verb', 'verb', 'verb', 'navn'] #variabler
h = [ordene.append(input(f'skriv {rekkefølge[i]}: ')) for i in range(9)] #får input
print(f'Det var en {ordene[0]} januardag at elevene på den {ordene[1]} skolen skulle lære seg å bruke python.\n{ordene[8]} var den første til å {ordene[5]} etter å ha forsøkt seg på den {ordene[2]} koden som den {ordene[3]} læreren hadde gitt alle de {ordene[4]} elevene.\nLæreren {ordene[6]} og {ordene[7]} over at elevene ikke klarte å være stille.')
#printer ut historie




