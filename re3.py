a=input('enter total no of inputs:')
num=int(a)
print('enter the numbers:')
smallest=None
largest=None
while(num>0):
    b=input()
    no=int(b)
    num=num-1
    if largest is None or no>largest:
        largest=no
    if smallest is None or no<smallest:
        smallest=no
print('Largest number is:',largest)
print('Smallest number is:',smallest)
