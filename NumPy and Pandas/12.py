import pandas as pd
import numpy as np
numbers=pd.Series(np.random.randint(0,100,100))
#BROADCASTING:
print(numbers.head())
numbers+=2
print(numbers.head())
#procedural way of doing this is by
#iterating through the series using
#.iteritems()
for label,value in numbers.iteritems():
    numbers.loc[label]=value+2
print(numbers.head())
