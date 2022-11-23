longest=None
smallest=None
total=0
while(True):
    k=input("enter a number:")
    if k=='done':
        break
    else:
        try:
            num=int(k)
        except:
            print("enter a integer value")
            continue
    total=total+1
    if longest==None or longest<num:
        longest=num
    if smallest== None or smallest>num:
        smallest=num
print("Total number of inputs are:",total)
print("Largest number in the list is:",longest)
print("Smallest number in the list is:",smallest)
