stuff=list()
while True:
    a=input('enter an element:')
    if a=='end':
        break
    else:
        stuff.append(a)
print('list formed is\n',stuff)
g=input("enter a number")
if g in stuff:
    print(g,"is in the list")
else:
    print(g,"is not in the list")
