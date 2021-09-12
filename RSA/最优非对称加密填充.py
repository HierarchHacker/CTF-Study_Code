#!/usr/bin/python
# coding=utf-8

#最优非对称加密填充
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open('./tmp/pubkey.pem', 'r') as f:
    key = RSA.importKey(f)
    N = key.n
    e = key.e
print N
print e

with open('./tmp/private.pem', 'r') as f:
    private = RSA.importKey(f)
    oaep = PKCS1_OAEP.new(private)

with open('./tmp/flag.enc', 'r') as f:
    print oaep.decrypt(f.read())
