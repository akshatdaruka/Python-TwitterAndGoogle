def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    df=pd.read_csv('NISPUF17.csv')
    df=df[df['P_NUMVRC']>=0]
    df=df[(df['HAD_CPOX']==1)|(df['HAD_CPOX']==2)]
    df2=df[['P_NUMVRC','HAD_CPOX']].dropna()
    print(len(df2))
    print(df2.head(10))
    corr, pval=stats.pearsonr(df["HAD_CPOX"],df["P_NUMVRC"])
    return corr
print(corr_chickenpox())
