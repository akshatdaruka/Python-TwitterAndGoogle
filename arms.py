#ARMSTRONG NUMBER:
x=input('enter a number')
sum=0
for i in x:
    num=int(i)
    sum=sum+(num*num*num)
inum=int(x)
if (inum==sum):
    print("the given number is armstrong.")
else:
    print("the given number is not armstrong.")
