#FIBONACCI SERIES:
n=int(input("enter the value of n: "))
f1=0
f2=1
print("the n terms in fibonacci series is:")
print(f1)
print(f2)
for i in range(0,n-2):
    f=f1+f2
    f1=f2
    f2=f
    print(f)
