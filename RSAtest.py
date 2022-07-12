from RSAinternship import *

# Generate public key, private key, and n(product of two prime numbers)
k = 5
pbk, pvk, n = key_gen(k)

# Print public key
print('Public key: ' + str(pbk) + ', ' + str(n))

# Print private key
print('Private key: ' + str(pvk))

print('')

# Assign number to encrypt
m = 255
print('Plain text: ' + str(m))

# Encrypt number
e = Enc(pbk, n, m)
print('Encrypted text: ' + str(e))

# Decrypt number
d = Dec(pvk, n, e)
print('Decrypted text: ' + str(d))
print('')

# Homomorphism 
m1 = 10
m2 = 30

p1, p2 = Mult(pbk, n, m1, m2)
print('Homomorphism: ' + str(p1) + ", " + str(p2))
