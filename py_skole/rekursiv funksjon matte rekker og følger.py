def s(x, forrige=0):
    if x == 0:
        print(round(forrige))
    if forrige==0:
        s(x-1, 1)
    elif x > 0 and forrige != 0:
        s(x-1, ((forrige)**(1/3)+1)**3)

s(50)
