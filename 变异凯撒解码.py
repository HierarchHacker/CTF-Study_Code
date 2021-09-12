ciphertext = input('Please input:')
j = 7
for i in ciphertext:
    print(chr(ord(i) + j), end='')
    j += 1
