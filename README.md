# RSA
### Key Generation:
- Choose two prime numbers $p$ and $q$
- $n = p \times q $
- $\Phi N = (p-1)(q-1)$
- Find integer $e$ such that: $gcd(e, \Phi N) = 1$ 
- Public key &rarr; $(e, \Phi N)$
- Find integer $d$ such that:  $ed$ $mod$ $\Phi N = 1$
- Private key &rarr; $d$
### Encryption:
- Choose integer $m$ such that: $0 \leq m \leq n$
- $Enc(m) = m^e$ $mod$ $n = c$
### Decryption:
- $Dec(c) = c^d$ $mod$ $n = m$
### Homomorphism:
- $Enc(m_1m_2) = Enc(m_1)Enc(m_2)$ $mod$ $n$
### Miller Rabin Test:
 - Tests if number is likely to be prime
 - 

