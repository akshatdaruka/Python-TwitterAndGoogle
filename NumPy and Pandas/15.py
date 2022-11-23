#DATAFRAME INDEXING AND LOADING:
#we will use csv(comma seperated files) files datasets.
import pandas as pd
df=pd.read_csv('Admission_predict.csv')
#the function read_csv() will read and store a csv
#file into a variable df.
print(df.head())
#to make already existing column as index we
#use index_col attibute:
df=pd.read_csv('Admission_predict.csv',index_col=0)
#we can rename a column rename() function.
#we have to pass a dictionary with keys as
#old column name and values as new column name
new_df=df.rename(columns={'SOP':'Statement of Purpose',
'LOR':'Letter of recomendation'})
print(new_df.head())
#we might see that the column name is not
#changed, due to non matching to of the
#exact column name with that of the keys
#due to unwanted white spaces or something
#we can check the exact column name
#using attribute .columns
print(df.columns)
#to clear the whitespaces from column
#or row we use .strip() as a mapper
#parameter, and indicate it the axis
#wether row or column.
new_df=new_df.rename(mapper=str.strip,axis='columns')
print(new_df.head())
#we can also use df.columns attribute by
#assigning to it a list of column names
#which will directly rename the column
cols=list(df.columns)
cols=[x.lower().strip() for x in cols]
df.columns=cols
print(df.head())
