import pandas as pd
import numpy as np
def average_influenza_doses():
    df=pd.read_csv('NISPUF17.csv')
    x=0
    y=0
    n=0
    m=0
    for ind in df.index:
        if df['CBF_01'][ind]==1 and np.isnan(df['P_NUMFLU'][ind])==False:
            x=x+(df['P_NUMFLU'][ind])
            n=n+1
        elif df['CBF_01'][ind]==2 and np.isnan(df['P_NUMFLU'][ind])==False:
            y=y+(df['P_NUMFLU'][ind])
            m=m+1
        else:
            continue
    tup=(x/n,y/m)
    print(tup)
average_influenza_doses()
