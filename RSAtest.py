from RSAinternship import *

# Generate public key, private key, and n(product of two prime numbers)
pbk, pvk, n = key_gen(5)

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


h1 = Mult(pbk, n, m1, m2)
print('Homomorphism: ' + str(h1))
