#MERGING DATAFRAMES:
import pandas as pd
staff_df=pd.DataFrame([{'Name':'Kelly','Role':'Director of HR'},
{'Name':'Sally','Role':'Course Liasion'},{'Name':'James','Role':'Grader'}])
student_df=pd.DataFrame([{'Name':'James','School':'Business'},
{'Name':'Mike','School':'Law'},{'Name':'Sally','School':'Engineering'}])
staff_df=staff_df.set_index('Name')
student_df=student_df.set_index('Name')
print(staff_df.head())
print(student_df.head())
print("Outer join or union:")
print(pd.merge(staff_df,student_df,how='outer',left_index=True,right_index=True))
print("Inner join or intersection:")
print(pd.merge(staff_df,student_df,how='inner',left_index=True,right_index=True))
print("left join/all staffs no matter if thet are students or not:")
print(pd.merge(staff_df,student_df,how='left',left_index=True,right_index=True))
print("right join/all students no matter if they are staff or not:")
print(pd.merge(staff_df,student_df,how='right',left_index=True,right_index=True))
#we dont need to include index we can make any column as joining column:
staff_df=staff_df.reset_index()
student_df=student_df.reset_index()
#we will use 'on' parameter and pass list of joining column:
print(pd.merge(staff_df,student_df,how='right',on='Name'))
staff_df=pd.DataFrame([{'Name':'Kelly','Role':'Director of HR','Location':'ABC'},
{'Name':'Sally','Role':'Course Liasion','Location':'efg'},{'Name':'James','Role':'Grader','Location':'hio'}])
student_df=pd.DataFrame([{'Name':'James','School':'Business','Location':'edg'},
{'Name':'Mike','School':'Law','Location':'uyt'},{'Name':'Sally','School':'Engineering','Location':'kjh'}])
#here both the DataFrame have location column but we want to join them
#on name column and both can have different meaning of location like
#home address or office address so the merged DataFrame will preserve
#this information and append _x and _y to differentiate between 2 column with same name:
print(pd.merge(staff_df,student_df,how='left',on='Name'))
#multi-indexing :
#we can pass multiple column name to 'on' parameter:
staff_df=pd.DataFrame([{'First':'Kelly','Role':'Director of HR','Last':'Johnson'},
{'First':'Sally','Role':'Course Liasion','Last':'Watson'},{'First':'James','Role':'Grader','Last':'Smith'}])
student_df=pd.DataFrame([{'First':'James','School':'Business','Last':'Stones'},
{'First':'Mike','School':'Law','Last':'Lawrence'},{'First':'Sally','School':'Engineering','Last':'Watson'}])
print(pd.merge(staff_df,student_df,how='inner',on=['First','Last']))
