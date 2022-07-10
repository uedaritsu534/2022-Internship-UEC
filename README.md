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
 - Choose a positive integer $n$
 - Calculate $k$ and $m$ such that: $n - 1 = 2^k m$
 - Randomly choose a number $a$ such that: $2 \leq a \leq n-1$
 - Calculate $b$ such that: $b = a^m$ $mod$ $n$
 - If $b$ $mod$ $n = 1$: $n$ is likely to be prime
 - If not, calculate the next step $k$ times
   - If $b$ $mod$ $n = -1$: $n$ is likely to be prime
   - $b = b^2$ $mod$ $n$
- If not, $n$ is not prime
### mpow:
- Drastically reduces the number of operations to performs modular exponentiation
- $b^e$ can be written as: 
  - $b^{(\Sigma ^{n-1}_{i = 0}a_i2^i)}  = \Pi _{i = 0}^{n-1}b^{a_i2^i}$
- Therefore solution  $c$  will be:  
   - $c$ $mod$ $m = \Pi _{i = 0}^{n-1}b^{a_i2^i}$
 
 # Image with filter 1
 
