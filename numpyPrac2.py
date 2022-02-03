# Importing Numpy library
import numpy as np


# Create a on dimensional array which contain the cube from 0 to 9
a = np.arange(10)**3

# Printing the array
print(a)

# Indexing of the Array
print(a[2])
# Slicing the aaray
print(a[2:5])

# From start to position 6, exclusive, set every element to 1000
a[:6:2] = 1000

print(a)

# to reverse the array
print(a[::-1])