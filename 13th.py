found=False
print("before",found)
for value in [3,67,5,45,3,23,45,6,98]:
    if(value==45):
        found=True
        print(value,found)
        quit()
    
print("after",found)
