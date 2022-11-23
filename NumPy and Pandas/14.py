#DATAFRAME:
import pandas as pd
record1=pd.Series({'Name':'Alice',
'Class':'Physics','Score':85})
record2=pd.Series({'Name':'Jack',
'Class':'Chemistry','Score':82})
record3=pd.Series({'Name':'Helen',
'Class':'Biology','Score':90})
df=pd.DataFrame([record1,record2,record3],index=['school1','school2','school1'])
print(df.head())
#alternate way of creating dataframe:
students=[{'Name':'Alice',
'Class':'Physics','Score':85},
{'Name':'Jack',
'Class':'Chemistry','Score':82},
{'Name':'Helen',
'Class':'Biology','Score':90}]
df1=pd.DataFrame(students,index=['school1','school2','school1'])
print(df1.head())
#using iloc and loc attributes:
print(df.loc['school2'])
print(type(df.loc['school2']))
print(df.loc['school1'])
print(type(df.loc['school1']))
#giving 2 attributes to loc():
print(df.loc['school1','Name'])
print(df.T)
print(df.T.loc['Name'])
#indexing operator in DataFrame in pandas
#is reserved for column selection
#iloc and loc is for row selection:
print(df['Name'])
#if we will use iloc/loc with column name, we will get error.
#CHAINING OPERATIONS TOGETHER:
print(df.loc['school1']['Name'])
#CHAINING returns the copy of dataframe rather than
#returning the view.It can be slow.
#SLICING:
print(df.loc[:,['Name','Score']])
#the first parameter is the no of rows we want to see
#the second parameter is the names of columns we want to see.
#DROP() FUNCTION:
#it takes a single parameter of which row to be dropped.
print(df.drop('school1'))
#it doesn't change the actuall dataframe.
print(df)
#drop() have 2 optional parameters,
#1st is inplace, if it's set to true then
#DATAFRAME will be updated instead of
#copy being returned.
#2nd is axis,by default it's value is 0
#which means the row will be dropped
#if it's set to 1 then column will be dropped.
copy_df=df.copy()
copy_df.drop('Name',inplace=True,axis=1)
print(copy_df)
#other way of deleting a column using del keyword
#with indexing opeartor:
del copy_df['Class']
print(copy_df)
#Adding new row to the dataframe:
df['Class_Ranking']=None
#new column named Class_Ranking with value
#None is being added to dataframe df:
print(df)
