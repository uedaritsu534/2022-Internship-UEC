from RSAinternship import *
import numpy as np

k = 6
arr = np.array([[1,2], [3,4]])
x = np.array([[1], [2]])
pbk, pvk, n = key_gen(k)

print(pbk)

arr_height = len(arr)
arr_width = len(arr[0])
x_height = len(x)
x_width = len(x[0])

# Print matricies
print("Matrix 1")
print(arr)
print('')

print("Matrix 2")
print(x)
print('')

print("Product of Matrix1 and 2")
print(arr.dot(x))
print('')

# Encrypt matrix 1
for i in range(arr_height):
    for j in range(arr_width):
        arr[i][j] = Enc(pbk, n, arr[i][j])

print("Encrypted Matrix1(E1)")
print(arr)
print('')

# Encrypt matrix 2
for i in range(x_height):
    for j in range(x_width):
        x[i][j] = Enc(pbk, n, x[i][j])

print("Encrypted Matrix2(E2)")
print(x)
print('')

# Multiply the two matricies
prod = []
for k in range(x_width):
    for i in range(arr_height):
        prod_row = []
        for j in range(arr_width):
            prod_row.append(arr[i][j] * x[j][k])
        prod.append(prod_row)

print("Product of E1 and E2(no addition here)")
print(prod)
print('')

# Decrypt product
prod_height = len(prod)
prod_width = len(prod[0])
for i in range(prod_height):
    for j in range(prod_width):
        prod[i][j] = Dec(pvk, n, prod[i][j])

# Print decrypted product
print("Decrypted product")
print(prod)
print('')

# Do addition 
dec_prod = []
for i in range(prod_height):
    dec_row = []
    num = 0
    for j in range(prod_width):
        num += prod[i][j]
    dec_row.append(num)
    dec_prod.append(dec_row)

# Print final matrix
print("After addition")
print(dec_prod)