brett = [[1,2,3],[4,5,6],[7,8,9]]
game = True
def place(x, y, s):
    if s not in 'xo': raise ValueError
    if str(brett[x][y]) in '123456789': brett[x][y] = s
    else: print('allerede i bruk')       
def check():
    global game
    vinner = False
    for index, item in enumerate(brett):
        if len(set(item)) == 1: vinner = item[0]
        elif len(set([i[index] for i in brett])) == 1: vinner = item[index]
        elif len(set([item[index] for index, item in enumerate(brett)])) == 1: vinner = item[-1]
        elif len(set([item[-(index+1)] for index, item in enumerate(brett)])) == 1: vinner = item[0]
    draw = [y for i in brett for y in i if str(y) in '123456789']
    if not draw: print('draw!!!!')
    if vinner != False: print(f'{vinner} vant!!!!')
    if not draw or vinner != False: game = False
while game:
    [print(i) for i in brett]
    inp = input('rad, kolonne, x/y: ').split(',')
    inp = [i.split(' ') for i in inp]
    inp = [y for i in inp for y in i if y != '']
    try: place(int(inp[0])-1, int(inp[1])-1, inp[2])
    except: print('du skrev noe feil')
    check()
    
        
    
