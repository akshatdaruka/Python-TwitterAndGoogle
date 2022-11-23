#print the ascii values:
while(True):
    k=input("enter a character: ")
    if(k=='done'):
        break
    elif(len(k)>1):
        print("enter a single character please.")
        continue    
    else:
        print('ASCII value of given character is:',ord(k))
