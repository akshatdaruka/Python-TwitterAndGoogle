largest=None
smallest=None
sum=0
count=0
while True:
    gnum=input("enter a number".capitalize())
    if gnum=='done':
        break
    else:
        try:
            num=int(gnum)
        except:
            print("invalid input".capitalize())
            continue
        if largest is None or num>largest:
            largest=num
        if smallest is None or num<smallest:
            smallest=num
        sum=sum + num
        count=count + 1
print("total number entered are:".capitalize(),count)
print("sum of all number are:".capitalize(),sum)
print("average is:".capitalize(),sum/count)
print("largest no is:".capitalize(),largest)
print("smallest no is:".capitalize(),smallest)
