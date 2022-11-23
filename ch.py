p=int(input().strip())
a=list(map(int, input().rstrip().split()))
f=list()
res=True
for i in range(len(a)):
    c=list()
    c.append(a[i])
    for j in range(len(a)):
        for w in range(len(c)):
            if (c[w]-a[j])<=1 and (c[w]-a[j])>=-1 and i!=j:
                res=True
            else:
                res=False
                break
        if(res):
            c.append(a[j])
    print(c)
    f.append(len(c))
    c=c.clear()
print(f)
