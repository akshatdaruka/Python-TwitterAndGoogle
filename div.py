
def division(a,b):
    count=0
    while a>=b:
        a=a-b
        count=count+1
    dcount=0
    x=a*10
    while x>=b:
        x=x-b
        dcount=dcount+1
    dcount1=0
    y=x*10
    while y>=b:
        y=y-b
        dcount1=dcount1+1
    dcount2=0
    z=y*10
    while z>=b:
        z=z-b
        dcount2=dcount2+1
    print("a/b:",count,".",dcount,dcount1,dcount2)
a=float(input("enter 1st number:"))
b=float(input("enter 2nd number:"))
division(a,b)
