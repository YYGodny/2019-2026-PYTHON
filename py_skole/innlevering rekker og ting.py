def pharmanydica(t): #t = tabletterprdag
    k = (10*t)/(1-0.6)#summeformel, a1 = 10, kvotient = 0.6
    dager = 0 #antall dager
    if k > 100: #det som skal bli skrevet hvis det er over 100mg virkestoff
        nd = 0 #nåverende dose
        while True: #en loop som går til nåverende dose er over 100 mg
            nd = nd*0.6+10*t #an = an*0.6+10t
            if nd > 100: #når nåverende dose er over 100mg må loopen stoppe
                break
            dager += 1 #plusser på antall dager til nåverende dose er over 100mg
        return f'{t} tabletter er forsvarlig i {dager} dager' #returner antall dager
    return f'total mengde virkestoff er {k}mg'#returnerer bare total virkestoff, siden k ikke er over 100
while True: #evig loop
    i = int(input('skriv inn antall tabletter pr dag: ')) #input for antall tabletter pr dag
    print(pharmanydica(i)) # skriver ut output




