from turtle import *
#maks høyde er ca.320
#maks lengde er ca.630

def firkant(x, y, size, fc, stripe = False, rims=4):
    penup()
    goto(x, y)
    pendown()
    fillcolor(fc)
    begin_fill()
    goto(x+size, y)
    goto(x-size, y)
    goto(x-size, y+size*2)
    goto(x+size, y+size*2)
    goto(x+size, y)
    end_fill()
    if stripe == True:
        sl = size/rims
        fillcolor('white')
        begin_fill()
        goto(x+sl, y)
        goto(x-sl, y)
        goto(x-sl, y+size*2)
        goto(x+sl, y+size*2)
        goto(x+sl, y)
        end_fill()
        penup()
        goto(x, y+size-sl)
        pendown()
        begin_fill()
        goto(x+size, y+size-sl)
        goto(x-size, y+size-sl)
        goto(x-size, y+size+sl)
        goto(x+size, y+size+sl)
        goto(x+size, y+size-sl)
        end_fill()
        
#pen
speed(100)

#bakgrunn
Screen().colormode(255)
Screen().bgcolor(123, 63, 0)

#vindu
firkant(-300, 50, 100, 'skyblue', stripe=True, rims=10)

#bakke
penup()
goto(0, -220)
pendown()
fillcolor(110, 38, 14)
begin_fill()
goto(1000, -220)
goto(-1000, -220)
goto(-1000, -330)
goto(1000, -330)
goto(1000, -220)
end_fill()


#juletre
firkant(400, -220, 30, 'brown')
fillcolor('green')
begin_fill()
penup()
goto(400, -160)
pendown()
#høyre
goto(500, -160)
goto(450, -110)
goto(475, -110)
goto(425, -60)
goto(450, -60)
goto(400, 0)
#venstre
goto(400, 0)
goto(350, -60)
goto(375, -60)
goto(325, -110)
goto(350, -110)
goto(300, -160)
goto(400, -160)
end_fill()

#julegave
firkant(350, -220, 24, 'red', stripe = True)


