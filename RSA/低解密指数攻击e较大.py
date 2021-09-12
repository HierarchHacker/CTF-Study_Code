import  RSAwienerHacker
n=
e=
d =  RSAwienerHacker.hack_RSA(e,n)
if d:
    print(d)
import hashlib
flag = "flag{" + hashlib.md5(hex(d)).hexdigest() + "}"
print flag
