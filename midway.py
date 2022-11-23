sum=0
number=0
largestsofar=None
smallest=None
while True:
    n=input("type a number:")
    if n=='done':
        break
    else:
        try:
            num=float(n)
        except:
            print('invalid input')
            continue
        sum=sum+num
        number=number+1
        if largestsofar is None:
            largestsofar=num
        elif num>largestsofar:
            largestsofar=num
        if smallest is None:
            smallest=num
        elif num<smallest:
            smallest=num
print('total no of input are',number)
print('sum of all input are',sum)
print('largest no is',largestsofar)
print('smallest no is',smallest)
