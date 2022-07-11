
import numpy as np
import matplotlib.pyplot as plt
from RSAinternship import *
import cv2

gazo = cv2.imread( "./images/7134.png", 0 )
sample_gazo = cv2.imread( "./images/7134.png", 0 )
pbk, pvk, n = key_gen(6)

gazo = cv2.resize(gazo, dsize = None, fx = 0.05, fy = 0.05)
sample_gazo = cv2.resize(sample_gazo, dsize = None, fx = 0.05, fy = 0.05)
height, width = gazo.shape
print(height)
print(width)

# Print original image
print( "Original image" )
print( gazo )
plt.figure()
plt.imshow(gazo, cmap="gray", vmin=0, vmax=255)
gazo = gazo.tolist()

# Encrypt image
for y in range(height):
  for x in range(width):
      gazo[y][x] = Enc(pbk, n, gazo[y][x])

gazo = np.array(gazo)

# Print encrypted image
print( "Encrypted image" )
print(gazo)
plt.figure()
plt.imshow(gazo, cmap="gray", vmin=0, vmax=255)

# Apply filter to both images
gazo2 = np.zeros((height,width))
sample_filter_gazo = np.zeros((height, width))
gazo2 = gazo2.tolist()
for x in range(1,(width-1)):
    for y in range(1,(height-1)):
        filter = [
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]
            ]
        gasochi = []
        gasochi_sample = 0
        for xx in range(3):
            for yy in range(3):
              # Apply filter to sample image
              gasochi_sample += sample_gazo[y+yy-1][x+xx-1] * filter[yy][xx]

              #Apply image to encrypted image
              filter[yy][xx] = Enc(pbk, n, abs(filter[yy][xx]))              
              gasochi.append(gazo[y+yy-1][x+xx-1] * filter[yy][xx])
        gazo2[y][x] = gasochi
        if(gasochi_sample >= 255):
          gasochi_sample = 255
        elif(gasochi_sample <= 0):
          gasochi_sample = 0
        sample_filter_gazo[y][x] = int(gasochi_sample)

# Print list of encrypted image that has the filter applied
print( "Encrypted image w/ filter" )
print( gazo2 )

# Decrypt image
for y in range(height):
  for x in range(width):
    if (width-1) > x >= 1 and (height-1) > y >= 1:
      gasochi3 = 0
      for z in range(9):
        g = gazo2[y][x][z]
        gasochi2 = Dec(pvk, n, int(g))
        if(z == 4):
          gasochi3 -= gasochi2
        else: 
          gasochi3 += gasochi2
      gasochi3 = int(gasochi3)
      if(gasochi3 >= 255):
        gasochi3 = 255
      elif(gasochi3 <= 0):
        gasochi3 = 0
      gazo2[y][x] =  gasochi3
    else: 
      gazo2[y][x] = int(Dec(pvk, n, gazo2[y][x]))

# Print decrypted image
gazo2 = np.array(gazo2)
print( "Decrypted image" )
print( gazo2 )
plt.figure()
plt.imshow(gazo2, cmap="gray", vmin=0, vmax=255)

# Print sample image for comparison
print("Sample image(no encryption)")
print( sample_filter_gazo )
plt.figure()
plt.imshow(sample_filter_gazo, cmap="gray", vmin=0, vmax=255)
plt.show()