import random

#Finds the greatest common denominator of x and y
def find_gcd(x, y):
    while True:
        if x%y == 0:
            break
        y1 = x%y
        x1 = y
        x = x1
        y = y1
    return y

#Use miller rabin test to find if n is prime or not
def miller_rabin_test(n):
    if n <= 2:
        return False
    k = 0
    m = n-1
    while(m%2 == 0):
        k += 1
        m = m/2
    count = 0
    for j in range(10):
        a = random.randint(2, n-1)
        b = pow(a, int(m), int(n))
        if b == 1:
            count += 1
            continue
        for i in range(0, k):
            if b == n-1:
                count += 1
                break
            b = pow(b,2,n)
    if count == 10:
        return True
    return False

#Generates 2 prime numbers that are k bit long and generate key from those numbers
def key_gen(k):
    while True:
        p = random.randint(2**(k-1), (2**k)-1)
        if miller_rabin_test(p):
            break
    while True:
        q = random.randint(2**(k-1), (2**k)-1)
        if miller_rabin_test(q) and q != p:
            break
    n = p*q
    phiN = (p-1)*(q-1)
    pbk = make_pbk(phiN)
    pvk = make_pvk(pbk, phiN)
    return pbk, pvk, n

#Creates the public key using phi(n)
def make_pbk(phiN):
    pbK = 2
    while True:
        if find_gcd(pbK, phiN) == 1:
            break
        pbK = pbK + 1
    return pbK

#Creates the private key using public key and phi(n)
def make_pvk(pbK, phiN):
    d = 1
    while True:
        if (pbK*d)%phiN == 1:
            break
        d = d + 1
    return d

#Calculates a^b mod m
def mpow(a, b, m):
    c = 1
    while b >= 1:
        if b % 2 == 1:
            c = (a * c) % m
        a = pow(a, 2) % m
        b = b // 2
    return c

#Encrypts m using public key and n
def Enc(pbK, n, m):
    c = (m**pbK)%n
    return c

#Decrypts c using private key and n
def Dec(pvK, n, c):
    m = mpow(c, pvK, n)
    return m

#Homomorphism
def Mult(pbK, n, m1, m2,):
    c1 = Enc(pbK, n, m1)
    c2 = Enc(pbK, n, m2)
    p1 = (c1*c2)%n
    p2 = Enc(pbK, n, m1*m2)
    return p1, p2

