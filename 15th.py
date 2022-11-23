sum=0
count=0
while True:
    n=input("enter a number:")
    if n=='done':
        break
    else:
        try:
            k=int(n)
        except:
            print("invalid input")
            continue
    sum=sum+k
    count=count+1
print("over")
print("sum=",sum)
print("total input=",count)
print("average=",sum/count)
