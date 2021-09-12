import gmpy2
from gmpy2 import invert, iroot
import gmpy2 as gp
from libnum import xgcd, invmod

n=[,,,,,,,,,,,,,,,,,,,]
for i in n:
    for j in n:
        if (i<>j):
            pub_p=gmpy2.gcdext(i,j)
            if (pub_p[0]<>1)&(i>j):
                print i
                print j
                print pub_p[0]
                a=i,p=pub_p[0]
q=a/p
p =  gp.mpz()
q =  gp.mpz()
e =  gp.mpz()
c =  gp.mpz()
n = p*q
phi = (p-1) * (q-1)
d = gp.invert(e, phi)
m = pow(c, d, n)
print hex(m)
