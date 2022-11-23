#INDEXING SLICING AND ITERATING
import numpy as np
import math
a=np.array([1,2,3,4,5,6])
print(a[0])
print(a[3])
print(a[:3])
print(a[4:])
print(a[-1:0])
print(a[2:5])
#multi dimensional array:

b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(b[2,3])
print(b[1,3])
print(np.array([b[2,3],b[1,3],b[0,2]]))
#other method:ZIPING METHOD :
print(b[[2,1,0],[3,3,2]])
#boolean indexing:
print(b>=5)
print(b[b>=5])

print(b[:2])#first two rows
print(b[:, :2])#first two coloumns
print(b[:2, 1:3])#first two rows with column 1 to 3
#subarrays:
sub_array= b[:2,1:3]
print(sub_array)
sub_array[0,0]= 50
print(sub_array)
print(b)
