#.LOC IS USED TO ADD NEW DATA AS WELL:
import pandas as pd
s=pd.Series([1,2,3])
s.loc['History']=102
print(s)
#Examples of series where values are not unique:
students_classes=pd.Series({'Alice':'Physics','Jack':'Chemistry',
'Molly':'English','Sam':'History'})
print(students_classes)
kelly_classes=pd.Series(['Philosophy','Arts','Math'],
index=['Kelly','Kelly','Kelly'])
print(kelly_classes)
#using .append()
all_students_classes=students_classes.append(kelly_classes)
print(all_students_classes)
#if we will querry kelly in all_students_classes
#we will not get a single object but we will
#get a whole series:
print(all_students_classes['Kelly'])
