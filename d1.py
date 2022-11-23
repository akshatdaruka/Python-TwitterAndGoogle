dtn=dict()
names=list()
while True:
    k=input("enter a name:")
    if k=='done':
        break
    else:
        names.append(k)
#for name in names:
#    if name not in dtn:
#        dtn[name]=1
#    else:
#        dtn[name]=dtn[name]+1
for name in names:
    dtn[name]=dtn.get(name,0)+1
print(dtn)
