import re
name=input("enter a file name:")
fhand=open(name)
for line in fhand:
    lst=re.findall('\s(\(.+\))',line)
    if len(lst)>=1:
        print(lst)
