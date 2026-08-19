alfabet = 'abcdefghijfklmnopqrstuvwxyz '
text = 'hvordan klarte du det'
code = ''

for i in text:
    code += chr(ord(i)*2)

print(code)
