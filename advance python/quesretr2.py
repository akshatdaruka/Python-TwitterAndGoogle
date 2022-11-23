import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
def findinga(url,pos):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    i=0
    for tag in tags:
        i=i+1
        if i==pos:
            return (tag.get('href',None))
l=input("enter a number")
ti=int(l)
cur_num=0
while(cur_num<ti):
    print("Retreiveing:",url)
    url=findinga(url,18)
    cur_num=cur_num+1
print(url)
