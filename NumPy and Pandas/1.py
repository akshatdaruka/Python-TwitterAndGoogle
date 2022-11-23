import numpy as np
import math

a= np.array([1,2,3])
print(a)
print(a.ndim)    #print dimension of array

b= np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)   # shape of the attribute it returns a tuple value
b.dtype.name     # returns the data type stored in the array

d= np.zeros((2,3))   #array with placeholder zeros dimension 2*3
e= np.ones((2,3))   # array with placeholder one with dim 2*3
print(d)
print(e)

print(np.random.rand(2,3))  # generate array with random values

f=np.arange(10,50,2)    # generate a sequence starting with 10 with a
        #difference of 2 between consequitive number till 50 (exclusive)
print(f)

g= np.linspace(0,2,15)  # generate a array starting with 0 ending with 2 both
         # inclusive and having 15 numbers between them (float)
print(g)
