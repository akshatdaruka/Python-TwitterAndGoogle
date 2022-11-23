#Convert general timing to 24 hours format.
def timeConversion(s):
    if 'PM' in s :
        if s[0]=='1' and s[1]=='2':
            return s[0:8]
        else:
            k=int(s[0:2])+12
            val=(str(k).strip()+s[2:8].strip()).replace(" ","")
            return val
    elif 'AM' in s:
        if s[0]=='1' and s[1]=='2':
            k='00'
            val=(k+s[2:8].strip()).replace(" ","")
            return val
        else:
            return s[0:8]
n=input("enter a time: ")
if int(n[0:2])>12 or int(n[3:5])>60 or int(n[6:8])>60:
    print("enter valid time!")
else:
    print("Time in 24 hours format is:",end=" ")
    print(timeConversion(n))
