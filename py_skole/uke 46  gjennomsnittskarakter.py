# Write your code here :-)
fag = int(input('Hvor mange fag har du? '))
s = 0
for i in range(fag):
    karakter = int(input(f'Oppgi karakteren for fag {i+1}: '))
    s += karakter


print(f'Gjennomsnittskarakteren er: {s/fag}')
print(f'meget godt')
