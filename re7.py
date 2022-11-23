#check if a number is a perfect square:
n=int(input("enter a number: "))
x=0
while(True):
    x=x+1
    if(n==(x*x)):
        print("the number is a perfect square.")
        break
    elif(n<(x*x)):
        print("the number is not a perfect square.")
        break
    else:
        continue
