sum=0
count=0
largest=None
smallest=None
largestline=" "
smallestline=" "
fname=input("enter a file name:".capitalize())
try:
    fhand=open(fname)
except:
    print("enter a valid file name")
    quit()
for lines in fhand:
    start=lines.find(":")
    end=lines.find(" ",start)
    value=lines[start+1:end]
    try:
        ivalue=float(value)
    except:
        print("input invalid",value)
        continue
    if largest is None:
        largest=ivalue
        largestline=lines
    elif ivalue>largest:
        largest=ivalue
        largestline=lines
    if smallest is None:
        smallest=ivalue
        smallestline=lines
    elif smallest>ivalue:
        smallest=ivalue
        smallestline=lines
    sum=sum+ivalue
    count=count+1
print("total items are:".upper(),count)
print("total sum of all products is:".upper(),sum)
print("average is:".upper(),sum/count)
print("cheapest item is".upper(),smallestline.rstrip())
print("most expensive item is".upper(),largestline.rstrip())
