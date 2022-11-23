#CREATING PANDAS SERIES DATA STRUCTURES:

import pandas as pd
student_score={'Alice':'Physics',
'Jack':'Chemistry',
'Molly':'English'}
s=pd.Series(student_score)
print(s)
print(s.index)

students=[('Alice','Brown'),('Jcak','White'),('Molly','Green')]
print(pd.Series(students))

p=pd.Series(['Physics','Chemistry','English'],index=['Alice','Jack','Molly'])
print(p)

#non alignment of dictionary keys and index values:
student_score1={'Alice':'Physics',
'Jack':'Chemistry',
'Molly':'English'}
k=pd.Series(student_score1,index=['Jack','Molly','Sam'])
print(k)
