x=int(input("enter 1st no.:"))
y=int(input("enter 2nd no.:"))
z=int(input("enter 3rd no.:"))
print("previous sequence is:\n")
print("x=",x,"\ny=",y,"\nz=",z)
x=x+y+z
y=x-y-z
z=x-y-z
x=x-y-z
print("sequence after swapping is:\n")
print("x=",x,"\ny=",y,"\nz=",z)
print("different sequence::\n")
x=x+z
z=x-z
x=x-z
print("x=",x,"\ny=",y,"\nz=",z)
