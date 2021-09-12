#!/usr/bin/env python
#coding:utf-8

import gmpy2
from Crypto.PublicKey import RSA

public_key = "./tmp/pubkey.pem"
cipher_file = "./tmp/flag.enc"

#读入公钥
with open(public_key, "r") as f:
    key = RSA.importKey(f)
    n = key.n
    e = key.e

#读入密文
with open(cipher_file, "r") as f:
    cipher = f.read().encode("hex")
    cipher = int(cipher, 16)
    #print(cipher)

#破解密文
def get_flag():
    i = 0
    while True:
        if(gmpy2.iroot(cipher+i*n, 3)[1] == True):
            flag_bin = int(gmpy2.iroot(cipher+x*n, 3)[0])
            flag = hex(flag_bin)[2:-1].decode("hex")
            print(flag) 
            break
        i += 1

def get_flag_for():
    for x in xrange(118600000, 118720000):
        if(gmpy2.iroot(cipher+x*n, 3)[1] == 1):
            flag_bin = int(gmpy2.iroot(cipher+x*n, 3)[0])
            flag = hex(flag_bin)[2:-1].decode("hex")
            print(flag)
            break 

if __name__ == "__main__":
    get_flag_for()
    #get_flag()
