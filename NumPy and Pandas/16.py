#QUERYING DATAFRAME:
#boolean masking:boolean mask is an array which
#each value is either True or False
import pandas as pd
df=pd.read_csv('Admission_predict.csv')
df.columns=[x.lower().strip() for x in df.columns]
print(df.head())
#boolean mask are created by applying
#indexing operator and comparison opeators
#directly to pandas series/dataframe objects
admit_mask=df['chance of admit']>0.7
print(admit_mask)
#result of broadcasting a comparison operator is
#a boolean mask. Underneath pandas is applying
#comparison operator through vectorization.
#Here the result will be a series because
#only one column is being operated on, filled
#with true or false values.
#Now we can use this boolean mask to 'hide' the
#data we dont want(false values)
#we will use .where() function for this
print(df.where(admit_mask).head())
#the result will be as:
#where the chance of admit is >0.7
#there all datas will be there, and
#where the condition is false it will
#be NaN written there.
#If we don't want NaN to be written there
#and only want datas which match the condition
#we will use .dropna() function.
print(df.where(admit_mask).dropna().head())
#we don't have to use .where() and .dropona()
#everytime, we have a syntax that can be used
#insted
print(df[df['chance of admit']>0.7].head())
#The indexing operator on dataframe does:
#1.Can be called with a string parameter
#to project a single column :
print(df['gre score'].head())
#2.we can also send a list of column as string:
print(df[['gre score','toefl score']].head())
#3.we can send it a boolean mask:
print(df[df['gre score']>320].head())
#COMBINING MULTIPLE BOOLEAN MASK :
#we can't use 'and' or 'or' as the python
#underneath dont know how to compare 2 series
#or dataframes object using 'and' or 'or'
#we will use pipe(|) and ampersand(&) operator
print((df['chance of admit']>0.7)&(df['chance of admit']<0.9))
#we have to use parantheses around the individual
#terms we are interested in.
#Another way of doing this is by getting rid of
#comparison operator and using built in functions:
print(df['chance of admit'].gt(0.7)&df['chance of admit'].lt(0.9))
#we can also chain them together as these functions
#are build right into the series or dataframe objects:
print(df['chance of admit'].gt(0.7).lt(0.9))
