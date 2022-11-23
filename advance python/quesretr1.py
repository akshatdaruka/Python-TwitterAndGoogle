import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
#ignore ssl certificate error
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("enter-")
html=urllib.request.urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,'html.parser')

#retreive all anchor tags
sum=0
tags=soup('span')
for tag in tags:
    a=int(tag.contents[0])
    sum=sum+a
print(sum)
