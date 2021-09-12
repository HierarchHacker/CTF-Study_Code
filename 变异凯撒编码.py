answer = input('Please input:')
j = 7 # 首字符ASCII码的位移顺序
for i in answer:
    print(chr(ord(i) - j), end='')
    j += 1
