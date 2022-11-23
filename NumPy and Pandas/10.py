#QUERRING SERIES:
import pandas as pd
students_classes={'Alice':'Physics',
'Jack':'Chemistry',
'Molly':'English',
'Sam':'History'}
s=pd.Series(students_classes)
print(s)
#querrying using loc and iloc :
print(s.iloc[3])
print(s.loc['Molly'])
#loc and iloc are not methods they are attributes.
#we can ignore using loc and iloc explicitly,
#pandas can itself recognize them on the
#basis of arguments passed:
print(s[3])
print(s['Molly'])
