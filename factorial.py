def factori(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    print("Factorial is:",fact)
while True:
    a=input("enter a number:\n")
    if a=='done':
        break
    else:
        num=int(a)
        factori(num)
print("PROGRAM END!!")
