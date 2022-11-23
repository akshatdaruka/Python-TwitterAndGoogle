#FIBONACCI NUMBER:
n=int(input("enter a number: "))
f1=0
f2=1
while(True):
    f=f1+f2
    f1=f2
    f2=f
    if f==n or n==0:
        print("it is a fibonacci number")
        break
    elif f>n:
        print("it is not a fibonacci number")
        break
    else:
        continue
