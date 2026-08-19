import os
import glob

#cum = os.popen('dir downloads').readlines()[3][23::1].split('\Desktop\python')[:-1][0] funker ikke

cum = os.popen('dir downloads').readlines()

for line in cum:
    if 'Directory' in line:
        cum = line
        cum = cum.replace(' ', '')
        cum = cum.replace('\\', '')
        cum = cum.split('DirectoryofC:Users')
        #cum.pop(0)
             
cum2 = []
for i in cum[1]:
    if i == 'O':
        break
    cum2.append(i)
cum2 = ''.join(cum2)    

gum = glob.glob(f'C:/Users/{cum2}/downloads/*')

for lines in gum:
    print(lines)







