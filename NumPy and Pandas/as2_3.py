import pandas as pd
#P_NUMVRC-vaccine doses
#SEX- gendre of the child
#HAD_CPOX- had chicken pox
def chickenpox_by_sex():
    df=pd.read_csv('NISPUF17.csv')
    a=0
    b=0
    c=0
    d=0
    for ind in df.index:
        if df['SEX'][ind]==1 and df['P_NUMVRC'][ind]>0:
            if(df['HAD_CPOX'][ind]==1):
                a=a+1
            if(df['HAD_CPOX'][ind]==2):
                b=b+1
        elif df['SEX'][ind]==2 and df['P_NUMVRC'][ind]>0:
            if(df['HAD_CPOX'][ind]==1):
                c=c+1
            if(df['HAD_CPOX'][ind]==2):
                d=d+1
        else:
            continue
    e=dict()
    e={"male":(a/b),
    "female":(c/d)}
    return e
print(chickenpox_by_sex())
