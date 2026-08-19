def count_animals(x):
    animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]
    for i in animals:
            if i in x:
                animals.remove(i)
    res = []
    t = False
    for i in animals:
        f = []
        for index, item in enumerate(i):
            if item in x:
                f.append(True)
            else:
                f.append(False)
		
        if False in f:
            continue
		
        elif False not in f:
            res.append(i)
	    
        t = False
    if res == []:
        return 'ingen dyr'  
    return f'det er {len(res)} dyr: {res}'

while True:
    x = input('skriv noe')
    print(count_animals(x))
    
