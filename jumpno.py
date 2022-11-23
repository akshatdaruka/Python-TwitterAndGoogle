x=input("enter a number")
if(len(x)==1):
    print("jumping number.")
for a in range(0,len(x)-1):
    if len(x)==2:
        if int(x[a])==int(x[a+1])+1:
            continue
        elif int(x[a])==int(x[a+1])-1:
            continue
        else:
            print("non jumping")
            break
    else:
        if (int(x[a])==int(x[a-1])+1 or int(x[a])==int(x[a-1])-1) and (int(x[a])==int(x[a+1])-1 or int(x[a])==int(x[a+1])+1):
            continue
        else:
            print('non jumping')
            break
