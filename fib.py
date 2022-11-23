#FIBONACCI SERIES:
n=int(input("enter the value of n: "))
f1=0
f2=1
if n==1:
    print("nth fibonacci no is:",f1)
elif n==2:
    print("nth fibonacci no is:",f2)
else:
    for i in range(0,n-2):
        f=f1+f2
        f1=f2
        f2=f
    print("nth fibonacci no is:",f)
