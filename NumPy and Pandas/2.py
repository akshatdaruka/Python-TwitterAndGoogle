# ARRAY OPERATION:
import numpy as np
import math

a=np.array([10,20,30,40])
b=np.array([1,2,3,4])

c=a+b
d=a-b
e=a*b
f=a/b
# all the above operation will be element wise only
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

farenhite= np.array([0,-10,-5,-15,0])
celcius= (farenhite-32)*(5/9)
print(celcius)

print(celcius>-20) #it will return true for every value in
#celcius array which is > -20 and false otherwise(boolean array)

#FOR MATRIX MULTIPLICATION WE USE '@'

A= np.array([[1,1],[0,1]])
B= np.array([[2,0],[3,4]])
print(A@B) #MATRIX MULTIPLICATION
print(A*B) #ELEMENTWISE MULTIPLICATION

#UPCASTING:

array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[7.1,8.2,5.6],[3.2,5.6,8.9]])
print(array1.dtype)
print(array2.dtype)
array3=array1+array2
print(array3)
print(array3.dtype) #arry3 will be of float type
#while manupulating array of 2 diff type the
#resultant type is more general of the 2
#this is called UPCASTING

#AGGREGATION FUNCTIONS:
#to find sum,max,min,mean etc. in a given array
print(array3.sum())
print(array3.max())
print(array3.min())
print(array3.mean())

# to make an array of a particular dimension we use
#reshape functions for example:
j= np.arange(1,16,1).reshape(3,5)  #here (3,5) is
print(j)                           #the dimension
g=np.arange(1,19,2).reshape(3,3)
print(g)
i=np.linspace(0,4,15).reshape(5,3)
print(i)
