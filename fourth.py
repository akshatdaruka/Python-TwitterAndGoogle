astr=input('enter a value:')
try:
    istr=int(astr)
except:
    istr=-1
if(istr==-1):
    print('please enter a numeric value')
else:
    print('success',istr)
