count=list()
def division(a,b,c):
    cou=0
    while(c>0):
        while a>=b:
            a=a-b
            cou=cou+1
        count.append(cou)
        c=c-1
        a=a*10
        division(a,b,c)
    #for num in count:///
    #[''['
    #[]']]
        print(num)
a=int(input("enter divident:"))
b=int(input("enter divider:"))
c=int(input("enter the no of time"))
division(a,b,c)
