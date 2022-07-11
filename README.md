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
 ### Step 1:
  - Encrypt image
  <img src="https://user-images.githubusercontent.com/108774371/178175104-514b0736-53dc-4fc3-acb3-6190b5a2e0f7.png"  width="25%" height="25%">
  &darr; 
  <img src="https://user-images.githubusercontent.com/108774371/178176522-e1bce687-ac6b-4cb2-83f0-72dd35077061.png"  width="25%" height="25%">
  
 ### Step 2:
  - Apply encrypted filter to encrypted image
  - Filter type: Moving average filter
  - Effect of filter: Makes the image blur
 ### Step 3:
  - Decrypt image
  
  <img src="https://user-images.githubusercontent.com/108774371/178176715-2287fb53-c972-4c3a-99f2-11e2547428da.png"  width="25%" height="25%">
 
  # Image with filter 2
 ### Step 1:
  - Encrypt color image
   <img src="https://user-images.githubusercontent.com/108774371/178176807-5ff6288a-ca9c-427a-8195-500b7abb2ff9.png"  width="33%" height="33%">
  &darr;
   <img src="https://user-images.githubusercontent.com/108774371/178176892-96758bcb-26a2-4c8d-9966-54e7427e0225.png"  width="33%" height="33%">
  
 ### Step 2:
  - Apply encrypted filter to encrypted image
  - Filter type: Moving average filter
  - Effect of filter: Makes the image blur
 ### Step 3:
  - Decrypt image
  <img src="https://user-images.githubusercontent.com/108774371/178176965-7803db76-d291-4dc3-ba14-8cf1cad9bc80.png"  width="33%" height="33%">
 
 # Image with filter 3
 ### Step 1:
  - Encrypt image
   <img src="https://user-images.githubusercontent.com/108774371/178177141-58d2ed56-e44a-450c-aa8a-70b387b8d535.png"  width="25%" height="25%">
  &darr;
   <img src="https://user-images.githubusercontent.com/108774371/178177194-3e4a8303-8ebe-4cb3-9987-03bae90c4386.png"  width="25%" height="25%">
  
 ### Step 2:
  - Apply encrypted filter to encrypted image
  - Filter type: Laplacian filter
  - Effect of filter: Makes edge standout and others black
 ### Step 3:
  - Decrypt image
   <img src="https://user-images.githubusercontent.com/108774371/178177254-8cf9d108-aada-426a-bd7b-d3a4ac14f8e8.png"  width="25%" height="25%">
  
