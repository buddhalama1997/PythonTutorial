# Importing numpy library
import numpy as np

# Create a function
def f(x,y):
    return 10*x + y

# Creating a multidimensional array using above function
b = np.fromfunction(f, (5,4), dtype=int)

# print b
print(b)


# print the value where x = 2 and y = 3
print(b[2,3])

# print the each row in the second column of b
print(b[:,1])

# print the value till 4th row in the second column of b
print(b[0:4,1:3])

# for loop to print the row of b

for row in b:
    print(row)

# For printing the each elements

for element in b.flat:
    print(element)