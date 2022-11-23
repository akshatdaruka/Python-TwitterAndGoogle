#PRIME NUMBER:
x=input("enter a number:")
num=int(x)
for i in range(2,num):
    if num%i==0:
        print("no is not prime.")
        break
    elif (num%i!=0) and(i==num-1) :
        print("no is prime")
    else :
        continue
a=int(input('enter a number: '))
b=int(input('enter another number: '))
print("prime nos between",a,'and',b,'is:')
for d in range(a,b):
    for o in range(2,d):
        if d%o==0:
            break
    else:
        print(d)
