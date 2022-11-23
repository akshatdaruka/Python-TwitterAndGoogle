sig=input("enter a sign of seperation: ")
inputs=input("enter numbers seperated by above sign: ")
a=list()
for k in inputs.split(sig):
    a.append(int(k))
largest=None
smallest=None
for num in a:
    if(largest is None or num>largest):
        largest=num
    if(smallest is None or num<smallest):
        smallest=num
#print(a)
print('Largest:',largest)
print('Smallest:',smallest)
