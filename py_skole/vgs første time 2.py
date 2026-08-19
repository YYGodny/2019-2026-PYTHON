print('de første 20 første oddetallene:')
x = 1
for i in range(20):
    print(x)
    x += 2

print('de 20 første tallene i følgen 1, 5, 9, 13...')
x = 1
[print(x+i*4) for i in range(20)]

print('de 20 første tallene i følgen 8, 5, 2...')
x = 8
[print(x+i*-3) for i in range(20)]
    
print('de 20 første tallene i følgen 3, 6, 12, 24...')
x = 3
for i in range(20):
    print(x)
    x *= 2
    
    
