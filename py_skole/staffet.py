def behandletekst(tekst, n):
    nyTekst = ''
    for bokstav in tekst:
        if bokstav in 'abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ':
            nyBokstav = manipulereBokstav(bokstav, n)
            nyTekst = nyTekst + nyBokstav
        else:
            nyTekst = nyTekst + bokstav
    return nyTekst

def manipulereBokstav(bokstav, n):
    alfabet = 'abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'
    for index, i in enumerate(alfabet):
        if i == bokstav:
            posisjon = index
    nyPosisjon = (posisjon + n) % 29
    return alfabet[nyPosisjon]

print(behandletekst('Hei på deg', 3))
            
