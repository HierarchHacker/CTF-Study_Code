import gmpy2
p = gmpy2.mpz(473398607161)#初始化大整数
q = gmpy2.mpz(4511491)
e = gmpy2.mpz(17)
phi_n = (p-1)*(q-1)
d = gmpy2.invert(e,phi_n)#invert（x，m）返回y使得x * y == 1 modulo m，如果不存在y，则返回0
print("p=%s,q=%s,e=%s"%(p,q,e))
print("d is:\n%s"%d)

