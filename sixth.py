grade=input('enter a grade:')
g=float(grade)
if(g>1):
    print('input not in range')
    quit()
elif(g<0):
    print("input not in range")
    quit()
elif(g>0.9):
    print('A')
elif(g>0.8):
    print('B')
elif(g>0.7):
    print('C')
elif(g>0.6):
    print('D')
else:
    print('F')       
print("code over")
