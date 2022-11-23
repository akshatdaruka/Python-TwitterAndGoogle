
# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    n=len(s)
    f=list()
    magc=15
    for i in range(0,len(s)):
        sumd1 = 0
        c=list()
        for j in range(0,len(s[0])):
            sumd1 = sumd1 + s[i][j]
            c.append(s[i][j])
        print(c)
        if sumd1==magc:
            c.clear()
            continue
        else:
            s[i][j]=max(c)+(magc-sumd1)
            f.append(magc-sumd1)
            c.clear()
    for i in range(0,n):
        sumd1=0
        c=list()
        for j in range(0,n):
            sumd1=sumd1+s[j][i]
            c.append(s[j][i])
        print(c)
        if sumd1==magc:
            c.clear()
            continue
        else:
            s[j][i]=max(c)+(magc-sumd1)
            f.append(magc-sumd1)
            c.clear()
    fsum=0        
    for h in f:
        if h>0:
            fsum=fsum+h
    print(s)
    print(fsum)
    return(fsum)
s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))
result = formingMagicSquare(s)
print(result)
