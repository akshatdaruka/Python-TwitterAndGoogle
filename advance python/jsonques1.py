import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode= ssl.CERT_NONE

url=input("Enter a url:")
hand=urllib.request.urlopen(url,context=ctx).read()

import json
info=json.loads(hand.decode())
sum=0
for items in info['comments']:
    a=int(items['count'])
    sum=sum+a
print(sum)
