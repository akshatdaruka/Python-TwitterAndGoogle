sig=input("enter the sign of seperation: ")
inputs=input("enter numbers seperated by above sign: ")
largest=None
smallest=None
for k in inputs.split(sig):
    num=int(k)
    if largest is None or num>largest:
        largest=num
    if smallest is None or num<smallest:
        smallest=num
print('Largest:',largest)
print('smallest:',smallest)            
