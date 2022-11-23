score = input("Enter Score: ")
sg=float(score)
try:
    if(sg>1):
	    print('OUT OF RANGE')
    elif(sg<0):
        print('OUT OF RANGE')
        quit()
except:
    if(sg>=0.9):
        print('A')
    elif(sg>=0.8):
        print('B')
    elif(sg>=0.7):
        print('C')
    elif(sg>=0.6):
	    print('D')
    else:
	    print('F')
