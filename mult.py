def multiplic(num1,num2):
    mul=0
    while num2>0:
         mul=mul+num1
         num2=num2-1
    print("multiplication of these 2 numbers will be:\n",mul)
while True:
    a=input("enter 1st number:")
    b=input("enter 2nd number:")
    if a=='done' or b=='done':
        break
    else:
        num1=int(a)
        num2=int(b)
        multiplic(num1,num2)
print("PROGRAM DONE")
