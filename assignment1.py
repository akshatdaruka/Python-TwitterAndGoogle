import re
name=input("enter a file name:")
fhand=open(name)
sum=0
for line in fhand:
    stuff=re.findall('\s*([0-9]+)\s*',line)
    for num in stuff:
        rnum=int(num)
        sum=sum+rnum
print(sum)
