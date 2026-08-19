import os
import glob

cum = os.popen('dir downloads').readlines()

for line in cum:
    if 'Directory' in line:
        cum = line
        
cum2 = ''
count = 0

for i in cum:
    if i == '\\':
        count += 1
    if i == '\\':
        continue
    if count == 2:
        cum2 += i

gum = glob.glob(f'C:/Users/{cum2}/downloads/*')

for lines in gum:
    print(lines)







