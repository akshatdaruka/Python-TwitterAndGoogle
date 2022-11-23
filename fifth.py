hours=input("enter the hours:")
rate=input("enter the rate:")
try:
    h=float(hours)
    r=float(rate)
except:
    print("please enter a numeric value")
    quit()
print("the input values are",h,",",r)
if(h>40):
    Pay=((h-40)*1.5*r)+(40*r)
else:
    Pay=h*r
print("Pay:",Pay)
