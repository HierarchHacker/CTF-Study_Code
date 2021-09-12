#coding=utf-8
import math
import sys
from Crypto.PublicKey import RSA
arsa=RSA.generate(1024)
arsa.p=
arsa.q=
arsa.e=
arsa.n=arsa.p*arsa.q
Fn=long((arsa.p-1)*(arsa.q-1))
i=1
while(True):
    x=(Fn*i)+1
    if(x%arsa.e==0):
           arsa.d=x/arsa.e
           break
    i=i+1
private=open('private.pem','w')
private.write(arsa.exportKey())
private.close()
 