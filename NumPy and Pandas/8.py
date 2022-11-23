#PANDAS:
#SERIES DATA STRUCTURES:

import pandas as pd

students=['Alice','Jack','Molly']
print(pd.Series(students))

numbers=[1,2,3,4]
print(pd.Series(numbers))

#handling missing datas:

student1=['Alice','Jack',None]
print(pd.Series(student1))

number1=[1,2,None]
print(pd.Series(number1))

#NaN and None are not the same;
#they are used to represent missing data
#but there structures are different
#NaN is a floating point value
#NaN is not equuivalent to None

import numpy as np

print(np.nan==None)
print(np.nan==np.nan)
# .isnan() function are used to check for NaN
print(np.isnan(np.nan))
