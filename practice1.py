import re
sum=0
name=input("enter a file name:")
fhand=open(name)
flist=list()
for lines in fhand:
    lines=lines.rstrip()
    lst=re.findall('\s*([0-9]+)\s*',lines)
# in the above case the numbers are preceeded And
# succeeded by whitespace and '\s' is used for
# matching with whitespace and also we only need
# numeric parts so ([0-9]+)--> one or more digit
    for nums in lst:
        num=int(nums)
        flist.append(num)
        sum=sum+num
print("sum:",sum)
print("list of all numbers :")
print(sorted(flist))
print("max is:",max(flist))
print("min is:",min(flist))
