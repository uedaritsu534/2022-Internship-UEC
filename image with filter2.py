from random import sample
import numpy as np
import matplotlib.pyplot as plt
from RSAinternship import *
import cv2

gazo = cv2.imread( "./images/2098_color.png", 3 )
gazo = cv2.cvtColor(gazo, cv2.COLOR_BGR2RGB)
sample_gazo = cv2.imread( "./images/2098_color.png", 3 )
sample_gazo = cv2.cvtColor(sample_gazo, cv2.COLOR_BGR2RGB)
pbk, pvk, n = key_gen(8)

# Resize image
gazo = cv2.resize(gazo, dsize = None, fx = 0.5, fy = 0.5)
sample_gazo = cv2.resize(sample_gazo, dsize = None, fx = 0.5, fy = 0.5)
height, width , c = gazo.shape

sample_filter_gazo = []
for i in range(height):
    sample_filter_gazo.append([])
    for j in range(width):
        sample_filter_gazo[i].append([])
        for k in range(c):
            sample_filter_gazo[i][j].append(0)

# Print original image
print( "Original image" )
print( gazo )
plt.figure()
plt.imshow(gazo)
gazo = gazo.tolist()

# Encrypt image 
for y in range(height):
  for x in range(width):
    for z in range(c):
      gazo[y][x][z] = Enc(pbk, n, gazo[y][x][z])

# Print encrypted image
gazo = np.array(gazo)
print( "Encrypted image" )
print(gazo)
plt.figure()
plt.imshow(gazo)



gazo2 = np.zeros((height,width, c))
gazo2 = gazo2.tolist()

# Apply filter to both images 
for x in range(1,(width-1)):
    for y in range(1,(height-1)):
      for z in range(3):
        filter = [
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9]
            ]
        gasochi = []
        gasochi_sample = 0
        for xx in range(3):
            for yy in range(3):
                # Apply filter to sample image
                gasochi_sample += sample_gazo[y+yy-1][x+xx-1][z] * filter[yy][xx]

                # Apply filter to encrypted image 
                filter[yy][xx] = Enc(pbk, n, filter[yy][xx]*27)              
                gasochi.append(gazo[y+yy-1][x+xx-1][z] * filter[yy][xx])
        gazo2[y][x][z] = gasochi
        sample_filter_gazo[y][x][z] = int(gasochi_sample)

# Decrypt image 
for y in range(height):
  for x in range(width):
    for z in range(c):
      if (width-1) > x >= 1 and (height-1) > y >= 1:
        gasochi3 = 0
        for zz in range(9):
          g = gazo2[y][x][z][zz]
          gasochi2 = Dec(pvk, n, int(g))/27
          gasochi3 += gasochi2
        gazo2[y][x][z] =  int(gasochi3)
      else: 
        gazo2[y][x][z] = int(Dec(pvk, n, int(gazo2[y][x][z])))

# Print decrypted image
gazo2 = np.array(gazo2)
print( "Decrypted image" )
print( gazo2 )
plt.figure()
plt.imshow(gazo2)

# Print sample image for comparison
sample_filter_gazo = np.array(sample_filter_gazo)
print("Sample image(no encryption)")
print( sample_filter_gazo )
plt.figure()
plt.imshow(sample_filter_gazo)
plt.show()












