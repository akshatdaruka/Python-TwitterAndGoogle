#manipulate data:
import pandas as pd
grades=pd.Series([90,70,80,60])
total=0
for grade in grades:
    total+=grade
print(total/len(grades))
#vectorization:
#we can write the above code using
#the numpy sum method
import numpy as np
total=np.sum(grades)
print(total/len(grades))
