largest=None
smallest=None
sum=0
count=0
largestline=None
smallestline=None
name=input("enter a file name:".upper())
try:
    fhand=open(name)
except:
    print("enter a valid file name".capitalize())
    quit()
for lines in fhand:
    first=lines.find(":")
    end=lines.find(" ",first)
    gnum=lines[first+1:end]
    try:
        num=float(gnum)
    except:
        print("invalid input".upper())
        continue
    if largest is None or num>largest:
        largest=num
        largestline=lines
    if smallest is None or num<smallest:
        smallest=num
        smallestline=lines
    sum=sum + num
    count=count + 1
print("total no of items:".upper(),count)
print("most expensive items is".capitalize(),largestline.rstrip())
print("cheapest item is".upper(),smallestline.rstrip())
print("suM oF aLl pRoDucT Is:".lower(),sum)
