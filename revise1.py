#program to find 20 most and least common word in a text file!!
count=dict()
name=input("enter a file name:\n")
fhand=open(name)
for lines in fhand:
    words=lines.split()
    for word in words:
        count[word]=count.get(word,0)+1
print("COUNTING..............\n")
nlst=sorted([(v,k) for k,v in count.items()],reverse=True)
print("20 most common word are:\n")
for v,k in nlst[:20]:
    print(k,":",v)
nlst1=sorted([(v,k) for k,v in count.items()])
print("\n20 least common words are:\n")
for v,k in nlst1[:20]:
    print(k,":",v)
