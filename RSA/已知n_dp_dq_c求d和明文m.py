import gmpy2 as gp

p = gp.mpz()
q = gp.mpz()
dp = gp.mpz()
dq = gp.mpz()
c = gp.mpz()

n = p*q
phin = (p-1)*(q-1)
dd = gp.gcd(p-1, q-1)
d=(dp-dq)//dd * gp.invert((q-1)//dd, (p-1)//dd) * (q-1) +dq
print(d)

m = gp.powmod(c, d, n)
print('-------------------')
print(m)
print(hex(m)[2:])
