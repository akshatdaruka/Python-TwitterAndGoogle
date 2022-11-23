name=input("enter a file name")
handle=open(name)
count=dict()
for lines in handle:
    words=lines.split()
    for word in words:
        count[word]=count.get(word,0)+1
bigword=None
bigcount=None
smallcount=None
smallword=None
for k,v in count.items():
    if bigcount is None or v>bigcount:
        bigcount=v
    if smallcount is None or v<smallcount:
        smallcount=v
for k,v in count.items():
    if bigcount==v:
        print("words which occured MOST no of time is:",k)
        print("no of occurence:",v)
        print("\n")
    if smallcount==v:
        print("words which occured LEAST no of time is:",k)
        print("no of occurence:",v)
        print("\n")
