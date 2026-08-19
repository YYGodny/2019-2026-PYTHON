import random

barn = random.randint(1, 30)
avforing = 0

for i in range(1460):#man kan endre på antall timer, så lenge man husker at det bare gjelder 4 timer hver dag
    avforing += sum([random.randint(1, 2) for i in range(60)])#måker
    plussminus = random.randint(1, 2)
    if plussminus == 2:#tilfeldig om barn kommer eller går
        barn -= random.randint(1, 30)
        if barn < 0:
            barn = 0
    else:
        barn += random.randint(1, 30)
    if barn > 30:#ender hvis det blir mer enn 30 barn
        avforing += sum([random.randint(1, 3) for i in range(60)])
    else:
        avforing += 60
    print(f'time {i+1}, det er {avforing} avføring på bakken')
 
print(f'gjennomsnittet hver dag er {avforing/365}')      
    
##
