import re
sum=0
name=input("enter a file name:")
fhand=open(name)
for line in fhand:
    line=line.rstrip()
    if re.search('^W.*t$',line):
        print(line)

for line in fhand:
    lst=re.findall('\s(\(.+\))',line)
    if len(lst)>=1:
        print(lst)
