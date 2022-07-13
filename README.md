# RSA
### Key Generation:
- Choose two prime numbers $p$ and $q$
- $n = p \times q $
- $\Phi N = (p-1)(q-1)$
- Find integer $e$ such that: gcd($e, \Phi N$) $= 1$ 
- Public key &rarr; $(e, \Phi N)$
- Find integer $d$ such that:  $ed$ mod $\Phi N = 1$
- Private key &rarr; $d$
### Encryption:
- Choose integer $m$ such that: $0 \leq m \leq n$
- Enc($m$)$ = m^e$ mod $n = c$
### Decryption:
- Dec($c$) $= c^d$ mod $n = m$
### Homomorphism:
- Enc($m_1m_2$) = Enc($m_1$)Enc($m_2$) mod $n$
### Miller Rabin Test:
 - Tests if number is likely to be prime
 - Choose a positive integer $n$
 - Calculate $k$ and $m$ such that: $n - 1 = 2^k m$
 - Randomly choose a number $a$ such that: $2 \leq a \leq n-1$
 - Calculate $b$ such that: $b = a^m$ mod $n$
 - If $b$ mod $n = 1$: $n$ is likely to be prime
 - If not, calculate the next step $k$ times
   - If $b$ mod $n = -1$: $n$ is likely to be prime
   - $b = b^2$ mod $n$
- If not, $n$ is not prime
### mpow:
- Drastically reduces the number of operations to performs modular exponentiation
- $b^e$ can be written as: 
  - $b^{(\Sigma ^{n-1}_{i = 0}a_i2^i)}  = \Pi _{i = 0}^{n-1}b^{a_i2^i}$
- Therefore solution  $c$  will be:  
   - $c$ mod $m = \Pi _{i = 0}^{n-1}b^{a_i2^i}$
 
# RSA test
### Precondition:
 - $k = 5$ (Key made with two prime numbers that is k bit long)
 - $m = 255$ (Number to encrypt)
 - $m_1 = 10$ (First number for homomorphism)
 - $m_2 = 30$ (Second number for homomorphism)
 ### Result:
  <img src="https://user-images.githubusercontent.com/108774371/178429875-74acb5a0-b5a4-43b0-b4c4-01d29d659d00.png"  width="33%" height="33%">

# 2D Homomorphism
 ### Precondition:
  - Matrix and Vector are multipliable
  - key_gen(6)
  - arr = [[1, 2], [3, 4]]
  - x = [[1], [2]]<br>
  <img src="https://user-images.githubusercontent.com/108774371/178662423-f57ec143-f7d0-4cd7-8e78-619095b5dcfc.png"  width="33%" height="33%">



 # Image with filter 1
 ### Step 1:
  - Encrypt image
  <img src="https://user-images.githubusercontent.com/108774371/178175104-514b0736-53dc-4fc3-acb3-6190b5a2e0f7.png"  width="25%" height="25%">
  &darr; 
  <img src="https://user-images.githubusercontent.com/108774371/178427009-137b6873-fa7e-4c6f-bcd7-b1b4ebda0b61.png"  width="25%" height="25%">

   - Encrypted image will not always look the same because key is generated randomly.
   - Encrypted image might look the same as the original image after encryption because 0(black) will not change and if 255(white) exceeds 255, it will stay white.

 ### Step 2:
  - Apply encrypted filter to encrypted image
  - Filter type: Moving average filter
  - Effect of filter: Makes the image blur
 ### Step 3:
  - Decrypt image
  
  <img src="https://user-images.githubusercontent.com/108774371/178176715-2287fb53-c972-4c3a-99f2-11e2547428da.png"  width="25%" height="25%">
 
 - Image without encryption
  <img src="https://user-images.githubusercontent.com/108774371/178422773-cc27e953-b43a-471b-8bd0-4a31a85dfcf5.png"  width="25%" height="25%">

  # Image with filter 2
 ### Step 1:
  - Encrypt color image
   <img src="https://user-images.githubusercontent.com/108774371/178176807-5ff6288a-ca9c-427a-8195-500b7abb2ff9.png"  width="33%" height="33%">
  &darr;
   <img src="https://user-images.githubusercontent.com/108774371/178176892-96758bcb-26a2-4c8d-9966-54e7427e0225.png"  width="33%" height="33%">

   - Image is mostly white because most RBG values exceed 255. 

 ### Step 2:
  - Apply encrypted filter to encrypted image
  - Filter type: Moving average filter
  - Effect of filter: Makes the image blur
 ### Step 3:
  - Decrypt image
  <img src="https://user-images.githubusercontent.com/108774371/178176965-7803db76-d291-4dc3-ba14-8cf1cad9bc80.png"  width="33%" height="33%">

  - Image without encryption

   <img src="https://user-images.githubusercontent.com/108774371/178423137-1b513749-a273-45fe-8ad4-7ce64426364f.png"  width="33%" height="33%">

 # Image with filter 3
 ### Step 1:
  - Encrypt image
   <img src="https://user-images.githubusercontent.com/108774371/178177141-58d2ed56-e44a-450c-aa8a-70b387b8d535.png"  width="25%" height="25%">
  &darr;
   <img src="https://user-images.githubusercontent.com/108774371/178177194-3e4a8303-8ebe-4cb3-9987-03bae90c4386.png"  width="25%" height="25%">
   - Encrypted image looks the same as the original image because 0(black) does not change after encryption and 255(white) is exceeding 255 which keeps it white.
  
 ### Step 2:
  - Apply encrypted filter to encrypted image
  - Filter type: Laplacian filter
  - Effect of filter: Makes edge standout and others black
 ### Step 3:
  - Decrypt image
   <img src="https://user-images.githubusercontent.com/108774371/178177254-8cf9d108-aada-426a-bd7b-d3a4ac14f8e8.png"  width="25%" height="25%">
  
 - Image without encryption
 <img src="https://user-images.githubusercontent.com/108774371/178423326-f5a003da-c648-419a-b9d8-7ae7ef30f992.png"  width="25%" height="25%">

 # Simulation environment
### Software
- macOS Big Sur Version 11.6.7
 - Python 3.10.5
 - Visual Studio Code Version 1.68.1
 ### Hardware
  - Macbook Air (Retina, 2020)
  - Processor 1.1 Ghz Quad-Core Intel Core i5
  - Memory 8 GB 3733 MHz 


