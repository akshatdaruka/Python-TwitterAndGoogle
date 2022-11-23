import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = False
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    address=input('Enter location:')
    if len(address)<1:
        break
    parms=dict()
    parms['address']=address
    if api_key is not False:parms['key']=api_key
    url=serviceurl+urllib.parse.urlencode(parms)
    print("========RETREIVING URL...",url,"========")
    uh=urllib.request.urlopen(url,context=ctx)
    data=uh.read().decode()
    print('RETREIVED',len(data),'CHARACTERS')
    try:
        js=json.loads(data)
    except:
        js=None
    if not js or 'status' not in js or js['status']!='OK':
        print('====FAILURE TO RETREIVE====')
        print(data)
        continue
    #print(json.dumps(js,indent=2))
    place_id=js['results'][0]['place_id']
    print("place id:".upper(),place_id)
    location=js['results'][0]['formatted_address']
    print("location:".upper(),location)
    lat=js['results'][0]['geometry']['location']['lat']
    lng=js['results'][0]['geometry']['location']["lng"]
    print("latitude:".upper(),lat)
    print("longitude:".upper(),lng)
