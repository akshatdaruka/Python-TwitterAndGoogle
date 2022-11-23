#check a number is a perfect cube or not:
n=int(input("enter a number: "))
x=0
while(True):
    x=x+1
    if(n==(x*x*x)):
        print("Number is a perfect cube.")
        break
    elif(n<(x*x*x)):
        print("Number is not a perfect cube.")
        break
    else:
        continue        
