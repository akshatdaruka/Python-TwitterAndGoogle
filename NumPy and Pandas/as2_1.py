import pandas as pd
def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    df=pd.read_csv('NISPUF17.csv')

    a=0
    b=0
    c=0
    d=0
    for x in df['EDUC1']:
        if x==1:
            a=a+1
        elif x==2:
            b=b+1
        elif x==3:
            c=c+1
        elif x==4:
            d=d+1
    l=len(df['EDUC1'])
    a1=a/l
    b1=b/l
    c1=c/l
    d1=d/l
    e={"less than high school":a1,
        "high school":b1,
        "more than high school but not college":c1,
        "college":d1}
    return(e)

    raise NotImplementedError()
print(proportion_of_education())
assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
