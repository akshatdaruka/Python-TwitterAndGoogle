filename=input("ENTER A FILE NAME: ")
fhandle=open(filename)
count=dict()
for lines in fhandle:
    line = lines.split()
    for word in line:
        count[word]= count.get(word,0)+1
for (a,b) in sort(count).items()
    print(a,b)
