smallest=None
print("before")
for value in [4,67,56,4,3,5,2,1,45,68]:
    if smallest is None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest,value)
print("after",smallest)        
