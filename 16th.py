sum=0
count=0
largestsofar=-1
smallest=None
while True:
    n=input("enter a number:")
    #have to check if the input is 'done' or not
    if n=='done':
        break
    #check whether input in numeric value or not
    else:
        try:
            k=float(n)
        except:
            print("Invalid input")
            continue
    #first we will do the logic operator's work for largest and smallest value
    if(k>largestsofar):
        largestsofar=k
    if(smallest is None):
        smallest=k
    elif(smallest>k):
        smallest=k
    #then we will do the mathematical operator work for sum and average value
    sum=sum+k
    count=count+1
print("over")
print("sum=",sum)
print("total input=",count)
print("average=",sum/count)
print("largest number is=",largestsofar)
print("smallest number is=",smallest)
