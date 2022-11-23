fname=input("enter a file name")
fhand=open(fname)
count=0
acount=0
inp=fhand.read()
for lines in fhand:
    count=count+1
print('total lines is',count)
print('total a in the file is',acount)
print("total character in the file is",len(inp)-9)
for words in inp:
    if "a" in words:
        acount=acount+1
print('total  a is',acount)        
