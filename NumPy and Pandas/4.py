#USING NUMPY TO MANIPULATE AND MANAGE A DATASET

import numpy as np
import math

cars=np.genfromtxt("dataset1.csv",delimiter=',',skip_header=1,dtype=None,names=('s.no.',
'manufacturer','model','displ','year','cyl','trans','drv','cty','hwy','fl','class'))
#this will be a one dimensional array with 234 tuples:
print(cars['manufacturer'][0:12])
#modify a whole column:
cars['displ']=cars['displ']*10
print(cars['displ'][0:20])
print(len(cars[cars['displ']< 30]))
print(cars[cars['displ']< 30]['cyl'].mean())
print(cars[cars['displ']< 20]['cty'].mean())
print(cars[cars['displ']< 20]['hwy'].mean())
