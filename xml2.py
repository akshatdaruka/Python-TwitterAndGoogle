import xml.etree.ElementTree as ET
input='''<stuff>
<users>
 <user x="2">
  <id>001</id>
  <name>Akshat</name>
 </user>
 <user x="7">
  <id>007</id>
  <name>Daruka</name>
 </user>
</users>
</stuff>'''
stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('user count:',len(lst))
for items in lst:
    print('name:',items.find('name').text)
    print('id:',items.find('id').text)
    print('attribute:',items.get("x"))
