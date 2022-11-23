#reading a xml file saved in the system.
urlname=input("enter a url:")
uhand=open(urlname).read()
import xml.etree.ElementTree as ET
stuff=ET.fromstring(uhand)
lst=stuff.findall('comments/comment')
print("USER COUNT...",len(lst))
sum=0
for item in lst:
    a=int(item.find('count').text)
    sum=sum+a
print("sum of all the numbers in the file is...".upper(),sum)
