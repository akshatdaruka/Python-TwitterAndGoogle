import urllib.request, urllib.parse, urllib.error
urlname=input("enter a url:")
uhand=urllib.request.urlopen(urlname).read()
import xml.etree.ElementTree as ET
stuff=ET.fromstring(uhand)
lst=stuff.findall('commentinfo/comment')
sum=0
for item in lst:
    a=item.find('count').text
    sum=sum+a
print(sum)    
