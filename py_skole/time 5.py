gjennomsnitt = 0
fag2 = ['norsk', 'matte', 'udv', 'naturfag', 'samfunnsfag', 'kroppsøving', 'språk', 'engelsk', 'krle', 'valgfag', 'musikk']
for i in fag2:
    i = int(input(f'skriv karakter i {i}: '))
    if i < 0 or i > 6:
        continue
    gjennomsnitt += i
print('gjennomsnittet er: ', gjennomsnitt/len(fag2))
