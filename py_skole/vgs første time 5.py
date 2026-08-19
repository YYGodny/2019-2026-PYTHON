ukene = [42, 37.5, 39]
s = 0

for index, i in enumerate(ukene):
    print(f'uke {index} {(37.5 * 210) + (i-37.5)*315}, du jobbet {i-37.5} timer overtid')
    s += (37.5 * 210) + (i-37.5)*315
print(f'du fikk {s} tilsammen')
