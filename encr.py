def encryption(s):
    s=s.replace(" ", "")
    s=s.strip()
    sq=int(len(s) ** 0.5)
    w=sq
    h=sq
    if sq*(sq+1)<len(s):
        w=w+1
    if sq*sq==len(s):
        h=h-1
    lst=[[0 for j in range(h+1)] for i in range(w)]
    r=0
    for i in range(w):
        for j in range(h+1):
            if r<=len(s)-1:
                lst[i][j]=s[r]
            else:
                lst[i][j]=' '
            r=r+1
    c=""
    for i in range(h+1):
        c1=[row[i] for row in lst]
        c=c+str(c1)
    c=c.replace(" ","")
    c=c.replace("[","")
    c=c.replace(",","")
    c=c.replace("]"," ")
    c=c.replace("'","")
    return(c)
v=input("enter a string: ")
print(encryption(v))    
