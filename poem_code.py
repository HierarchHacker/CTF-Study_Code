# coding=utf-8
# python2版本
""" 
最后一行有密文路径，使用前请修改相关内容，
poem.txt里只存放poem，cipher.txt里存放密文，两文件里不存放其他无关字符
"""
import itertools

def load_file(filename):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    words = []
    for line in lines:
        for word in line.split():
        # 过滤特殊字符 .
            words.append(word.split('.')[0].lower()) 
    return words

abc = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(poem, cipher):
    # 诗
    twords = load_file(poem)
    # 密文
    cwords = load_file(cipher)

    # code 存下来了我依此取了哪些位置的单词作为秘钥
    code = []
    for i in cwords.pop(0):
        code.append(abc.index(i))
    
    # xwords[i] 表示第i个单词有哪些可能
    xwords = [[] for x in range(len(code))]
    for xcount, c in enumerate(code):
        # 因为加密时位置对26取模了，所以这里要列举出所有的可能情况
        while c < len(twords):
            xwords[xcount].append(twords[c].lower())
            c += 26

    # 直接枚举每一种秘钥
    for elem in itertools.product(*xwords):
        # pword 就是秘钥
        pword = ''
        for word in elem:
            pword += word
        plen = len(pword)

        countx = 0
        pcode = [None] * plen   # pcode按顺序存储着每一列字符串(此时已经还原了顺序)
        # 将打乱的列顺序还原
        for c in abc:
            for pc, pl in enumerate(pword):
                if not c == pl:
                    continue
                pcode[countx] = cwords[pc]
                countx += 1

    
        mlen = len(pcode[0])
        password = ''
        # 按行，先取第一行，再取第二行....
        for row in range(mlen):
            for col in pcode:
                password += col[row]

        print(password)
    
if __name__ == "__main__":
    decrypt('C:\Users\Hierarch\Desktop\poem.txt', 'C:\Users\Hierarch\Desktop\cipher.txt')
