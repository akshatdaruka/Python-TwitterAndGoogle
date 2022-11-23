d={'d':34,'b':23,'c':47}
abc=sorted(d.items())
print(abc)
cde=sorted(d.items(),reverse=True)
print(cde)
print("printing sorted by values instead of keys")
mno=list()
for k,v in d.items():
    newtup=(v,k)    #newtup is tuple
    mno.append(newtup) #mno will be the list of tuple
print(sorted(mno,reverse=True))
print(sorted(mno))
