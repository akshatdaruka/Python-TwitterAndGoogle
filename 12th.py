largestsofar=-1
sum=0
zork=0
print("before",largestsofar)
for num in [9,7,3,2,1,87,56,99,76,54]:
    zork=zork+1
    if num>largestsofar:
        largestsofar=num
    print(largestsofar,num)
    sum=sum+num
print("total no of things:",zork)
print("largest no",largestsofar)
print("sum is",sum)
print("average is:",sum/zork)
smallest=largestsofar
for value in  [9,7,3,2,1,87,56,99,76,54]:
    if value<smallest:
        smallest=value
print("smallest number is",smallest)
