import numpy as np

a = np.arange(15).reshape(3,5)

print(a)

print(a.ndim)

print(a.dtype.name)

print(a.itemsize)

print(a.size)

b = np.array([6,7,8])


print(b)

print(type(b))

print(b.dtype)

c = np.array([(1,2,3,4),(5,6,7,8)],dtype=complex)

print(c)

d=  np.zeros((4,5))

print(d)

e = np.ones((3,3,4))

print(e)