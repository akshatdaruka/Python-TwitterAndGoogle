name=input("enter file name")
fhand=open(name)
count=dict()
for lines in fhand:
    words=lines.split()
    for word in words:
        count[word]=count.get(word,0)+1
#lst=list()
#for k,v in count.items():
#    lst.append((v,k))
#lstn=sorted(lst,reverse=True)
#for val,key in lstn[:10]:
#    print(key,val)
print('\n10 most common word and there no of occurence is:')
nlst=sorted([(v,k) for k,v in count.items()],reverse=True)
for val,key in nlst[:10]:
    print(key,":",val)
rlst=sorted([(v,k) for k,v in count.items()])
print('\n10 most leat occured word and there no of occurence is:')
for val,key in rlst[:10]:
    print(key,":",val)
