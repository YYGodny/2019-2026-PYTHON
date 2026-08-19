file = open('test.txt', 'w')
file.write('du er gay')
file.close()

file = open('test.txt')
print(file.read())
file.close()
