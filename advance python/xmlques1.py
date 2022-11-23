import urllib.request, urllib.parse, urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
urlname=input("enter a url:")
uhand=urllib.request.urlopen(urlname,context=ctx).read()
import xml.etree.ElementTree as ET
stuff=ET.fromstring(uhand)
lst=stuff.findall('comments/comment')
sum=0
for item in lst:
    a=int(item.find('count').text)
    sum=sum+a
print(sum)
