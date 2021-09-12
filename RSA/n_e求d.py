import gmpy2
from Crypto.Util import number
p = 473398607161
q = 4511491
e = 17
d = gmpy2.invert(e,(p-1)*(q-1))
print (d)
